pip install -r requirements.txt.\.venv\Scripts\Activate.ps1
import streamlit as st
from supabase import create_client
import hashlib, secrets
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="Coffre Vidéo (MVP)", layout="centered")

sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def now_utc():
    return datetime.now(timezone.utc)

def get_or_create_vault(owner_user_id: str):
    res = sb.table("vaults").select("*").eq("owner_user_id", owner_user_id).execute()
    if res.data:
        return res.data[0]
    created = sb.table("vaults").insert({"owner_user_id": owner_user_id, "title": "Mon coffre"}).execute()
    return created.data[0]

st.title("Coffre Vidéo Posthume — MVP")

# ---------------------------
# 1) Auth simple via Supabase
# ---------------------------
with st.expander("Créer un compte", expanded=False):
    reg_email = st.text_input("Email", key="reg_email")
    reg_pwd = st.text_input("Mot de passe", type="password", key="reg_pwd")
    if st.button("Créer mon compte"):
        try:
            sb.auth.sign_up({"email": reg_email, "password": reg_pwd})
            st.success("Compte créé. Tu peux te connecter.")
        except Exception as e:
            st.error(f"Erreur création: {e}")

st.subheader("Connexion")
email = st.text_input("Email", key="login_email")
pwd = st.text_input("Mot de passe", type="password", key="login_pwd")

if st.button("Se connecter"):
    try:
        auth = sb.auth.sign_in_with_password({"email": email, "password": pwd})
        st.session_state["user_email"] = email
        st.session_state["user_id"] = auth.user.id
        st.success("Connecté.")
    except Exception as e:
        st.error(f"Erreur login: {e}")

if "user_id" not in st.session_state:
    st.info("Connecte-toi pour voir ton coffre.")
    st.stop()

user_id = st.session_state["user_id"]
user_email = st.session_state["user_email"]

vault = get_or_create_vault(user_id)

st.sidebar.write(f"Connecté : {user_email}")
st.sidebar.write(f"Vault : {vault['id']}")

tab1, tab2, tab3 = st.tabs(["Uploader", "Bénéficiaires", "Accès token"])

# ---------------------------
# 2) Upload + save metadata
# ---------------------------
with tab1:
    st.subheader("Uploader une vidéo")
    title = st.text_input("Titre", value="Mon message", key="vid_title")
    file = st.file_uploader("Choisir une vidéo", type=["mp4", "mov", "m4v", "webm"])

    if st.button("Uploader", disabled=(file is None)):
        try:
            object_key = f"{vault['id']}/{secrets.token_hex(8)}_{file.name}"
            bucket = sb.storage.from_("video-wills")
            bucket.upload(object_key, file.getvalue(), {"content-type": file.type or "video/mp4"})

            ins = sb.table("videos").insert({
                "vault_id": vault["id"],
                "title": title,
                "storage_path": object_key,
                "released": False
            }).execute()

            st.success("Vidéo uploadée.")
            st.write(ins.data[0])

        except Exception as e:
            st.error(f"Erreur upload: {e}")

    st.markdown("### Mes vidéos")
    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if not vids:
        st.info("Aucune vidéo pour l'instant.")
    else:
        for v in vids:
            st.write(f"- {v['title']} | released={v['released']} | id={v['id']}")

# ---------------------------
# 3) Beneficiaries + token
# ---------------------------
with tab2:
    st.subheader("Bénéficiaires")
    ben_email = st.text_input("Email du bénéficiaire", key="ben_email")
    if st.button("Ajouter", disabled=(not ben_email)):
        try:
            sb.table("beneficiaries").insert({"vault_id": vault["id"], "email": ben_email}).execute()
            st.success("Bénéficiaire ajouté.")
        except Exception as e:
            st.error(f"Erreur: {e}")

    bens = sb.table("beneficiaries").select("*").eq("vault_id", vault["id"]).execute().data
    st.write([b["email"] for b in bens] if bens else "Aucun")

    st.subheader("Libérer une vidéo (manuel)")
    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if vids and bens:
        video_choice = st.selectbox("Vidéo", vids, format_func=lambda x: f"{x['title']} ({x['id']})")
        ben_choice = st.selectbox("Bénéficiaire", bens, format_func=lambda x: x["email"])

        if st.button("Générer token (7 jours)"):
            try:
                sb.table("videos").update({"released": True}).eq("id", video_choice["id"]).execute()

                raw_token = secrets.token_urlsafe(32)
                token_hash = sha256(raw_token)
                expires = now_utc() + timedelta(days=7)

                sb.table("access_tokens").insert({
                    "video_id": video_choice["id"],
                    "beneficiary_email": ben_choice["email"],
                    "token_hash": token_hash,
                    "expires_at": expires.isoformat()
                }).execute()

                st.success("Token à transmettre:")
                st.code(raw_token)

            except Exception as e:
                st.error(f"Erreur token: {e}")
    else:
        st.info("Il faut au moins 1 vidéo et 1 bénéficiaire.")

# ---------------------------
# 4) Beneficiary access
# ---------------------------
with tab3:
    st.subheader("Accès bénéficiaire")
    token = st.text_input("Coller le token reçu", key="access_token")

    if st.button("Accéder", disabled=(not token)):
        try:
            token_hash = sha256(token)
            res = sb.table("access_tokens").select("*").eq("token_hash", token_hash).execute().data
            if not res:
                st.error("Token invalide.")
                st.stop()

            t = res[0]
            exp = datetime.fromisoformat(t["expires_at"].replace("Z", "+00:00"))
            if now_utc() > exp:
                st.error("Token expiré.")
                st.stop()

            v = sb.table("videos").select("*").eq("id", t["video_id"]).execute().data[0]
            if not v["released"]:
                st.error("Vidéo non libérée.")
                st.stop()

            bucket = sb.storage.from_("video-wills")
            signed = bucket.create_signed_url(v["storage_path"], 3600)
            video_url = signed["signedURL"]

            st.success("Accès autorisé.")
            st.video(video_url)

        except Exception as e:
            st.error(f"Erreur: {e}")
