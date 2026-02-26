import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Kidan Vid", layout="wide")

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidanvid.png"  # mets ton logo ici

# --- Style propre type site officiel ---
st.markdown("""
    <style>
        .logo-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .divider {
            margin-top: 10px;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
st.markdown('<div class="logo-container">', unsafe_allow_html=True)

if LOGO_PATH.exists():
    st.image(str(LOGO_PATH), width=240)  # taille élégante type site officiel
else:
    st.warning("Logo introuvable dans /assets/logo_kidanvid.png")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

# --- Texte d’introduction ---
st.title("Un message vidéo, transmis au bon moment.")
st.write(
    "Enregistrez un message destiné à vos proches, puis contrôlez précisément "
    "l’accès des bénéficiaires lorsque le décès est déclaré."
)

st.markdown("""
- Accès bénéficiaires par jeton temporaire sécurisé  
- Validation notariale  
- Journalisation et traçabilité  
""")

st.subheader("Commencer")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

col1, col2 = st.columns(2)

with col1:
    st.button("Continuer", use_container_width=True)

with col2:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")
