import streamlit as st

st.set_page_config(page_title="Testamentum — Tableau de bord", page_icon="📁", layout="wide")

# --- Guard: si pas connecté, retour connexion
if "user_id" not in st.session_state:
    st.switch_page("pages/1_Connexion.py")

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
      section.main > div{ max-width: 1100px !important; padding-top: 1.2rem !important; }

      .card{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
      }

      .title{ font-weight: 900; font-size: 1.7rem; color: var(--text); margin: 0; }
      .sub{ color: var(--muted); margin-top: 4px; }

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

# Header
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="title">Tableau de bord</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub">Connecté : {st.session_state.get("user_email","")}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Déconnexion (sans rouge)
col1, col2 = st.columns([0.25, 0.75])
with col1:
    if st.button("Se déconnecter"):
        st.session_state.clear()
        st.switch_page("app.py")

# Tabs
tab_upload, tab_benef = st.tabs(["Téléverser", "Bénéficiaires & jetons"])

with tab_upload:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Téléverser une vidéo")
    title = st.text_input("Titre", value="Mon message")
    video = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "m4v", "webm"])
    if st.button("Téléverser"):
        st.info("MVP : branchez ici votre logique Supabase Storage (upload) + insertion DB.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Vos vidéos")
    st.info("Aucune vidéo pour l’instant.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab_benef:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Bénéficiaires & jetons")
    st.info("MVP : branchez ici votre création de jetons / liste / expiration.")
    st.markdown("</div>", unsafe_allow_html=True)
