import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"


def show_logo(path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return

    try:
        img = Image.open(path)
        st.image(img, width=1100)
    except Exception as e:
        st.error(f"Impossible de charger le logo : {e}")


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


show_logo(LOGO_PATH)

st.title("Kidan Vid")

st.write(
    """
Plateforme de transmission vidéo, audio et documentaire sécurisée.

Envoyez des messages personnels en toute confidentialité.
Vidéos, audios, documents et accès bénéficiaire sont organisés
dans une logique humaine, technique et juridique.
"""
)

st.warning(
    """
Point juridique important

En France, une vidéo seule ne constitue pas un testament juridiquement valable.
Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
"""
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche"):
        go_to_page("Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé"):
        go_to_page("Creer_un_envoi_securise.py")

st.markdown("---")

st.subheader("Les 4 piliers")

c1, c2 = st.columns(2)

with c1:
    st.write("Vidéo")
    st.write("Messages vidéo personnels programmés.")
    st.write("Audio")
    st.write("Souvenirs vocaux et témoignages.")

with c2:
    st.write("Sécurisation")
    st.write("Chiffrement et contrôle d'accès.")
    st.write("Notaires")
    st.write("Pilier juridique central.")

st.markdown("---")

st.subheader("Témoignage")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.markdown("---")
st.subheader("Accès rapides")

q1, q2, q3, q4 = st.columns(4)
with q1:
    if st.button("Qui sommes-nous"):
        go_to_page("Qui_sommes_nous.py")
with q2:
    if st.button("Nous contacter"):
        go_to_page("Nous_contacter.py")
with q3:
    if st.button("Informations légales"):
        go_to_page("Informations_legales.py")
with q4:
    if st.button("Mentions légales"):
        go_to_page("Mentions_legales.py")

st.markdown("---")
st.subheader("Connexion")
st.write("Accédez à votre espace sécurisé.")

st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer", key="btn_continue_home"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire", key="btn_benef_home"):
        go_to_page("Acces_beneficiaire.py")

st.markdown("---")
st.caption("© Kidan Vid")
