import streamlit as st
from supabase import create_client
import uuid
from datetime import datetime, timedelta

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
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
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
      }

      .stTextInput input {
        border-radius: 12px !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Testamentum")
st.caption("Coffre vidéo sécurisé — Accès contrôlé pour les bénéficiaires")

# ---------------------------------------------------
# Connexion Supabase
# ---------------------------------------------------

sb = create_client(
    st.secrets["supabase"]["url"],
    st.secrets["supabase"]["key"]
)

# ---------------------------------------------------
# Fonctions
# ---------------------------------------------------

def get_or_create_vault(owner_user_id):
    existing = sb.table("vaults").select("*").eq("owner_user_id", owner_user_id).execute()
    if existing.data:
        return existing.data[0]

    created = sb.table("vaults").insert({
        "owner_user_id": owner_user_id,
        "title": "Coffre principal"
    }).execute()

    return created.data[0]


def generate_token(vault_id):
    token = str(uuid.uuid4())
    expires = (datetime.utcnow() + timedelta(days=7)).isoformat()

    sb.table("access_tokens").insert({
        "vault_id": vault_id,
        "token": token,
        "expires_at": expires
    }).execute()

    return token


# ---------------------------------------------------
# Authentification
# ---------------------------------------------------

if "user_id" not in st.session_state:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Créer un compte")
        email_reg = st.text_input("Adresse email", key="reg_email")
        password_reg = st.text_input("Mot de passe", type="password", key="reg_pass")

        if st.button("Créer mon compte"):
            try:
                sb.auth.sign_up({
                    "email": email_reg,
                    "password": password_reg
                })
                st.success("Compte créé avec succès. Vous pouvez maintenant vous connecter.")
            except Exception:
                st.error("Une erreur est survenue lors de la création du compte.")

    with col2:
        st.subheader("Connexion")
        email = st.text_input("Adresse email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")

        if st.button("Se connecter"):
            try:
                response = sb.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })
                st.session_state["user_id"] = response.user.id
                st.session_state["user_email"] = response.user.email
                st.rerun()
            except Exception:
                st.error("Identifiants invalides.")

    st.stop()

# ---------------------------------------------------
# Utilisateur connecté
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
# Interface principale
# ---------------------------------------------------

tab1, tab2, tab3 = st.tabs([
    "Téléversement",
    "Bénéficiaires",
    "Accès par jeton"
])

# ---------------------------------------------------
# Téléversement vidéo
# ---------------------------------------------------

with tab1:
    st.subheader("Téléverser une vidéo testamentaire")

    uploaded = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "avi"])

    if uploaded:
        file_name = f"{uuid.uuid4()}_{uploaded.name}"

        sb.storage.from_("videos").upload(file_name, uploaded.getvalue())

        sb.table("videos").insert({
            "vault_id": vault["id"],
            "file_path": file_name
        }).execute()

        st.success("Vidéo téléversée avec succès.")

# ---------------------------------------------------
# Gestion bénéficiaires
# ---------------------------------------------------

with tab2:
    st.subheader("Ajouter un bénéficiaire")

    beneficiary_email = st.text_input("Adresse email du bénéficiaire")

    if st.button("Générer un jeton d’accès"):
        token = generate_token(vault["id"])
        st.success("Jeton généré avec succès.")
        st.info(f"Jeton à transmettre au bénéficiaire : {token}")

# ---------------------------------------------------
# Accès par jeton
# ---------------------------------------------------

with tab3:
    st.subheader("Accès bénéficiaire")

    input_token = st.text_input("Veuillez coller le jeton reçu")

    if st.button("Accéder"):
        result = sb.table("access_tokens").select("*").eq("token", input_token).execute()

        if result.data:
            record = result.data[0]
            expiry = datetime.fromisoformat(record["expires_at"])

            if datetime.utcnow() > expiry:
                st.error("Ce jeton a expiré.")
            else:
                videos = sb.table("videos").select("*").eq("vault_id", record["vault_id"]).execute()

                if videos.data:
                    file_path = videos.data[0]["file_path"]
                    signed_url = sb.storage.from_("videos").create_signed_url(file_path, 3600)
                    st.video(signed_url["signedURL"])
                else:
                    st.warning("Aucune vidéo disponible.")
        else:
            st.error("Jeton invalide.")        except Exception as e:
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


