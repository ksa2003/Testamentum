import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"


def apply_theme() -> None:
    """
    CSS uniquement (pas de st.set_page_config ici).
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

    /* TITRE: ivoire/doré léger */
    .tm-title {{
      font-size: 46px;
      font-weight: 750;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #F7F3EA 0%, #E7DDC6 55%, #D1C1A1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 6px 22px rgba(0,0,0,0.35);
      margin: 0 0 6px 0;
    }}

    .tm-sub {{
      font-size: 14px;
      color: rgba(255,255,255,0.85);
      margin: 0 0 6px 0;
    }}

    .tm-latin {{
      font-size: 13px;
      font-style: italic;
      color: rgba(255,255,255,0.70);
      margin: 0 0 14px 0;
    }}

    /* Bulles */
    .tm-chips {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin: 6px 0 18px 0;
    }}
    .tm-chip {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 18px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.22);
      background: rgba(255,255,255,0.10);
      color: rgba(255,255,255,0.92);
      font-size: 16px;
      font-weight: 650;
      line-height: 1;
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.12);
    }}

    /* Nuances lisibles */
    .tm-muted {{
      color: rgba(255,255,255,0.75);
    }}
    .tm-strong {{
      color: rgba(255,255,255,0.95);
      font-weight: 650;
    }}

    /* Inputs */
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

    /* ============================
       ALIGNEMENT BOUTONS (FIX)
       ============================ */

    /* Forcer les colonnes à avoir la même "baseline" et supprimer les marges parasites */
    div[data-testid="stHorizontalBlock"] {{
      align-items: stretch !important;
    }}

    div[data-testid="column"] {{
      display: flex !important;
      align-items: stretch !important;  /* important: stretch */
    }}

    div[data-testid="column"] > div {{
      width: 100% !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-start !important;
    }}

    /* Supprime les écarts automatiques dans les colonnes */
    div[data-testid="column"] .element-container {{
      margin: 0 !important;
      padding: 0 !important;
    }}

    /* Le conteneur des boutons doit être identique dans chaque colonne */
    div[data-testid="column"] .stButton {{
      width: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      display: block !important;
    }}

    /* Boutons: même hauteur, même alignement vertical */
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
      line-height: 1 !important;
      box-sizing: border-box !important;
    }}

    .stButton > button:hover {{
      background: rgba(255,255,255,0.18) !important;
    }}

    .tm-primary .stButton > button {{
      background: #E5E7EB !important;
      color: #111827 !important;
      border: none !important;
    }}

    .tm-primary .stButton > button:hover {{
      background: #F3F4F6 !important;
    }}

    @media (max-width: 520px) {{
      .tm-title {{ font-size: 36px; }}
      .tm-card {{ padding: 22px; }}
      .tm-chip {{ font-size: 15px; padding: 9px 16px; }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
