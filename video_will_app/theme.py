import streamlit as st
from pathlib import Path


def apply_theme(title: str = "Kidan Vid"):
    try:
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )
    except Exception:
        pass


def img(path, caption=None, use_container_width=True):
    p = Path(str(path))

    if not p.exists():
        st.warning(f"Image introuvable : {p}")
        return

    try:
        st.image(str(p), caption=caption, use_container_width=use_container_width)
    except TypeError:
        # Compatibilité anciennes versions Streamlit
        st.image(str(p), caption=caption, use_column_width=True)
