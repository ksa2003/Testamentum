import streamlit as st
from pathlib import Path


def apply_theme(title: str = "Kidan Vid"):
    # Evite les crash si déjà appelé ailleurs
    try:
        st.set_page_config(page_title=title, layout="wide")
    except Exception:
        pass


def img(path, caption=None, use_container_width=True):
    """
    Affiche une image en compatibilité Streamlit :
    - Streamlit récent : use_container_width
    - Streamlit ancien : use_column_width
    """
    p = Path(str(path))

    if not p.exists():
        st.warning(f"Image introuvable : {p}")
        return

    try:
        st.image(str(p), caption=caption, use_container_width=use_container_width)
    except TypeError:
        # Anciennes versions Streamlit
        st.image(str(p), caption=caption, use_column_width=True)
