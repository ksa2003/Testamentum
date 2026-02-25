import streamlit as st
import inspect
from pathlib import Path


# -------------------------------------------------------
# Safe page config + clean theme
# -------------------------------------------------------
def apply_theme(title: str = "Kidan Vid"):
    """
    Applique la configuration de page en toute sécurité.
    - title est optionnel (évite TypeError si une page appelle apply_theme() sans argument)
    """
    try:
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="collapsed",
        )
    except Exception:
        # Si déjà appelé ailleurs, on ignore
        pass

    st.markdown(
        """
        <style>
        /* Cache la navigation automatique des pages Streamlit */
        [data-testid="stSidebarNav"] { display: none; }
        [data-testid="stSidebarNavSeparator"] { display: none; }

        /* Fond général */
        .main { background-color: #f8f8f8; }

        h1, h2, h3 { color: #1f2c44; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# Ultra-safe image loader (anti-TypeError Streamlit)
# -------------------------------------------------------
def img(path, caption=None, use_container_width=True):
    """
    Affiche une image compatible avec toutes les versions Streamlit.

    - Versions récentes : use_container_width
    - Anciennes versions : use_column_width
    """
    p = Path(path)

    if not p.exists():
        st.warning(f"Image introuvable : {p.name}")
        return

    params = inspect.signature(st.image).parameters

    if "use_container_width" in params:
        st.image(str(p), caption=caption, use_container_width=use_container_width)
    elif "use_column_width" in params:
        st.image(str(p), caption=caption, use_column_width=use_container_width)
    else:
        st.image(str(p), caption=caption)
