import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Testamentum — Connexion", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}

      :root{
        --bg:#000000;
        --surface:#0b0f14;
        --border:#2f3336;
        --text:#e7e9ea;
        --muted:#71767b;
        --accent:#1d9bf0; /* bleu X */
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{ max-width: 720px; padding-top: 1.2rem; }

      .panel{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 12px;
      }

      h1,h2,h3,p,div,span,label{ color: var(--text) !important; }
      .muted{ color: var(--muted) !important; }

      .stTextInput input{
        background: #0f1419 !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;       /* IMPORTANT */
        caret-color: var(--text) !important; /* IMPORTANT */
        border-radius: 14px !important;
        padding: 0.9rem 1rem !important;
      }
      .stTextInput input::placeholder{ color: var(--muted) !important; }
      .stTextInput label{ color: var(--muted) !important; font-weight: 700 !important; }

      /* Boutons */
      .stButton button{
        background: var(--accent) !important;
        color: #001018 !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 900 !important;
        padding: 0.9rem 1rem !important;
        width: 100%;
      }
      .stButton button:hover{ filter: brightness(1.05); }

      .btn-secondary .stButton button{
        background: transparent !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
      }

      /* Tabs */
      button[data-baseweb="tab"]{
        color: var(--muted) !important;
      }
      button[data-baseweb="tab"][aria-selected="true"]{
        color: var(--text) !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

prefill = st.session_state.get("prefill_email", "")

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.title("Connexion")
st.caption("Veuillez vous identifier pour accéder à votre coffre.")
st.markdown("</div>", unsafe_allow_html=True)

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
        except Exception:
            st.error("Identifiants invalides ou compte non confirmé.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab_signup:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    email = st.text_input("Adresse e-mail", value=prefill, key="reg_email")
    pwd = st.text_input("Mot de passe", type="password", key="reg_pwd")

    if st.button("Créer mon compte"):
        try:
            sb.auth.sign_up({"email": email, "password": pwd})
            st.success("Compte créé. Veuillez vous connecter.")
        except Exception:
            st.error("Impossible de créer le compte.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
if st.button("Retour à l’accueil"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)
