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
      color: rgba(255,255,255,0.82
