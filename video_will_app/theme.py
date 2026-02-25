# video_will_app/theme.py
from __future__ import annotations

from pathlib import Path
import streamlit as st


def apply_theme(title: str = "Kidan Vid", subtitle: str | None = None) -> None:
    """
    Thème SAFE : ne casse pas la sidebar Streamlit, ne masque pas la navigation des pages.
    """
    # IMPORTANT : ne jamais cacher stSidebar/stSidebarNav dans le CSS
    st.markdown(
        """
        <style>
        /* Layout général */
        .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

        /* Petits ajustements esthétiques (sans toucher la navigation) */
        h1, h2, h3 { letter-spacing: 0.2px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if title:
        st.title(title)
    if subtitle:
        st.caption(subtitle)


def img(
    p: str | Path,
    caption: str | None = None,
    use_container_width: bool = True,
) -> None:
    """
    Affiche une image sans planter si elle manque.
    """
    path = Path(str(p))
    if not path.exists():
        st.warning(f"Image introuvable : {path}")
        return

    st.image(str(path), caption=caption, use_container_width=use_container_width)
