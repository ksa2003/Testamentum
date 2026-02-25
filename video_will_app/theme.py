from pathlib import Path
import streamlit as st


def apply_theme(title: str = "Kidan Vid"):
    try:
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )
    except Exception:
        pass


def img(path, caption=None):
    """
    Affiche une image sans jamais faire planter l'app.
    """
    try:
        p = Path(path)
        if p.exists():
            st.image(str(p), use_container_width=True)
        else:
            st.warning(f"Image introuvable : {p.name}")
    except Exception as e:
        st.warning(f"Erreur affichage image : {e}")
