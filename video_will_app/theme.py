import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"


def apply_theme():
    st.set_page_config(page_title="Kidan Vid", layout="centered")

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

    /* IMPORTANT: couleur du texte des bulles */
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


def img(path: str):
    """
    Helper compatible avec anciennes versions Streamlit.
    Certaines versions ne supportent pas use_container_width.
    """
    try:
        st.image(path, use_container_width=True)
    except TypeError:
        st.image(path, use_column_width=True)
