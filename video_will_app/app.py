import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# -----------------------------
# Style X-like (sobriété)
# -----------------------------
st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}

      /* Garder la sidebar visible si vous voulez la navigation, sinon commentez la ligne suivante */
      /* [data-testid="stSidebar"] {display:none;} */

      :root{
        --bg:#000000;
        --surface:#0b0f14;
        --border:#2f3336;
        --text:#e7e9ea;
        --muted:#71767b;
        --accent:#1d9bf0; /* bleu X */
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{ padding: 0 !important; max-width: 100% !important; }

      /* Inputs Streamlit */
      .stTextInput input{
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;           /* IMPORTANT: texte visible */
        caret-color: var(--text) !important;     /* curseur visible */
        border-radius: 14px !important;
        padding: 0.9rem 1rem !important;
      }
      .stTextInput input::placeholder{ color: var(--muted) !important; }
      .stTextInput label{ color: var(--muted) !important; font-weight: 700 !important; }

      .stButton button{
        background: var(--accent) !important;
        color: #001018 !important;
        border-radius: 999px !important;
        border: none !important;
        padding: 0.9rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }

      .stButton button:hover{ filter: brightness(1.05); }

      /* Sections */
      .wrap{ min-height: 100vh; padding: 22px 16px; }
      .container{ max-width: 1080px; margin: 0 auto; }

      .topbar{
        display:flex; justify-content:space-between; align-items:center;
        padding: 12px 4px 18px 4px;
      }
      .brand{ color: var(--text); font-weight: 900; font-size: 1.2rem; letter-spacing: .02em; }
      .badge{
        color: var(--muted); border:1px solid var(--border);
        padding: 7px 12px; border-radius:999px; font-weight:700; font-size:0.9rem;
        background: rgba(255,255,255,0.02);
      }

      .hero{
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;
        background:
          radial-gradient(900px circle at 20% 10%, rgba(29,155,240,0.20), transparent 35%),
          radial-gradient(700px circle at 80% 30%, rgba(255,255,255,0.06), transparent 40%),
          var(--surface);
      }

      .grid{
        display:grid; grid-template-columns: 1.15fr 0.85fr;
        gap: 18px; align-items:start;
      }
      @media (max-width: 900px){ .grid{ grid-template-columns: 1fr; } }

      .h1{
        margin: 0 0 10px 0;
        color: var(--text);
        font-weight: 900;
        font-size: clamp(2.0rem, 4vw, 2.8rem);
        line-height: 1.08;
      }
      .lead{
        margin: 0 0 12px 0;
        color: var(--text);
        opacity: 0.92;
        font-size: 1.05rem;
        line-height: 1.55;
        max-width: 62ch;
      }
      .muted{ color: var(--muted); font-size: 0.95rem; line-height: 1.5; }
      .list{ color: var(--text); opacity: 0.90; line-height: 1.65; font-size: 1.0rem; }

      .card{
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 18px;
        background: rgba(255,255,255,0.02);
      }
      .card h3{ margin:0 0 8px 0; color: var(--text); font-weight: 900; }
      .fine{ color: var(--muted); font-size: 0.86rem; margin-top: 10px; line-height: 1.45; }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_html = """
<div class="wrap">
  <div class="container">
    <div class="topbar">
      <div class="brand">Testamentum</div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <div class="badge">Sécurité</div>
        <div class="badge">Confidentialité</div>
        <div class="badge">Traçabilité</div>
      </div>
    </div>

    <div class="grid">
      <div class="hero">
        <div class="h1">Transmettez un message vidéo à vos proches, de manière encadrée.</div>
        <div class="lead">
          Un coffre numérique pour enregistrer un message vidéo et gérer l’accès des bénéficiaires
          selon des règles strictes (jeton, expiration, journalisation), lorsque le décès est déclaré.
        </div>
        <div class="list">
          • Accès bénéficiaires par jeton temporaire<br/>
          • Option de validation notaire (workflow métier)<br/>
          • Historique des actions (MVP)
        </div>
      </div>

      <div class="card">
        <h3>Commencer</h3>
        <div class="muted">Saisissez votre e-mail pour créer un compte ou vous connecter.</div>
        <div class="fine">
          Version MVP : la conformité juridique dépend des pays (succession, notariat, protection des données).
        </div>
      </div>
    </div>
  </div>
</div>
"""
components.html(hero_html, height=420, scrolling=False)

# CTA Streamlit (à droite sur desktop / en dessous sur mobile)
_, col = st.columns([1.2, 0.8])
with col:
    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")
    if st.button("Continuer"):
        st.session_state["prefill_email"] = email.strip()
        st.switch_page("pages/1_Connexion.py")
    st.markdown(
        '<div class="fine">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
        unsafe_allow_html=True,
    )
