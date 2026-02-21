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
                st.error("Identifiants invalid
