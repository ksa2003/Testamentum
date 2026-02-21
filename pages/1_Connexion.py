import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Testamentum — Connexion", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
      .stApp { background: #0b0f14; }
      section.main > div { max-width: 720px; padding-top: 1.2rem; }
      .panel{
        background:#0b0f14; border:1px solid #2f3336; border-radius:16px;
        padding:16px; margin-bottom:12px;
      }
      h1,h2,h3,p,div,span,label { color:#fff !important; }
      .muted { color:#b6bcc2 !important; }
      .stTextInput input{
        background:#0f1419 !important; border:1px solid #2f3336 !important;
        color:#fff !important; border-radius:12px !important; padding:0.75rem 0.9rem !important;
      }
      .stButton button{
        background:#E50914 !important; color:#fff !important; border:none !important;
        border-radius:12px !important; font-weight:900 !important; padding:0.75rem 1.0rem !important;
        width:100%;
      }
      .btn-secondary .stButton button{
        background:transparent !important; border:1px solid #2f3336 !important; color:#fff !important;
      }
      #MainMenu {visibility:hidden;} footer{visibility:hidden;} header{visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.title("Connexion")
st.caption("Veuillez vous identifier pour accéder à votre coffre.")
st.markdown("</div>", unsafe_allow_html=True)

prefill = st.session_state.get("prefill_email", "")

tab_login, tab_signup = st.tabs(["Se connecter", "Créer un compte"])

with tab_login:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    email = st.text_input("Adresse e-mail", value=prefill, key="login_email")
    pwd = st.text_input("Mot de passe", type="password", key="login_pwd")

    if st.button("Se connecter"):
        try:
            auth = sb.auth.sign_in_with_password({"email": email, "password": pwd})
            st.session_state["user_id"] = auth.user.id
            st.session_state["user_email"] = auth.user.email
            st.success("Connexion réussie.")
            st.switch_page("pages/2_Tableau_de_bord.py")
        except Exception as e:
            st.error("Identifiants invalides ou compte non confirmé.")
            st.caption(str(e)[:200])
    st.markdown("</div>", unsafe_allow_html=True)

with tab_signup:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    email = st.text_input("Adresse e-mail", value=prefill, key="reg_email")
    pwd = st.text_input("Mot de passe", type="password", key="reg_pwd")

    if st.button("Créer mon compte"):
        try:
            sb.auth.sign_up({"email": email, "password": pwd})
            st.success("Compte créé. Veuillez vous connecter.")
        except Exception as e:
            st.error("Impossible de créer le compte.")
            st.caption(str(e)[:200])
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
if st.button("Retour à l’accueil"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)
