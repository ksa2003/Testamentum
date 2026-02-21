import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}

      /* Cache la sidebar Streamlit pour un rendu "site" */
      [data-testid="stSidebar"] {display:none;}

      :root{
        --bg:#f3f2ef;         /* LinkedIn background */
        --card:#ffffff;
        --text:#191919;
        --muted:#5f6368;
        --border:#e0e0e0;
        --blue:#0a66c2;       /* LinkedIn blue */
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{ max-width: 1100px !important; padding-top: 1.2rem !important; }

      .topbar{
        display:flex; align-items:center; justify-content:space-between;
        margin-bottom: 16px;
      }
      .brand{ font-weight: 900; letter-spacing: .02em; font-size: 1.2rem; color: var(--text); }
      .pill{
        border:1px solid var(--border);
        background: var(--card);
        padding: 8px 12px;
        border-radius: 999px;
        color: var(--muted);
        font-weight: 700;
        font-size: 0.92rem;
      }

      .grid{
        display:grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 16px;
      }
      @media (max-width: 900px){
        .grid{ grid-template-columns: 1fr; }
      }

      .card{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 16px;
      }

      .h1{
        margin: 0 0 8px 0;
        font-size: clamp(1.8rem, 3.2vw, 2.4rem);
        line-height: 1.15;
        font-weight: 900;
        color: var(--text);
      }
      .lead{
        margin: 0 0 10px 0;
        color: var(--muted);
        font-size: 1.02rem;
        line-height: 1.55;
      }
      .list{
        color: var(--text);
        font-size: 0.98rem;
        line-height: 1.65;
      }
      .sub{
        margin-top: 12px;
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.45;
      }

      /* Inputs & boutons */
      .stTextInput input{
        background: #fff !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        border-radius: 10px !important;
        padding: 0.85rem 0.9rem !important;
      }
      .stTextInput label{
        color: var(--muted) !important;
        font-weight: 700 !important;
      }
      .stButton button{
        background: var(--blue) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.85rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }

      .section-title{
        font-weight: 900;
        color: var(--text);
        margin: 10px 0 6px 0;
      }
      .hr{
        height: 1px; background: var(--border);
        margin: 14px 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
      <div class="brand">Testamentum</div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <div class="pill">Sécurité</div>
        <div class="pill">Confidentialité</div>
        <div class="pill">Traçabilité</div>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <div class="h1">Transmettez un message vidéo à vos proches, de manière encadrée.</div>
        <div class="lead">
          Testamentum est un coffre numérique pour enregistrer un message vidéo et gérer l’accès des bénéficiaires
          selon des règles strictes (jeton, expiration, journalisation), lorsque le décès est déclaré.
        </div>

        <div class="list">
          • Accès bénéficiaires par jeton temporaire et sécurisé<br/>
          • Option de validation par notaire (workflow métier)<br/>
          • Historique des actions pour traçabilité (MVP)
        </div>

        <div class="hr"></div>

        <div class="section-title">Pourquoi c’est utile</div>
        <div class="lead">
          Pour laisser un message clair, humain et structuré, avec une transmission respectueuse et contrôlée.
        </div>

        <div class="sub">
          Version MVP : la mise en production internationale implique des exigences juridiques par pays
          (succession, notariat, protection des données).
        </div>
      </div>

      <div class="card">
        <div class="section-title">Commencer</div>
        <div class="lead">Saisissez votre adresse e-mail pour créer un compte ou vous connecter.</div>
    """,
    unsafe_allow_html=True,
)

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

if st.button("Continuer"):
    st.session_state["prefill_email"] = email.strip()
    st.switch_page("pages/1_Connexion.py")

st.markdown(
    """
        <div class="sub">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
