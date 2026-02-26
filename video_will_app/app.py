import streamlit as st
from pathlib import Path
import base64

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
    max-width: 1200px;
}
header {visibility: hidden;}
/* Logo responsive */
.kidan-logo-wrap{
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 0.2rem;
    margin-bottom: 0.8rem;
}
.kidan-logo{
    width: 100%;
    max-width: 1100px;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOGO GRAND FORMAT (compat old Streamlit)
# ==============================
BASE_DIR = Path(__file__).resolve().parent
logo_path = BASE_DIR / "assets" / "logo_kidan_vid.png"

if logo_path.exists():
    b64 = base64.b64encode(logo_path.read_bytes()).decode("utf-8")
    st.markdown(
        f"""
        <div class="kidan-logo-wrap">
            <img class="kidan-logo" src="data:image/png;base64,{b64}" alt="Kidan Vid Logo"/>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"Logo introuvable : {logo_path}")

st.markdown("<br>", unsafe_allow_html=True)

# ==============================
# TITRE PRINCIPAL
# ==============================
st.markdown("""
<h1 style='text-align:center; font-size:42px; margin-bottom: 0.4rem;'>
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
<div style='max-width:700px; margin:auto; font-size:16px; line-height: 1.8;'>
• Accès bénéficiaires par jeton temporaire sécurisé<br>
• Validation notariale<br>
• Journalisation et traçabilité<br>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==============================
# SECTION CONNEXION
# ==============================
st.subheader("Commencer")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

col1, col2 = st.columns(2)

with col1:
    st.button("Continuer")

with col2:
    st.button("Accès bénéficiaire")
