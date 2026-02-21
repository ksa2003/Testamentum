import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ------------------------------------------------------------
# THEME X (noir, blanc, bleu) + layout mobile-first
# ------------------------------------------------------------
st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}

      /* Pour éviter l'effet "app Streamlit", on peut cacher la sidebar */
      [data-testid="stSidebar"] {display:none;}

      :root{
        --bg:#000000;
        --surface:#0b0f14;
        --surface2:#0f1419;
        --border:#2f3336;
        --text:#e7e9ea;
        --muted:#8b98a5;
        --accent:#1d9bf0; /* bleu X */
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{
        max-width: 980px !important;
        padding-top: 1.0rem !important;
      }

      /* Inputs Streamlit - IMPORTANT pour voir le texte tapé */
      .stTextInput input{
        background: var(--surface2) !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        caret-color: var(--text) !important;
        border-radius: 14px !important;
        padding: 0.95rem 1rem !important;
      }
      .stTextInput input::placeholder{ color: var(--muted) !important; }
      .stTextInput label{
        color: var(--muted) !important;
        font-weight: 800 !important;
      }

      .stButton button{
        background: var(--accent) !important;
        color: #001018 !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.9rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }
      .stButton button:hover{ filter: brightness(1.05); }

      .fine{
        color: var(--muted);
        font-size: 0.86rem;
        line-height: 1.4;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HERO (HTML rendu, donc aucun code n'apparaît)
# ------------------------------------------------------------
hero = """
<div style="
  border:1px solid #2f3336;
  background:
    radial-gradient(900px circle at 15% 10%, rgba(29,155,240,0.22), transparent 38%),
    radial-gradient(700px circle at 85% 30%, rgba(255,255,255,0.06), transparent 40%),
    #0b0f14;
  border-radius: 18px;
  padding: 18px;
">
  <div style="display:flex; align-items:center; justify-content:space-between; gap:12px; flex-wrap:wrap;">
    <div style="color:#e7e9ea; font-weight:900; letter-spacing:.02em; font-size:1.1rem;">Testamentum</div>
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
      <span style="border:1px solid #2f3336; padding:7px 12px; border-radius:999px; color:#8b98a5; font-weight:800; font-size:.9rem; background:rgba(255,255,255,0.02);">Sécurité</span>
      <span style="border:1px solid #2f3336; padding:7px 12px; border-radius:999px; color:#8b98a5; font-weight:800; font-size:.9rem; background:rgba(255,255,255,0.02);">Confidentialité</span>
      <span style="border:1px solid #2f3336; padding:7px 12px; border-radius:999px; color:#8b98a5; font-weight:800; font-size:.9rem; background:rgba(255,255,255,0.02);">Traçabilité</span>
    </div>
  </div>

  <div style="margin-top:14px; color:#e7e9ea; font-weight:950; font-size:clamp(1.8rem, 4.2vw, 2.6rem); line-height:1.08;">
    Un message vidéo, transmis au bon moment.
  </div>

  <div style="margin-top:10px; color:#e7e9ea; opacity:.92; font-size:1.05rem; line-height:1.55; max-width:68ch;">
    Enregistrez un message vidéo destiné à vos proches, puis contrôlez l’accès des bénéficiaires lorsque le décès est déclaré.
    Le tout avec des règles strictes (jeton, expiration, journalisation).
  </div>

  <div style="margin-top:12px; color:#e7e9ea; opacity:.88; line-height:1.65;">
    • Accès bénéficiaires par jeton temporaire et sécurisé<br/>
    • Option de validation par notaire (workflow métier)<br/>
    • Historique des actions pour la traçabilité (MVP)
  </div>

  <div style="height:14px;"></div>

  <div style="
    border:1px solid #2f3336;
    background:#0f1419;
    border-radius: 16px;
    padding: 14px;
    color:#8b98a5;
    font-size:.92rem;
    line-height:1.5;
  ">
    Version MVP : la mise en production internationale implique des exigences juridiques par pays
    (succession, notariat, protection des données).
  </div>
</div>
"""
components.html(hero, height=360, scrolling=False)

st.write("")

# ------------------------------------------------------------
# CTA (Streamlit, donc fonctionnel + lisible)
# ------------------------------------------------------------
st.subheader("Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

if st.button("Continuer"):
    st.session_state["prefill_email"] = email.strip()
    st.switch_page("pages/1_Connexion.py")

st.markdown(
    '<div class="fine">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
    unsafe_allow_html=True,
)
