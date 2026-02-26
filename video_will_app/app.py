import streamlit as st
from pathlib import Path

# ==============================
# CONFIG PAGE
# ==============================

st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🎥",
    layout="wide"
)

# ==============================
# STYLE (réduction marge haute)
# ==============================

st.markdown("""
<style>
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 2rem;
}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOGO GRAND FORMAT
# ==============================

BASE_DIR = Path(__file__).resolve().parent
logo_path = BASE_DIR / "assets" / "logo_kidan_vid.png"

if logo_path.exists():
    st.image(str(logo_path), use_container_width=True)
else:
    st.warning(f"Logo introuvable : {logo_path}")

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# TITRE PRINCIPAL
# ==============================

st.markdown("""
<h1 style='text-align:center; font-size:42px;'>
Un message vidéo, transmis au bon moment.
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px; max-width:900px; margin:auto;'>
Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# LISTE AVANTAGES
# ==============================

st.markdown("""
<div style='max-width:700px; margin:auto; font-size:16px;'>

• Accès bénéficiaires par jeton temporaire sécurisé  
• Validation notariale  
• Journalisation et traçabilité  

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==============================
# SECTION CONNEXION
# ==============================

st.subheader("Commencer")

email = st.text_input("Adresse e-mail")

col1, col2 = st.columns(2)

with col1:
    st.button("Continuer", use_container_width=True)

with col2:
    st.button("Accès bénéficiaire", use_container_width=True)
