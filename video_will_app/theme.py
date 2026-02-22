import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme() -> None:
    css = f"""
    <style>
    /* ===== Background ===== */
    .stApp {{
      background:
        linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.80)),
        url("{BG_URL}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}

    /* ===== Global typography (nuances de blanc uniquement) ===== */
    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: rgba(255,255,255,0.92) !important;
    }}

    /* Force les textes Streamlit (sinon il remet du gris) */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span {{
      color: rgba(255,255,255,0.92) !important;
    }}

    /* Titres bien visibles */
    h1, h2, h3, h4, h5, h6 {{
      color: #FFFFFF !important;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    /* ===== Cards ===== */
    .tm-card {{
      background: rgba(15,18,22,0.82);
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    .tm-title {{
      font-size: 46px;
      font-weight: 750;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #FFFFFF 0%, rgba(255,255,255,0.88) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.88) !important;
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.72) !important;
    }}

    /* “Commencer” : blanc visible */
    .tm-section-title {{
      font-size: 22px;
      font-weight: 750;
      color: #FFFFFF !important;
      margin: 0 0 6px 0;
    }}

    /* Texte d’aide sous “Commencer” : blanc 85% */
    .tm-section-desc {{
      color: rgba(255,255,255,0.85) !important;
      margin: 0;
      font-size: 14px;
      font-weight: 500;
    }}

    /* “En continuant…” : blanc 75% (lisible mais discret) */
    .tm-footnote {{
      color: rgba(255,255,255,0.78) !important;
      font-size: 12.5px;
      font-weight: 500;
      margin-top: 10px;
    }}

    /* ===== Inputs ===== */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.90) !important;
      font-weight: 600 !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
      color: rgba(255,255,255,0.65) !important;
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

    /* ===== Columns align (boutons mêmes niveaux) ===== */
    div[data-testid="column"] {{
      display: flex !important;
      align-items: flex-start !important;
    }}

    div[data-testid="column"] > div {{
      width: 100% !important;
    }}

    div[data-testid="column"] .element-container,
    div[data-testid="column"] .stMarkdown,
    div[data-testid="column"] .stButton {{
      margin: 0 !important;
      padding: 0 !important;
    }}

    /* ===== Buttons ===== */
    .stButton > button {{
      width: 100% !important;
      height: 56px !important;
      min-height: 56px !important;
      padding: 0 22px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.22) !important;
      background: rgba(255,255,255,0.10) !important;
      color: #FFFFFF !important;
      font-size: 16px !important;
      font-weight: 650 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.18) !important;
    }}

    .tm-primary .stButton > button {{
      background: rgba(255,255,255,0.92) !important;
      color: rgba(17,24,39,1) !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: #FFFFFF !important;
    }}

    .tm-btnwrap {{
      margin: 0 !important;
      padding: 0 !important;
      display: block !important;
    }}

    @media (max-width: 520px) {{
      .tm-title {{ font-size: 36px; }}
      .tm-card {{ padding: 22px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
