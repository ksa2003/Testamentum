import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ---------------------------------------------------
# THEME sérieux (sobriété, lisible, international)
# ---------------------------------------------------
st.markdown(
    """
    <style>
      #MainMenu { visibility: hidden; }
      footer { visibility: hidden; }
      header { visibility: hidden; }

      /* Optionnel : cacher sidebar si vous ne voulez pas le menu Streamlit */
      [data-testid="stSidebar"] { display: none; }

      :root{
        --bg: #0B1220;
        --bg2:#0A0F1A;
        --surface: rgba(255,255,255,0.06);
        --border: rgba(255,255,255,0.12);
        --text: #F5F7FA;
        --muted: rgba(245,247,250,0.75);
        --accent: #3B82F6; /* bleu sobre */
      }

      .stApp { background: linear-gradient(180deg, var(--bg) 0%, var(--bg2) 100%) !important; }
      section.main > div { padding: 0 !important; max-width: 100% !important; }

      /* Inputs & buttons */
      .stTextInput input{
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        color: var(--text) !important;
        border-radius: 12px !important;
        padding: 0.85rem 0.9rem !important;
      }
      .stTextInput label{
        color: var(--muted) !important;
        font-weight: 700 !important;
      }
      .stButton button{
        background: var(--accent) !important;
        color: #081225 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.85rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }
      .stButton button:hover{ filter: brightness(1.08); }

      /* Layout helpers */
      .wrap{
        min-height: 100vh;
        padding: 26px 18px;
      }
      .container{
        max-width: 1120px;
        margin: 0 auto;
      }
      .topbar{
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap: 12px;
        margin-bottom: 26px;
      }
      .brand{
        font-weight: 900;
        letter-spacing: 0.04em;
        color: var(--text);
        font-size: 1.25rem;
      }
      .badge{
        border: 1px solid rgba(255,255,255,0.16);
        background: rgba(255,255,255,0.05);
        color: rgba(245,247,250,0.85);
        padding: 8px 12px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.92rem;
      }
      .grid{
        display:grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 22px;
        align-items:start;
      }
      @media (max-width: 900px){
        .grid{ grid-template-columns: 1fr; }
      }

      .hero{
        padding: 26px;
        border-radius: 18px;
        border: 1px solid var(--border);
        background:
          radial-gradient(900px circle at 10% 10%, rgba(59,130,246,0.18), transparent 40%),
          radial-gradient(700px circle at 90% 20%, rgba(16,185,129,0.10), transparent 35%),
          radial-gradient(900px circle at 50% 90%, rgba(99,102,241,0.12), transparent 40%),
          rgba(255,255,255,0.04);
      }
      .h1{
        color: var(--text);
        font-weight: 900;
        font-size: clamp(2.0rem, 3.6vw, 3.0rem);
        line-height: 1.07;
        margin: 0 0 12px 0;
      }
      .lead{
        color: var(--muted);
        font-size: 1.06rem;
        line-height: 1.55;
        margin: 0 0 14px 0;
        max-width: 62ch;
      }
      .bullets{
        color: rgba(245,247,250,0.82);
        font-size: 1.02rem;
        line-height: 1.6;
      }
      .card{
        padding: 18px;
        border-radius: 18px;
        border: 1px solid var(--border);
        background: rgba(255,255,255,0.04);
      }
      .card h3{
        margin: 0 0 6px 0;
        color: var(--text);
        font-weight: 900;
        font-size: 1.05rem;
      }
      .muted{
        color: var(--muted);
        font-size: 0.96rem;
        line-height: 1.55;
        margin: 0 0 10px 0;
      }
      .fine{
        color: rgba(245,247,250,0.62);
        font-size: 0.86rem;
        line-height: 1.45;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# HERO EN HTML "SÛR" (ne s'affichera jamais comme du code)
# ---------------------------------------------------
hero_html = """
<div class="wrap">
  <div class="container">
    <div class="topbar">
      <div class="brand">Testamentum</div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <div class="badge">Confidentialité</div>
        <div class="badge">Sécurité</div>
        <div class="badge">Traçabilité</div>
      </div>
    </div>

    <div class="grid">
      <div class="hero">
        <div class="h1">Un message vidéo, transmis avec respect et contrôle.</div>
        <div class="lead">
          Testamentum permet d’enregistrer un message vidéo à destination de vos proches, puis d’en gérer l’accès
          selon des règles strictes et traçables, lorsque le décès est déclaré.
        </div>

        <div class="bullets">
          • Accès des bénéficiaires par jeton sécurisé et temporaire<br/>
          • Workflow de validation notaire (optionnel, selon pays)<br/>
          • Stockage sécurisé et journalisation des actions (MVP)
        </div>
      </div>

      <div class="card">
        <h3>Commencer</h3>
        <p class="muted">Saisissez votre adresse e-mail pour créer un compte ou vous connecter.</p>
        <p class="fine">
          Ce service est en version MVP. La mise en production internationale implique des exigences juridiques
          et de conformité (données, succession, notariat) par pays.
        </p>
      </div>
    </div>
  </div>
</div>
"""

# On rend le HTML via components.html (évite 100% l'affichage en "code")
components.html(hero_html, height=520, scrolling=False)

# ---------------------------------------------------
# CTA Streamlit (inputs + bouton)
# ---------------------------------------------------
cta_container = st.container()
with cta_container:
    left, right = st.columns([1.2, 0.8])
    with right:
        email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")
        if st.button("Continuer"):
            st.session_state["prefill_email"] = email.strip()
            st.switch_page("pages/1_Connexion.py")
        st.markdown(
            '<div class="fine">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
            unsafe_allow_html=True
        )
