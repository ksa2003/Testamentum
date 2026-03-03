from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


def _st_image_compat(img, caption=None, width=None, use_container_width=False):
    """
    Compat Streamlit : certaines versions n'acceptent pas use_container_width.
    On tente use_container_width, puis fallback use_column_width.
    """
    try:
        if use_container_width:
            st.image(img, caption=caption, use_container_width=True)
        else:
            st.image(img, caption=caption, width=width)
    except TypeError:
        # Anciennes versions Streamlit : use_column_width
        if use_container_width:
            st.image(img, caption=caption, use_column_width=True)
        else:
            st.image(img, caption=caption, width=width)


def get_asset_path(filename: str) -> Path:
    return ASSETS_DIR / filename


def show_asset_image(
    filename: str,
    caption: str | None = None,
    width: int | None = None,
    use_container_width: bool = False,
):
    """
    Affiche une image depuis /assets.
    - width: fixe en pixels (si None, on peut utiliser la largeur de colonne)
    - use_container_width: True si on veut plein largeur (avec fallback)
    """
    p = get_asset_path(filename)
    if not p.exists():
        st.warning(f"Image introuvable : {p}")
        return

    try:
        img_bytes = p.read_bytes()
    except Exception:
        st.warning(f"Impossible de lire : {p}")
        return

    _st_image_compat(
        img_bytes,
        caption=caption,
        width=width,
        use_container_width=use_container_width,
    )
