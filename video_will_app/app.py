import streamlit as st
from supabase import create_client
import uuid
import hashlib
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Testamentum",
    page_icon="🔐",
    layout="centered"
)

# ---------------------------------------------------
# Branding / UI professionnel
# ---------------------------------------------------

st.markdown(
    """
    <style>
      .stApp {
        background: radial-gradient(1200px circle at 10% 10%, rgba(66,133,244,0.12), transparent 40%),
                    radial-gradient(900px circle at 90% 20%, rgba(0,200,150,0.10), transparent 35%),
                    radial-gradient(900px circle at 50% 90%, rgba(155,81,224,0.10), transparent 35%),
                    linear-gradient(180deg, #0b1220 0%, #0a0f1a 100%);
      }

      html, body, [class*="css"]  {
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Noto Sans", "Liberation Sans", sans-serif;
      }

      section.main > div {
        max-width: 900px;
        padding-top: 2rem;
      }

      .block-container {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
      }

      .stButton button {
        border-radius: 12px;
        padding: 0.6rem 1rem;
        border: 1px solid rgba(255,255,255,0.10);
      }

      .stTextInput input, .stTextArea textarea {
        border-radius: 12px !important;
      }

      button[role="tab"] {
        border-radius: 12px !important;
      }

      .stAlert {
        border-radius: 14px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Testamentum")
st.caption("Coffre vidéo sécurisé — Accès contrôlé par jeton pour les bénéficiaires")

# ---------------------------------------------------
# Connexion Supabase
# ---------------------------------------------------

sb = create_client(
    st.secrets["supabase"]["url"],
    st.secrets["supabase"]["key"]
)

# ---------------------------------------------------
# Helpers
# ---------------------------------------------------

def now_utc():
    return datetime.now(timezone.utc)

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ---------------------------------------------------
# DB Fonctions
# ---------------------------------------------------

def get_or_create_vault(owner_user_id: str):
    res = sb.table("vaults").select("*").eq("owner_user_id", owner_user_id).execute()
    if res.data:
        return res.data[0]
    created = sb.table("vaults").insert({
        "owner_user_id": owner_user_id,
        "title": "Coffre principal"
    }).execute()
    return created.data[0]

def create_access_token(video_id: str, beneficiary_email: str, days_valid: int = 7) -> str:
    raw = uuid.uuid4().hex + uuid.uuid4().hex  # token lisible + long
    token_hash = sha256(raw)
    expires = now_utc() + timedelta(days=days_valid)

    sb.table("access_tokens").insert({
        "video_id": video_id,
        "beneficiary_email": beneficiary_email,
        "token_hash": token_hash,
        "expires_at": expires.isoformat()
    }).execute()

    return raw

def verify_access_token(raw_token: str):
    token_hash = sha256(raw_token)
    rows = sb.table("access_tokens").select("*").eq("token_hash", token_hash).execute().data
    if not rows:
        return None, "invalid"

    t = rows[0]
    exp = datetime.fromisoformat(t["expires_at"].replace("Z", "+00:00"))
    if now_utc() > exp:
        return None, "expired"

    v_rows = sb.table("videos").select("*").eq("id", t["video_id"]).execute().data
    if not v_rows:
        return None, "video_not_found"

    return v_rows[0], "ok"

# ---------------------------------------------------
# Auth (Supabase Auth)
# ---------------------------------------------------

if "user_id" not in st.session_state:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Créer un compte")
        email_reg = st.text_input("Adresse email", key="reg_email")
        password_reg = st.text_input("Mot de passe", type="password", key="reg_pass")
        if st.button("Créer mon compte"):
            try:
                sb.auth.sign_up({"email": email_reg, "password": password_reg})
                st.success("Compte créé avec succès. Vous pouvez maintenant vous connecter.")
            except Exception as e:
                st.error("Une erreur est survenue lors de la création du compte.")
                st.caption(str(e)[:200])

    with col2:
        st.subheader("Connexion")
        email = st.text_input("Adresse email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")
        if st.button("Se connecter"):
            try:
                auth = sb.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state["user_id"] = auth.user.id
                st.session_state["user_email"] = auth.user.email
                st.rerun()
            except Exception as e:
                st.error("Identifiants invalides ou compte non confirmé.")
                st.caption(str(e)[:200])

    st.stop()

# ---------------------------------------------------
# Utilisateur connecté + Déconnexion
# ---------------------------------------------------

st.success("Connexion réussie.")
st.sidebar.write(f"Connecté : {st.session_state['user_email']}")

if st.sidebar.button("Se déconnecter"):
    try:
        sb.auth.sign_out()
    except Exception:
        pass
    st.session_state.clear()
    st.rerun()

user_id = st.session_state["user_id"]
vault = get_or_create_vault(user_id)

# ---------------------------------------------------
# UI - Tabs
# ---------------------------------------------------

tab1, tab2, tab3 = st.tabs(["Téléversement", "Bénéficiaires", "Accès par jeton"])

# ---------------------------------------------------
# Tab 1 - Upload vidéo
# ---------------------------------------------------

with tab1:
    st.subheader("Téléverser une vidéo")
    title = st.text_input("Titre", value="Mon message", key="vid_title")
    file = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "m4v", "webm"])

    if st.button("Téléverser", disabled=(file is None)):
        try:
            object_key = f"{vault['id']}/{uuid.uuid4().hex}_{file.name}"
            bucket = sb.storage.from_("video-wills")
            bucket.upload(object_key, file.getvalue(), {"content-type": file.type or "video/mp4"})

            sb.table("videos").insert({
                "vault_id": vault["id"],
                "title": title,
                "storage_path": object_key,
                "released": False
            }).execute()

            st.success("Vidéo téléversée avec succès.")
        except Exception as e:
            st.error("Impossible de téléverser la vidéo.")
            st.caption(str(e)[:200])

    st.markdown("### Vos vidéos")
    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if not vids:
        st.info("Aucune vidéo pour l’instant.")
    else:
        for v in vids:
            st.write(f"- {v.get('title','(sans titre)')} | libérée={v.get('released')} | id={v.get('id')}")

# ---------------------------------------------------
# Tab 2 - Bénéficiaires + génération de jeton
# ---------------------------------------------------

with tab2:
    st.subheader("Bénéficiaires")
    ben_email = st.text_input("Adresse email du bénéficiaire", key="ben_email")

    if st.button("Ajouter un bénéficiaire", disabled=(not ben_email)):
        try:
            sb.table("beneficiaries").insert({"vault_id": vault["id"], "email": ben_email}).execute()
            st.success("Bénéficiaire ajouté.")
        except Exception as e:
            st.error("Impossible d’ajouter ce bénéficiaire (déjà présent ou erreur).")
            st.caption(str(e)[:200])

    bens = sb.table("beneficiaries").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if bens:
        st.markdown("### Liste des bénéficiaires")
        for b in bens:
            st.write(f"- {b['email']}")
    else:
        st.info("Aucun bénéficiaire pour l’instant.")

    st.markdown("---")
    st.subheader("Générer un jeton d’accès (MVP manuel)")

    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if not vids or not bens:
        st.info("Veuillez d’abord ajouter au moins une vidéo et un bénéficiaire.")
    else:
        video_choice = st.selectbox("Sélectionner une vidéo", vids, format_func=lambda x: f"{x.get('title','(sans titre)')} ({x['id']})")
        ben_choice = st.selectbox("Sélectionner un bénéficiaire", bens, format_func=lambda x: x["email"])

        if st.button("Générer le jeton (7 jours)"):
            try:
                # Marquer la vidéo comme libérée (MVP)
                sb.table("videos").update({"released": True, "released_at": now_utc().isoformat()}).eq("id", video_choice["id"]).execute()

                token = create_access_token(video_choice["id"], ben_choice["email"], days_valid=7)
                st.success("Jeton généré. Veuillez le transmettre au bénéficiaire :")
                st.code(token)
            except Exception as e:
                st.error("Impossible de générer le jeton.")
                st.caption(str(e)[:200])

# ---------------------------------------------------
# Tab 3 - Accès par jeton
# ---------------------------------------------------

with tab3:
    st.subheader("Accès bénéficiaire")
    raw_token = st.text_input("Veuillez coller le jeton reçu", key="access_token")

    if st.button("Accéder", disabled=(not raw_token)):
        try:
            video, status = verify_access_token(raw_token)

            if status == "invalid":
                st.error("Jeton invalide.")
            elif status == "expired":
                st.error("Jeton expiré.")
            elif status != "ok":
                st.error("Impossible de retrouver la vidéo.")
            else:
                if not video.get("released"):
                    st.error("Contenu non libéré.")
                else:
                    bucket = sb.storage.from_("video-wills")
                    signed = bucket.create_signed_url(video["storage_path"], 3600)
                    st.success("Accès autorisé. Lecture en cours.")
                    st.video(signed["signedURL"])

        except Exception as e:
            st.error("Erreur lors de l’accès.")
            st.caption(str(e)[:200])
