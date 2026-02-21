import streamlit as st
from supabase import create_client

st.set_page_config(page_title="Testamentum — Connexion", page_icon="🔐", layout="centered")

st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}
      [data-testid="stSidebar"] {display:none;}

      :root{
        --bg:#f3f2ef;
        --card:#ffffff;
        --text:#191919;
        --muted:#5f6368;
        --border:#e0e0e0;
        --blue:#0a66c2;
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{ max-width: 640px !important; padding-top: 1.2rem !important; }

      .card{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
      }

      .title{ font-weight: 900; font-size: 1.6rem; color: var(--text); margin: 0 0 6px 0; }
      .lead{ color: var(--muted); margin: 0 0 10px 0; line-height: 1.5; }

      .stTextInput input{
        background: #fff !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        border-radius: 10px !important;
        padding: 0.85rem 0.9rem !important;
      }
      .stTextInput label{ color: var(--muted) !important; font-weight: 700 !important; }

      .stButton button{
        background: var(--blue) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.85rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }

      .btn-secondary .stButton button{
        background: transparent !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])
prefill = st.session_state.get("prefill_email", "")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="title">Connexion</div>', unsafe_allow_html=True)
st.markdown('<div class="lead">Veuillez vous identifier pour accéder à votre coffre.</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

tab_login, tab_signup = st.tabs(["Se connecter", "Créer un compte"])

with tab_login:
    st.markdown('<div class="card">', unsafe_allow_html=True)
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
    st.markdown('<div class="card">', unsafe_allow_html=True)
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
