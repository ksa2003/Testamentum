import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"


def apply_theme() -> None:
    """Applique le thème global Kidan Vid (background + cartes + boutons + chips)."""

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

    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: #FFFFFF;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    /* ---- Cards ---- */
    .tm-card {{
      background: rgba(15,18,22,0.82);
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    .tm-card p {{
      color: rgba(255,255,255,0.86);
      line-height: 1.55;
    }}

    .tm-card li {{
      color: rgba(255,255,255,0.86);
      margin: 0.35rem 0;
    }}

    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      letter-spacing: -0.02em;
      /* ton "pierre"/ivoire (accord avec le thème funéraire) */
      background: linear-gradient(90deg, #F3EDE2 0%, #E7DCC7 45%, #F8F3EA 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.82);
      margin-top: 6px;
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.70);
      margin-top: 6px;
    }}

    .tm-h2 {{
      font-size: 34px;
      font-weight: 800;
      letter-spacing: -0.01em;
      color: rgba(255,255,255,0.95);
      margin: 18px 0 10px 0;
    }}

    .tm-h3 {{
      font-size: 20px;
      font-weight: 750;
      color: rgba(255,255,255,0.92);
      margin: 0 0 10px 0;
    }}

    .tm-muted {{
      color: rgba(255,255,255,0.78);
    }}

    /* ---- Chips (bulles) ---- */
    .tm-chips {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 14px;
      margin-bottom: 14px;
    }}

    .tm-chip {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 9px 16px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.20);
      background: rgba(255,255,255,0.10);
      color: rgba(255,255,255,0.94);
      font-size: 14px;
      font-weight: 700;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.04);
    }}

    /* ---- Inputs ---- */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.88) !important;
      font-weight: 650 !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
      color: rgba(255,255,255,0.55) !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
      border: 1px solid rgba(255,255,255,0.70) !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.15) !important;
      outline: none !important;
    }}

    input:invalid {{
      border: 1px solid rgba(255,255,255,0.28) !important;
      box-shadow: none !important;
    }}

    /* ---- Columns / alignment ---- */
    div[data-testid="column"] {{
      display: flex !important;
      align-items: flex-start !important;
    }}

    div[data-testid="column"] > div {{
      width: 100% !important;
    }}

    div[data-testid="column"] .element-container,
    div[data-testid="column"] .stMarkdown,
    div[data-testid="column"] .stButton,
    div[data-testid="column"] .stForm {{
      margin: 0 !important;
      padding: 0 !important;
    }}

    /* ---- Buttons ---- */
    .stButton > button {{
      width: 100% !important;
      height: 56px !important;
      min-height: 56px !important;
      padding: 0 22px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.22) !important;
      background: rgba(255,255,255,0.10) !important;
      color: rgba(255,255,255,0.96) !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.18) !important;
    }}

    .tm-primary .stButton > button {{
      background: #E7DCC7 !important;
      color: #111827 !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: #F3EDE2 !important;
    }}

    /* petit texte en bas */
    .tm-footnote {{
      color: rgba(255,255,255,0.82);
      font-size: 13px;
      font-weight: 600;
      margin-top: 12px;
    }}

    /* Images dans les pages */
    img {{
      border-radius: 14px;
    }}

    @media (max-width: 520px) {{
      .tm-title {{ font-size: 36px; }}
      .tm-card {{ padding: 22px; }}
      .tm-h2 {{ font-size: 28px; }}
      .tm-chip {{ padding: 8px 14px; font-size: 13px; }}
    }}
    </style>
    """

    st.set_page_config(page_title="Kidan Vid", page_icon="⚖️", layout="centered")
    st.markdown(css, unsafe_allow_html=True)
