# video_will_app/app.py
from __future__ import annotations

from pathlib import Path
import streamlit as st

from theme import apply_theme, img
from kidan_content import get_slide, ASSETS_DIR


# IMPORTANT : doit être appelé AVANT tout autre st.*
st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main() -> None:
    apply_theme("Kidan Vid", "Coffre numérique sécurisé pour transmission vidéo posthume")

    # Exemple : afficher la cover (slide 1)
    s1 = get_slide(1)
    if s1 and getattr(s1, "image_path", None):
        img(s1.image_path)

    st.markdown(
        """
**Un message vidéo, transmis au bon moment.**

Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.

- Accès bénéficiaires par jeton temporaire sécurisé  
- Validation notariale (selon le niveau choisi)  
- Journalisation des actions et traçabilité  
        """
    )

    # Debug utile (tu peux enlever après)
    with st.expander("Diagnostic (assets)"):
        st.write("ASSETS_DIR:", str(ASSETS_DIR))
        if Path(ASSETS_DIR).exists():
            st.write("Fichiers:", [p.name for p in Path(ASSETS_DIR).glob("*.png")])
        else:
            st.error("ASSETS_DIR n'existe pas dans ce déploiement.")


if __name__ == "__main__":
    main()
