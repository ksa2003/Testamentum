# video_will_app/pages/Notaire_en_ligne.py

from pathlib import Path
import streamlit as st

from utils_media import show_image_safe, assets_dir_from_pages_file


st.set_page_config(page_title="Notaire en ligne", layout="wide")

ASSETS_DIR = assets_dir_from_pages_file(Path(__file__))
LOGO = ASSETS_DIR / "logo_kidan_vid.png"


def show_logo():
    ok = show_image_safe(LOGO)
    if not ok:
        st.warning("Logo introuvable : assets/logo_kidan_vid.png")


show_logo()

st.title("Notaire en ligne")
st.write(
    "Accédez à des informations et bonnes pratiques autour de la notarisation à distance, "
    "dans une approche globale."
)

st.header("Pourquoi utiliser un notaire en ligne ?")

st.subheader("Commodité")
st.write(
    "Obtenir des documents notariés à distance, via un appareil mobile ou une webcam, "
    "sans déplacement."
)

st.subheader("Vitesse")
st.write("Une séance moyenne peut prendre 5 à 10 minutes.")

st.subheader("Sécurité")
st.write(
    "Les documents peuvent être scellés numériquement pour limiter les risques de fraude "
    "et d'altération."
)

st.subheader("Facilité d'utilisation")
st.write(
    "Vous rejoignez une session via un lien, depuis un smartphone ou un navigateur d'ordinateur."
)

st.divider()

st.header("Questions fréquentes")

with st.expander("De quoi ai-je besoin pour une séance de notaire en ligne ?"):
    st.write(
        "- Un ordinateur ou smartphone avec navigateur et caméra\n"
        "- Une pièce d'identité valide\n"
        "- Les documents au format PDF"
    )

with st.expander("Est-ce que je reçois une copie papier avec signature manuscrite ?"):
    st.write(
        "Généralement, vous recevez un document signé et scellé numériquement (PDF). "
        "Les copies papier avec signature manuscrite ne sont pas toujours disponibles."
    )

with st.expander("Dois-je être dans le même pays/état que le notaire ?"):
    st.write(
        "Cela dépend des règles locales et du cadre juridique applicable. "
        "Le point clé est la conformité avec la réglementation du pays/état du notaire."
    )

st.divider()

st.header("Formulaires et modèles")
st.write("Section à compléter : modèles de documents, formulaires, guides, etc.")
