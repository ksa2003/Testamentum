from pathlib import Path
import streamlit as st


def apply_theme(title: str = "Kidan Vid"):
    # Ne jamais planter si set_page_config est déjà appelé ailleurs
    try:
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )
    except Exception:
        pass


def img(path, caption=None, **kwargs):
    """
    Affiche une image sans faire planter l'app.
    - Accepte tous les kwargs de st.image() (ex: use_container_width=True)
    """
    try:
        p = Path(path)
        if p.exists():
            st.image(str(p), caption=caption, **kwargs)
        else:
            st.warning(f"Image introuvable : {p.name}")
    except Exception as e:
        st.warning(f"Erreur affichage image : {e}")
