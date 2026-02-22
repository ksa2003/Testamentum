import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"


def apply_theme() -> None:
    css = f"""
    <style>
    /* =========================
       Background (tu voulais le garder)
    ========================== */
    .stApp {{
      background:
        linear-gradient(rgba(0,0,0,0.62), rgba(0,0,0,0.78)),
        url("{BG_URL}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}

    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: #FFFFFF;
    }}

    /* Largeur */
    section.main > div {{
      max-width: 920px;
      padding-top: 2.2rem;
    }}

    /* =========================
       Card + Typo (LISIBILITÉ)
    ========================== */
    .tm-card {{
      background: rgba(10,12,16,0.84);
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 18px;
      padding: 26px;
      backdrop-filter: blur(18px);
      box-shadow: 0 22px 100px rgba(0,0,0,0.70);
    }}

    /* Titre principal */
    .tm-title {{
      font-size: 46px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: rgba(255,255,255,0.98);
      text-shadow: 0 6px 26px rgba(0,0,0,0.65);
      -webkit-text-fill-color: initial;
    }}

    /* Sous-titre */
    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.92);
      text-shadow: 0 2px 12px rgba(0,0,0,0.55);
    }}

    /* Phrase latine */
    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.82);
      text-shadow: 0 2px 12px rgba(0,0,0,0.55);
    }}

    /* Titres secondaires (ex: Commencer, etc.) */
    .tm-h2 {{
      font-size: 22px;
      font-weight: 800;
      margin: 0 0 6px 0;
      color: rgba(255,255,255,0.98);
      text-shadow: 0 4px 18px rgba(0,0,0,0.60);
    }}

    /* Texte normal */
    .tm-text {{
      font-size: 14px;
      line-height: 1.55;
      color: rgba(255,255,255,0.92);
      text-shadow: 0 2px 12px rgba(0,0,0,0.55);
    }}

    /* Listes / bullets */
    .tm-card ul, .tm-card li {{
      color: rgba(255,255,255,0.92) !important;
      text-shadow: 0 2px 12px rgba(0,0,0,0.55);
    }}

    /* =========================
       Chips (Mémoire / Transmission / etc.)
    ========================== */
    .tm-chiprow {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
      margin-bottom: 14px;
    }}

    .tm-chip {{
      display: inline-flex;
      align-items: center;
      padding: 7px 12px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.26);
      background: rgba(255,255,255,0.12);
      font-size: 12px;
      font-weight: 650;
      color: rgba(255,255,255,0.96);
      text-shadow: 0 2px 10px rgba(0,0,0,0.45);
    }}

    /* =========================
       Inputs (Email, etc.)
    ========================== */
    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.92) !important;
      text-shadow: 0 2px 10px rgba(0,0,0,0.55);
    }}

    .stTextInput input, .stTextArea textarea {{
      background: rgba(0,0,0,0.45) !important;
      border: 1px solid rgba(255,255,255,0.28) !important;
      color: rgba(255,255,255,0.96) !important;
      border-radius: 12px !important;
    }}

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
      color: rgba(255,255,255,0.60) !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
      border: 1px solid rgba(255,255,255,0.72) !important;
      box-shadow: 0 0 0 3px rgba(255,255,255,0.16) !important;
      outline: none !important;
    }}

    /* Evite les bordures "invalid" rouges */
    input:invalid {{
      border: 1px solid rgba(255,255,255,0.28) !important;
      box-shadow: none !important;
    }}

    /* =========================
       Colonnes + Alignement boutons (tes problèmes d'alignement)
    ========================== */
    div[data-testid="column"] {{
      display: flex !important;
      align-items: stretch !important;
    }}

    div[data-testid="column"] > div {{
      width: 100% !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-end !important;
    }}

    div[data-testid="column"] .element-container,
    div[data-testid="column"] .stMarkdown,
    div[data-testid="column"] .stButton {{
      margin: 0 !important;
      padding: 0 !important;
    }}

    /* =========================
       Buttons (visibles + même hauteur + même alignement)
    ========================== */
    .stButton > button {{
      width: 100% !important;
      height: 56px !important;
      min-height: 56px !important;
      padding: 0 22px !important;
      border-radius: 999px !important;
      border: 1px solid rgba(255,255,255,0.26) !important;
      background: rgba(255,255,255,0.14) !important;
      color: rgba(255,255,255,0.96) !important;
      font-size: 16px !important;
      font-weight: 700 !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      box-shadow: 0 16px 34px rgba(0,0,0,0.35) !important;
      text-shadow: 0 2px 10px rgba(0,0,0,0.35);
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.20) !important;
      border-color: rgba(255,255,255,0.34) !important;
    }}

    .stButton > button:disabled {{
      opacity: 0.55 !important;
    }}

    /* Bouton principal (si tu entoures le bouton avec une div class tm-primary) */
    .tm-primary .stButton > button {{
      background: rgba(255,255,255,0.90) !important;
      color: rgba(17,24,39,0.98) !important;
      border: none !important;
      text-shadow: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: rgba(255,255,255,0.96) !important;
    }}

    .tm-btnwrap {{
      margin: 0 !important;
      padding: 0 !important;
      display: block !important;
    }}

    /* =========================
       Mobile
    ========================== */
    @media (max-width: 520px) {{
      .tm-title {{ font-size: 36px; }}
      .tm-card {{ padding: 22px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
