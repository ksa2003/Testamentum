import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🎥",
    layout="wide"
)

# --- SUPPRESSION DU PADDING HAUT ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# --- AFFICHAGE LOGO EN GRAND FORMAT ---
logo_path = "assets/logo_kidan_vid.png"  # adapte si besoin

if os.path.exists(logo_path):
    st.image(logo_path, use_container_width=True)
else:
    st.warning("Logo introuvable dans assets/logo_kidan_vid.png")


# --- ESPACE ---
st.markdown("<br>", unsafe_allow_html=True)

# --- TITRE ---
st.markdown(
    """
    <h1 style='text-align: center;'>
        Un message vidéo, transmis au bon moment.
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align: center; font-size:18px;'>
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
- Accès bénéficiaires par jeton temporaire sécurisé  
- Validation notariale  
- Journalisation et traçabilité  
""")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECTION CONNEXION ---
st.subheader("Commencer")

email = st.text_input("Adresse e-mail")

col1, col2 = st.columns(2)

with col1:
    st.button("Continuer", use_container_width=True)

with col2:
    st.button("Accès bénéficiaire", use_container_width=True)
