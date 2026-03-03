# video_will_app/utils_media.py

from pathlib import Path
import streamlit as st
from PIL import Image


def show_image_safe(path: Path, caption: str | None = None, width: int | None = None) -> bool:
    """
    Affiche une image de manière compatible avec différentes versions de Streamlit.
    Retourne True si affichée, False sinon.
    """
    try:
        if not path.exists():
            return False

        img = Image.open(path)

        # Streamlit récent
        try:
            st.image(img, caption=caption, width=width, use_container_width=(width is None))
            return True
        except TypeError:
            # Streamlit ancien
            st.image(img, caption=caption, width=width, use_column_width=(width is None))
            return True

    except Exception:
        return False


def assets_dir_from_pages_file(pages_file: Path) -> Path:
    """
    pages/XXX.py -> remonte à video_will_app/ puis assets/
    """
    app_dir = pages_file.resolve().parents[1]  # .../video_will_app
    return app_dir / "assets"
