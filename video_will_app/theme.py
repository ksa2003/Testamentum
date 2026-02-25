from __future__ import annotations

from pathlib import Path
from typing import Any, Optional, Union

import streamlit as st

# Background image (kept as before)
BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

PathLike = Union[str, Path]


def _safe_path(p: Any) -> Optional[Path]:
    """Convert to Path when possible."""
    if p is None:
        return None
    try:
        return Path(str(p))
    except Exception:
        return None


def _find_existing_image(path: Any) -> Optional[Path]:
    """Resolve an image path robustly.

    Accepts absolute/relative paths. If missing, tries to locate the file in the
    local assets directory by its filename.
    """
    p = _safe_path(path)
    if p is None:
        return None

    # 1) Direct path
    if p.exists() and p.is_file():
        return p

    # 2) Relative to app folder (video_will_app)
    app_dir = Path(__file__).resolve().parent

    candidates = [
        app_dir / p,  # relative
        app_dir / "assets" / p.name,  # assets/<filename>
        app_dir / "Assets" / p.name,  # common alternative
    ]

    for c in candidates:
        if c.exists() and c.is_file():
            return c

    return None


def apply_theme(app_name: str = "Kidan Vid"):
    """Apply global UI theme.

    In Streamlit Cloud/multipage apps, set_page_config can throw if called twice
    or after another Streamlit command. We fail soft to avoid crashing.
    """
    try:
        st.set_page_config(
            page_title=app_name,
            layout="wide",
            initial_sidebar_state="expanded",
        )
    except Exception:
        pass

    css = f"""
    <style>
    .stApp {{
      background:
        linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.80)),
        url("{BG_URL}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2rem;
    }}

    .tm-card {{
      background: rgba(15,18,22,0.82);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 20px 80px rgba(0,0,0,0.7);
    }}

    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      background: linear-gradient(90deg,#F3EDE2,#E7DCC7,#F8F3EA);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin: 0;
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.85);
      margin-top: 6px;
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.70);
      margin-top: 3px;
    }}

    .tm-h2 {{
      font-size: 32px;
      font-weight: 800;
      margin-top: 18px;
      color: rgba(255,255,255,0.95);
    }}

    .tm-chip {{
      padding: 9px 16px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.20);
      background: rgba(255,255,255,0.10);
      color: rgba(255,255,255,0.92);
      font-weight: 700;
      font-size: 14px;
      margin-right: 8px;
      display: inline-block;
      line-height: 1;
    }}

    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.85) !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stButton > button {{
      height: 56px !important;
      border-radius: 999px !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      border: 1px solid rgba(255,255,255,0.22) !important;
      background: rgba(255,255,255,0.10) !important;
      color: #FFFFFF !important;
    }}

    button[kind="primary"] {{
      background: #E7DCC7 !important;
      color: #111 !important;
      border: none !important;
    }}

    img {{
      border-radius: 16px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def img(
    path: Any,
    caption: Optional[str] = None,
    use_container_width: bool = True,
    **kwargs: Any,
):
    """Safe image renderer to avoid crashing when an image is missing."""
    resolved = _find_existing_image(path)
    if resolved is None:
        label = getattr(path, "name", None) or str(path)
        st.warning(f"Image introuvable : {label}")
        return

    # Try modern API first
    try:
        st.image(
            str(resolved),
            caption=caption,
            use_container_width=use_container_width,
            **kwargs,
        )
        return
    except TypeError:
        # Fallback for older Streamlit versions
        try:
            st.image(str(resolved), caption=caption, use_column_width=True)
            return
        except Exception as e:
            st.warning(f"Impossible d'afficher l'image ({resolved.name}) : {e}")
    except Exception as e:
        st.warning(f"Impossible d'afficher l'image ({resolved.name}) : {e}")
