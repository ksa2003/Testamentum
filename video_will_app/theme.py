import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme() -> None:
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

    html, body {{
      color: #FFFFFF !important;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    .tm-card {{
      background: rgba(15,18,22,0.85);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    /* TITRES */
    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      color: #FFFFFF !important;
      text-shadow: 0 6px 26px rgba(0,0,0,0.85);
    }}

    .tm-h2 {{
      font-size: 22px;
      font-weight: 800;
      color: #FFFFFF !important;
      text-shadow: 0 4px 20px rgba(0,0,0,0.90);
    }}

    /* PARAGRAPHES */
    .tm-text {{
      font-size: 15px;
      color: #FFFFFF !important;
      font-weight: 500;
      text-shadow: 0 2px 16px rgba(0,0,0,0.90);
    }}

    /* 🔥 "Commencer" en blanc forcé */
    .tm-card h2,
    .tm-card h3 {{
      color: #FFFFFF !important;
      font-weight: 800 !important;
    }}

    /* 🔥 FOOTNOTE CLAIRE */
    .tm-footnote {{
      color: #FFFFFF !important;
      font-size: 14px;
      font-weight: 600;
      text-shadow: 0 2px 16px rgba(0,0,0,0.90);
    }}

    /* LABEL EMAIL */
    .stTextInput label {{
      color: #FFFFFF !important;
      font-weight: 600;
      text-shadow: 0 2px 10px rgba(0,0,0,0.85);
    }}

    /* INPUT */
    .stTextInput input {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.40) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder {{
      color: rgba(255,255,255,0.70) !important;
    }}

    .stTextInput input:focus {{
      border: 1px solid #FFFFFF !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.20) !important;
    }}

    /* BOUTONS */
    .stButton > button {{
      width: 100% !important;
      height: 56px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.35) !important;
      background: rgba(255,255,255,0.20) !important;
      color: #FFFFFF !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      box-shadow: 0 16px 40px rgba(0,0,0,0.55) !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.30) !important;
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
