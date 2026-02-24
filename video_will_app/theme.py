import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme() -> None:
    """
    Thème global (CSS uniquement).
    Ne pas appeler st.set_page_config ici : doit rester dans app.py (ou tout début de chaque page).
    """
    css = f"""
    <style>
    /* Fond global */
    .stApp {{
      background:
        linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.80)),
        url("{BG_URL}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}

    /* Typo */
    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: #FFFFFF;
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    /* Cartes */
    .tm-card {{
      background: rgba(15,18,22,0.82);
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    .tm-card2 {{
      background: rgba(15,18,22,0.72);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 16px;
      padding: 22px;
      backdrop-filter: blur(14px);
      box-shadow: 0 18px 80px rgba(0,0,0,0.55);
    }}

    /* Titres / textes (nuances de blanc lisibles) */
    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #F5F1E6 0%, #D7C09A 55%, #B99257 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.86);
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.70);
    }}

    .tm-h2 {{
      font-size: 34px;
      font-weight: 800;
      color: rgba(255,255,255,0.94);
      margin: 0;
    }}

    .tm-h3 {{
      font-size: 22px;
      font-weight: 750;
      color: rgba(255,255,255,0.94);
      margin: 0;
    }}

    .tm-p {{
      font-size: 15px;
      line-height: 1.55;
      color: rgba(255,255,255,0.82);
    }}

    .tm-muted {{
      font-size: 13px;
      color: rgba(255,255,255,0.82);
    }}

    /* Inputs */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.88) !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: #FFFFFF !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
      color: rgba(255,255,255,0.58) !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
      border: 1px solid rgba(255,255,255,0.70) !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.15) !important;
      outline: none !important;
    }}

    /* Colonnes : alignement strict */
    div[data-testid="column"] {{
      display: flex !important;
      align-items: stretch !important;
    }}
    div[data-testid="column"] > div {{
      width: 100% !important;
      display: flex !important;
      flex-direction: column !important;
    }}
    div[data-testid="column"] .element-container,
    div[data-testid="column"] .stMarkdown,
    div[data-testid="column"] .stButton,
    div[data-testid="column"] div[data-testid="stFormSubmitButton"] {{
      margin: 0 !important;
      padding: 0 !important;
    }}

    /* Boutons : taille identique + pas de retour à la ligne */
    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {{
      width: 100% !important;
      height: 56px !important;
      min-height: 56px !important;
      padding: 0 22px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.22) !important;
      background: rgba(255,255,255,0.10) !important;
      color: rgba(255,255,255,0.92) !important;
      font-size: 16px !important;
      font-weight: 650 !important;
      white-space: nowrap !important;
      line-height: 1 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }}

    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {{
      background: rgba(255,255,255,0.18) !important;
    }}

    .tm-primary .stButton > button,
    .tm-primary div[data-testid="stFormSubmitButton"] > button {{
      background: #E5E7EB !important;
      color: #111827 !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover,
    .tm-primary div[data-testid="stFormSubmitButton"] > button:hover {{
      background: #F3F4F6 !important;
    }}

    /* Petites bulles (chips) */
    .tm-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 14px;
      margin-bottom: 16px;
    }}
    .tm-chip {{
      padding: 8px 16px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.18);
      background: rgba(255,255,255,0.08);
      color: rgba(255,255,255,0.90);
      font-size: 13px;
      font-weight: 650;
    }}

    @media (max-width: 520px) {{
      .tm-title {{ font-size: 36px; }}
      .tm-card {{ padding: 22px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
