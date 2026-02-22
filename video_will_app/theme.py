import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme() -> None:
    css = f"""
    <style>
    .stApp {{
      background:
        linear-gradient(rgba(0,0,0,0.60), rgba(0,0,0,0.78)),
        url("{BG_URL}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}

    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: #FFFFFF;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    .tm-card {{
      background: rgba(12,15,20,0.86);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    /* TITRE PRINCIPAL */
    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: #FFFFFF;
      text-shadow: 0 6px 26px rgba(0,0,0,0.75);
    }}

    /* SOUS TITRE */
    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.95);
      text-shadow: 0 2px 14px rgba(0,0,0,0.75);
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.85);
      text-shadow: 0 2px 14px rgba(0,0,0,0.75);
    }}

    /* 🔥 CORRECTION ICI */
    /* COMMENCER */
    .tm-h2 {{
      font-size: 22px;
      font-weight: 800;
      color: #FFFFFF !important;
      text-shadow: 0 4px 18px rgba(0,0,0,0.85);
    }}

    /* PARAGRAPHES */
    .tm-text {{
      font-size: 15px;
      line-height: 1.6;
      color: rgba(255,255,255,0.96) !important;
      text-shadow: 0 2px 14px rgba(0,0,0,0.80);
    }}

    /* 🔥 CORRECTION "En continuant..." */
    .tm-footnote {{
      font-size: 13px;
      color: rgba(255,255,255,0.90) !important;
      text-shadow: 0 2px 12px rgba(0,0,0,0.85);
      font-weight: 500;
    }}

    /* LISTES */
    .tm-card ul, .tm-card li {{
      color: rgba(255,255,255,0.95) !important;
      text-shadow: 0 2px 14px rgba(0,0,0,0.75);
    }}

    /* INPUTS */
    .stTextInput label {{
      color: rgba(255,255,255,0.95) !important;
      text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    }}

    .stTextInput input {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.32) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder {{
      color: rgba(255,255,255,0.65) !important;
    }}

    .stTextInput input:focus {{
      border: 1px solid rgba(255,255,255,0.80) !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.18) !important;
      outline: none !important;
    }}

    /* BOUTONS */
    .stButton > button {{
      width: 100% !important;
      height: 56px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.30) !important;
      background: rgba(255,255,255,0.18) !important;
      color: #FFFFFF !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      box-shadow: 0 16px 34px rgba(0,0,0,0.45) !important;
      text-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.28) !important;
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
