import streamlit as st
from pathlib import Path
import inspect

def show_image_if_exists(path: Path, *, caption: str | None = None, width: int | None = None, use_container_width: bool = False) -> bool:
    if not path.exists():
        st.warning(f"Image introuvable : {path.as_posix()}")
        return False

    # Signature de st.image pour compatibilité (Streamlit ancien / nouveau)
    sig = inspect.signature(st.image)
    params = sig.parameters

    kwargs = {}
    if caption is not None:
        kwargs["caption"] = caption

    # IMPORTANT:
    # - Certaines versions: use_container_width
    # - Anciennes versions: use_column_width
    # - Sinon: pas d'option de largeur auto
    if use_container_width:
        if "use_container_width" in params:
            kwargs["use_container_width"] = True
        elif "use_column_width" in params:
            kwargs["use_column_width"] = True
        # Ne PAS mettre width dans ce cas (ça peut faire TypeError sur certaines versions)
        st.image(str(path), **kwargs)
    else:
        if width is not None:
            kwargs["width"] = width
        st.image(str(path), **kwargs)

    return True
