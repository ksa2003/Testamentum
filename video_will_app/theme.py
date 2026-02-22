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

    /* ===== Typo globale : nuances de blanc ===== */
    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: rgba(255,255,255,0.82) !important;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown span {{
      color: rgba(255,255,255,0.82) !important;
      line-height: 1.55;
    }}

    h1, h2, h3, h4, h5, h6 {{
      color: rgba(255,255,255,0.90) !important;
      letter-spacing: -0.01em;
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

    /* ===== Titre “Testamentum” (forme signature) ===== */
    .tm-title {{
      font-size: 48px;
      font-weight: 820;
      letter-spacing: -0.03em;
      line-height: 1.03;
      font-family: "Georgia", "Times New Roman", ui-serif, serif;

      background: linear-gradient(
        90deg,
        rgba(132, 233, 214, 0.96) 0%,
        rgba(221, 196, 140, 0.94) 55%,
        rgba(255, 255, 255, 0.84) 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;

      text-shadow:
        0 8px 30px rgba(0,0,0,0.55),
        0 0 18px rgba(132,233,214,0.08);
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.80) !important;
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.66) !important;
    }}

    /* ===== Section “Commencer” : rendre lisible (blanc nuancé) ===== */
    .tm-section-title {{
      font-size: 20px;
      font-weight: 780;
      color: rgba(255,255,255,0.92) !important;
      margin: 0 0 6px 0;
      text-shadow: 0 10px 30px rgba(0,0,0,0.55);
    }}

    .tm-section-desc {{
      color: rgba(255,255,255,0.84) !important;
      margin: 0;
      font-size: 14px;
      font-weight: 560;
      text-shadow: 0 10px 30px rgba(0,0,0,0.50);
    }}

    /* ===== “En continuant…” : blanc nuancé bien visible ===== */
    .tm-footnote {{
      color: rgba(255,255,255,0.80) !important;
      font-size: 12.8px;
      font-weight: 560;
      margin-top: 10px;
      text-shadow: 0 10px 26px rgba(0,0,0,0.55);
    }}

    /* Sécurité : si la phrase est rendue via st.caption / small / p */
    .tm-footnote p, .tm-footnote small, .tm-footnote span {{
      color: rgba(255,255,255,0.80) !important;
    }}

    /* ===== Inputs ===== */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.80) !important;
      font-weight: 600 !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.26) !important;
      color: rgba(255,255,255,0.88) !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
      color: rgba(255,255,255,0.52) !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
      border: 1px solid rgba(255,255,255,0.55) !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.10) !important;
      outline: none !important;
    }}

    input:invalid {{
      border: 1px solid rgba(255,255,255,0.26) !important;
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
      border: 1px solid rgba(255,255,255,0.20) !important;
      background: rgba(255,255,255,0.09) !important;
      color: rgba(255,255,255,0.86) !important;
      font-size: 16px !important;
      font-weight: 650 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.14) !important;
      color: rgba(255,255,255,0.92) !important;
    }}

    .tm-primary .stButton > button {{
      background: rgba(229,231,235,0.88) !important;
      color: rgba(17,24,39,0.98) !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: rgba(243,244,246,0.92) !important;
    }}

    .tm-btnwrap {{
      margin: 0 !important;
      padding: 0 !important;
      display: block !important;
    }}

    @media (max-width: 520px) {{
      .tm-title {{ font-size: 38px; }}
      .tm-card {{ padding: 22px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
