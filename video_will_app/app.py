import streamlit as st
from pathlib import Path
from PIL import Image

# -------------------------------------------------
# CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="K",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo_kidan_vid.png"

# -------------------------------------------------
# LOGO
# -------------------------------------------------
def show_logo():
    if LOGO_PATH.exists():
        img = Image.open(LOGO_PATH)
        # ⚠️ PAS de use_container_width
        st.image(img, width=800)
    else:
        st.warning(f"Logo introuvable : {LOGO_PATH}")

# -------------------------------------------------
# NAVIGATION
# -------------------------------------------------
def go_to_page(page_name):
    try:
        st.switch_page(f"pages/{page_name}")
    except:
        st.info("Utilisez le menu à gauche pour naviguer.")

# -------------------------------------------------
# PAGE
# -------------------------------------------------

show_logo()

st.title("Kidan Vid")

st.write("Plateforme de transmission vidéo sécurisée.")
st.write("Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche"):
        go_to_page("Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé"):
        go_to_page("Creer_un_envoi_securise.py")

st.divider()

st.header("Connexion")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

colA, colB = st.columns(2)

with colA:
    if st.button("Continuer"):
        go_to_page("Connexion.py")

with colB:
    if st.button("Accès bénéficiaire"):
        go_to_page("Acces_beneficiaire.py")

st.caption("© Kidan Vid")
