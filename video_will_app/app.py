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
    if path.exists():
        img = Image.open(path)
        st.image(img, use_container_width=True)


# logo pleine largeur
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
        st.switch_page("pages/Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé"):
        st.switch_page("pages/Creer_un_envoi_securise.py")


st.markdown("---")

st.subheader("Les 4 piliers")

c1, c2 = st.columns(2)

with c1:
    st.write("🎥 Vidéo")
    st.write("Messages vidéo personnels programmés.")

    st.write("🎙 Audio")
    st.write("Souvenirs vocaux et témoignages.")

with c2:
    st.write("🛡 Sécurisation")
    st.write("Chiffrement et contrôle d'accès.")

    st.write("⚖ Notaires")
    st.write("Pilier juridique central.")

st.markdown("---")

st.subheader("Témoignage")

st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")
