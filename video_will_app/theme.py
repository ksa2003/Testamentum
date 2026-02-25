import streamlit as st
from pathlib import Path


# -------------------------------------------------------
# Safe theme function (Streamlit Cloud compatible)
# -------------------------------------------------------
def apply_theme(title: str):
    # IMPORTANT : set_page_config doit être appelé UNE SEULE FOIS
    # et en tout début d'exécution.
    try:
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )
    except:
        # Si déjà appelé ailleurs, on ignore
        pass

    # CSS léger, sans risque
    st.markdown(
        """
        <style>
        .main {
            background-color: #f8f8f8;
        }
        h1, h2, h3 {
            color: #1f2c44;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# Safe image loader
# -------------------------------------------------------
def img(path: str, caption=None, use_container_width=True):
    p = Path(path)

    if p.exists():
        st.image(str(p), caption=caption, use_container_width=use_container_width)
    else:
        st.warning(f"Image introuvable : {p.name}")
