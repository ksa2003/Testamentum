# video_will_app/app.py

from pathlib import Path
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🎥",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# ---------------------------
# Image compatibilité Streamlit
# ---------------------------
def show_image(path):
    if not path.exists():
        st.warning("Logo introuvable dans /assets")
        return
    img = Image.open(path)
    try:
        st.image(img, use_container_width=True)
    except TypeError:
        st.image(img, use_column_width=True)

# ---------------------------
# STYLE
# ---------------------------
st.markdown("""
<style>
.block-container { padding-top: 1.5rem; }
.kv-title { font-size: 2.2rem; font-weight: 700; }
.kv-sub { font-size: 1.1rem; color: #555; }
.section { margin-top: 2.5rem; }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOGO
# ---------------------------
show_image(LOGO_PATH)

# ---------------------------
# HERO
# ---------------------------
st.markdown('<div class="kv-title">Kidan Vid</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="kv-sub">Plateforme de transmission vidéo sécurisée.</div>',
    unsafe_allow_html=True
)

st.write("""
Envoyez des vidéos personnelles en toute confidentialité.  
La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne,
accessible uniquement par elle, lorsque vous reposez en paix.
""")

col1, col2, col3, col4 = st.columns(4)
col1.write("100% sécurisé")
col2.write("Accès unique et contrôlé")
col3.write("Programmation possible")
col4.write("Accessible partout")

# ---------------------------
# COMMENT CA MARCHE
# ---------------------------
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.header("Comment ça marche ?")

st.markdown("""
**I. Vous téléchargez votre vidéo**  
Format sécurisé, cryptage immédiat.

**II. Vous identifiez le destinataire**  
Email + téléphone + vérification d’identité.

**III. Nous sécurisons l’accès**  
Code unique + double authentification (2FA).

**IV. Le destinataire reçoit la vidéo**  
Accès personnel, protégé et traçable.
""")

# ---------------------------
# POURQUOI
# ---------------------------
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.header("Pourquoi Kidan Vid ?")

st.markdown("""
- Cryptage de bout en bout  
- Vidéo non téléchargeable  
- Accès limité dans le temps  
- Traçabilité des ouvertures  
- Option visionnage unique  
- Hébergement conforme RGPD  
""")

# ---------------------------
# OFFRES
# ---------------------------
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.header("Nos offres")

st.markdown("""
- Abonnement mensuel  
- Abonnement annuel  
- Envoi unique premium  
""")

# =====================================================
# 🔐 CONNEXION EN BAS (comme avant)
# =====================================================
st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.divider()

st.header("Connexion")

st.write("Accédez à votre espace sécurisé.")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

colA, colB = st.columns(2)

with colA:
    if st.button("Continuer", use_container_width=True):
        st.switch_page("pages/Connexion.py")

with colB:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")

st.caption("© Kidan Vid")
