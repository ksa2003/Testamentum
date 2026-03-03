import streamlit as st
from pathlib import Path
from PIL import Image

# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# -------------------------------------------------
# AFFICHAGE LOGO (propre et jamais coupé)
# -------------------------------------------------
def show_logo():
    if LOGO_PATH.exists():
        img = Image.open(LOGO_PATH)
        st.image(img, use_column_width=True)
    else:
        st.warning(f"Logo introuvable : {LOGO_PATH}")

# -------------------------------------------------
# NAVIGATION (si disponible)
# -------------------------------------------------
def go_to_page(page_name):
    try:
        st.switch_page(f"pages/{page_name}")
    except:
        st.info("Utilisez le menu à gauche pour naviguer.")

# -------------------------------------------------
# STYLE
# -------------------------------------------------
st.markdown("""
    <style>
    .block-container {
        max-width: 1000px;
        padding-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# CONTENU PRINCIPAL
# -------------------------------------------------

show_logo()

st.title("Kidan Vid")

st.write("Plateforme de transmission vidéo sécurisée.")
st.write("Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

# -------------------------------------------------
# BOUTONS PRINCIPAUX
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche"):
        go_to_page("Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé"):
        go_to_page("Creer_un_envoi_securise.py")

st.markdown("---")

# -------------------------------------------------
# POINTS FORTS
# -------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("**100% sécurisé**")

with c2:
    st.markdown("**Accès unique et contrôlé**")

with c3:
    st.markdown("**Programmation possible**")

with c4:
    st.markdown("**Accessible partout**")

st.markdown("---")

# -------------------------------------------------
# COMMENT CA MARCHE
# -------------------------------------------------
st.header("Comment ça marche ?")

st.markdown("**I. Vous téléchargez votre vidéo**")
st.write("Format sécurisé, cryptage immédiat.")

st.markdown("**II. Vous identifiez le destinataire**")
st.write("Email + téléphone + vérification d’identité.")

st.markdown("**III. Nous sécurisons l’accès**")
st.write("Code unique + double authentification (2FA).")

st.markdown("**IV. Le destinataire reçoit la vidéo**")
st.write("Accès personnel, protégé et traçable.")

st.markdown("---")

# -------------------------------------------------
# POURQUOI KIDAN VID
# -------------------------------------------------
st.header("Pourquoi Kidan Vid ?")

st.markdown("""
- Cryptage de bout en bout
- Vidéo non téléchargeable
- Accès limité dans le temps
- Traçabilité des ouvertures
- Visionnage unique possible
- Hébergement conforme RGPD
""")

st.markdown("---")

# -------------------------------------------------
# NOS OFFRES
# -------------------------------------------------
st.header("Nos offres")

st.markdown("""
- Abonnement mensuel
- Abonnement annuel
- Envoi unique premium
""")

st.markdown("---")

# -------------------------------------------------
# CONNEXION EN BAS (COMME AVANT)
# -------------------------------------------------
st.header("Connexion")

st.write("Accédez à votre espace sécurisé.")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

colA, colB = st.columns(2)

with colA:
    if st.button("Continuer"):
        go_to_page("Connexion.py")

with colB:
    if st.button("Accès bénéficiaire"):
        go_to_page("Acces_beneficiaire.py")

st.caption("© Kidan Vid")
