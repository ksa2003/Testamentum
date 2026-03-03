import streamlit as st
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = APP_DIR / "assets"

def show_logo():
    logo = ASSETS_DIR / "logo_kidan_vid.png"
    if logo.exists():
        st.image(str(logo), use_container_width=True)
    else:
        st.warning(f"Logo introuvable : {logo.as_posix()}")

st.set_page_config(page_title="Notaire en ligne", layout="wide")

show_logo()

st.title("Lien pour succession (actes notariés)")
st.subheader("Pourquoi utiliser un notaire en ligne ?")

st.markdown(
    """
**Commodité**  
Les signataires peuvent obtenir leurs documents notariés à distance via un appareil mobile ou une webcam.

**Vitesse**  
La séance moyenne de notarisation en ligne prend généralement 5 à 15 minutes.

**Sécurité**  
Les documents peuvent être scellés numériquement pour se protéger contre la fraude et l'altération.

**Facilité d'utilisation**  
Cliquez sur un lien pour rejoindre la session avec votre smartphone ou votre navigateur d'ordinateur.
"""
)

st.markdown("---")
st.info("Important : la notarisation en ligne dépend du cadre légal de chaque pays / État. Une page de conformité par juridiction sera nécessaire.")
