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

    html, body, [class*="css"] {{
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
      color: #FFFFFF;
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

    /* ====== TITRE: mêmes tailles que ta version (ne pas changer) ====== */
    .tm-title {{
      font-size: 46px;
      font-weight: 750;
      letter-spacing: -0.02em;

      /* Couleurs plus “solennelles” (ivoire / or ancien / cuivre / légère touche bordeaux) */
      background: linear-gradient(
        90deg,
        rgba(255, 248, 235, 0.98) 0%,
        rgba(233, 214, 170, 0.96) 40%,
        rgba(191, 145, 96, 0.92) 78%,
        rgba(255, 255, 255, 0.88) 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;

      text-shadow:
        0 10px 34px rgba(0,0,0,0.60),
        0 0 22px rgba(191,145,96,0.08);
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

    /* IMPORTANT: on laisse tes bulles “Mémoire / Transmission ...”
       Elles viennent de ton HTML/Markdown (spans) ou de ton CSS existant.
       On n’y touche pas ici pour garder EXACTEMENT le rendu de ta photo. */

    .stTextInput label, .stTextArea label {{
      color: rgba(255,255,255,0.85) !important;
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
