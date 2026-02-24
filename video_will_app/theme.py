import streamlit as st
import base64
from pathlib import Path


def get_base64_image(path):
    img_bytes = Path(path).read_bytes()
    return base64.b64encode(img_bytes).decode()


def apply_theme():
    bg_path = "video_will_app/assets/kidan_bg.jpg"

    try:
        bg_base64 = get_base64_image(bg_path)
        background = f"url('data:image/jpeg;base64,{bg_base64}')"
    except Exception:
        background = "linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85))"

    css = f"""
    <style>
    .stApp {{
        background:
            linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.85)),
            {background};
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    html, body {{
        color: rgba(255,255,255,0.92);
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    .tm-card {{
        background: rgba(15,18,22,0.85);
        border-radius: 20px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 20px 80px rgba(0,0,0,0.7);
    }}

    .tm-title {{
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(90deg,#F5F1E6,#C6A15B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .tm-sub {{
        font-size: 15px;
        color: rgba(255,255,255,0.85);
    }}

    .tm-chip {{
        padding: 8px 18px;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.18);
        background: rgba(255,255,255,0.08);
        color: white;
        font-size: 13px;
        font-weight: 600;
        margin-right: 8px;
    }}

    .stButton > button {{
        height: 56px !important;
        border-radius: 999px !important;
        white-space: nowrap !important;
        font-weight: 600;
        font-size: 15px;
    }}

    .tm-primary .stButton > button {{
        background: #E5E7EB !important;
        color: black !important;
        border: none !important;
    }}

    img.tm-image {{
        border-radius: 20px;
        margin-top: 10px;
        box-shadow: 0 15px 60px rgba(0,0,0,0.6);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
