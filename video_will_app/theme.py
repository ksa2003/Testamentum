import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"


def apply_theme() -> None:
    """
    Applique uniquement le CSS (PAS de st.set_page_config ici).
    Important : set_page_config doit être appelé une seule fois et avant tout affichage,
    idéalement dans app.py tout en haut, pas dans theme.py.
    """
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
      color: rgba(255,255,255,0.92);
    }}

    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    .tm-card {{
      background: rgba(15,18,22,0.82);
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    /* TITRE: ton “Testamentum” en teinte ivoire/doré (sobre, pas vert) */
    .tm-title {{
      font-size: 46px;
      font-weight: 750;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #F7F3EA 0%, #E7DDC6 55%, #D1C1A1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 6px 22px rgba(0,0,0,0.35);
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.85);
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.70);
    }}

    /* Labels lisibles (nuances de blanc, pas gris sur gris) */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.88) !important;
      font-weight: 600 !important;
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: rgba(255,255,255,0.95) !important;
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

    input:invalid {{
      border: 1px solid rgba(255,255,255,0.28) !important;
      box-shadow: none !important;
    }}

    /* Colonnes: garantit même hauteur/alignement des boutons */
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

    /* Boutons: même taille + bien centrés */
    .stButton > button {{
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
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      white-space: nowrap !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.18) !important;
    }}

    /* Variante bouton “primaire” si tu l’utilises via wrapper .tm-primary */
    .tm-primary .stButton > button {{
      background: #E5E7EB !important;
      color: #111827 !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: #F3F4F6 !important;
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
