import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ------------------------------------------------------------
# THEME: Legal Tech / Premium sombre (noir + gris froids + argent)
# ------------------------------------------------------------
st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}
      [data-testid="stSidebar"] {display:none;}

      :root{
        /* Fond */
        --bg:#000000;

        /* Surfaces */
        --surface:#0b0f14;     /* carte */
        --surface2:#0f1419;    /* inputs */

        /* Bordures */
        --border:#2f3336;
        --borderSoft:rgba(255,255,255,0.10);

        /* Textes (nuancés, pas seulement blanc) */
        --text:#e7e9ea;        /* principal */
        --text2:#d3d7dd;       /* secondaire clair */
        --muted:#8b98a5;       /* infos */
        --muted2:#6b7785;      /* micro-texte */

        /* Accent deuil (argent froid) */
        --accent:#c7cbd1;
        --accent2:#9aa3ad;
        --accent3:#5c6673;     /* gris acier */

        --shadow: 0 18px 60px rgba(0,0,0,.55);
      }

      .stApp{
        background:
          radial-gradient(900px circle at 12% 8%, rgba(199,203,209,0.06), transparent 45%),
          radial-gradient(700px circle at 88% 12%, rgba(155,165,173,0.05), transparent 42%),
          radial-gradient(650px circle at 50% 95%, rgba(92,102,115,0.05), transparent 48%),
          var(--bg) !important;
      }

      section.main > div{
        max-width: 1040px !important;
        padding-top: 1.1rem !important;
        padding-left: 0.4rem !important;
        padding-right: 0.4rem !important;
      }

      /* Inputs lisibles */
      .stTextInput input{
        background: linear-gradient(180deg, rgba(15,20,25,0.98), rgba(11,15,20,0.98)) !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        caret-color: var(--text) !important;
        border-radius: 14px !important;
        padding: 0.95rem 1rem !important;
      }
      .stTextInput input::placeholder{
        color: rgba(139,152,165,0.85) !important;
      }
      .stTextInput label{
        color: rgba(139,152,165,0.95) !important;
        font-weight: 800 !important;
      }

      /* Bouton principal (sans bleu) */
      .stButton button{
        background: linear-gradient(180deg, rgba(199,203,209,0.98) 0%, rgba(154,163,173,0.98) 100%) !important;
        color: #0b0f14 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 999px !important;
        padding: 0.9rem 1rem !important;
        font-weight: 950 !important;
        width: 100%;
        box-shadow: 0 12px 28px rgba(0,0,0,.45);
      }
      .stButton button:hover{
        filter: brightness(1.05);
      }

      .fine{
        color: rgba(107,119,133,0.92);
        font-size: 0.86rem;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HERO: marque gauche + dégradé subtil + latin + fade-in
# ------------------------------------------------------------
hero = """
<style>
  @keyframes fadeUp {
    0% { opacity:0; transform: translateY(10px); }
    100% { opacity:1; transform: translateY(0); }
  }
  .tm-hero { animation: fadeUp .55s ease-out both; }

  .tm-card {
    border: 1px solid rgba(255,255,255,0.10);
    background: rgba(15,20,25,0.68);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 26px 24px;
    box-shadow: 0 18px 60px rgba(0,0,0,.55);
  }

  .tm-top {
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap: 14px;
    flex-wrap:wrap;
  }

  /* Brand: plus à gauche, plus présent */
  .tm-brand {
    font-size: clamp(2.9rem, 7vw, 4.2rem);
    font-weight: 1000;
    letter-spacing: 0.02em;
    line-height: 1.02;
    margin: 0;
    text-align: left;
    background: linear-gradient(90deg,
      rgba(255,255,255,0.98) 0%,
      rgba(211,215,221,0.96) 30%,
      rgba(199,203,209,0.92) 55%,
      rgba(255,255,255,0.96) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }

  .tm-sub {
    margin-top: 8px;
    color: rgba(211,215,221,0.92);
    font-weight: 650;
    font-size: 1.02rem;
  }

  .tm-latin {
    margin-top: 10px;
    color: rgba(139,152,165,0.88);
    font-size: 0.95rem;
    font-style: italic;
    letter-spacing: 0.01em;
  }

  .tm-title {
    margin-top: 18px;
    color: rgba(231,233,234,0.98);
    font-weight: 950;
    font-size: clamp(1.55rem, 3.9vw, 2.35rem);
    line-height: 1.16;
  }

  /* Texte non coupé + largeur confortable */
  .tm-body {
    margin-top: 12px;
    color: rgba(211,215,221,0.92);
    line-height: 1.72;
    font-size: 1.05rem;
    max-width: 78ch;
  }

  .tm-bullets {
    margin-top: 14px;
    color: rgba(231,233,234,0.86);
    line-height: 1.78;
    font-size: 1.0rem;
  }

  .tm-pills {
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    justify-content:flex-end;
  }
  .tm-pill{
    border:1px solid rgba(255,255,255,0.10);
    background: rgba(0,0,0,0.20);
    padding: 6px 12px;
    border-radius: 999px;
    color: rgba(139,152,165,0.95);
    font-weight: 850;
    font-size: .88rem;
  }

  .tm-tag {
    margin-top: 10px;
    display:inline-flex;
    gap:10px;
    align-items:center;
    border:1px solid rgba(255,255,255,0.10);
    border-radius: 999px;
    padding: 6px 12px;
    color: rgba(211,215,221,0.92);
    font-size: .88rem;
    background: rgba(0,0,0,0.18);
  }
  .tm-dot{
    width:6px;height:6px;border-radius:999px;
    background: rgba(199,203,209,0.95);
    box-shadow: 0 0 0 4px rgba(199,203,209,0.10);
  }

</style>

<div class="tm-hero tm-card">
  <div class="tm-top">
    <div style="min-width: 260px;">
      <div class="tm-brand">Testamentum</div>
      <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
      <div class="tm-latin">Verba manent. Memoria custoditur.</div>
      <div class="tm-tag"><span class="tm-dot"></span> Legal Tech • Confidentialité • Traçabilité</div>
    </div>
    <div class="tm-pills">
      <span class="tm-pill">Sécurité</span>
      <span class="tm-pill">Confidentialité</span>
      <span class="tm-pill">Audit</span>
    </div>
  </div>

  <div class="tm-title">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-body">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    Le service est conçu pour une transmission respectueuse, avec des règles strictes et une gouvernance adaptée aux enjeux successoraux.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale (workflow métier, selon juridiction)<br/>
    • Journalisation des actions pour la traçabilité (MVP)
  </div>
</div>
"""
# Plus haut pour éviter toute coupe sur mobile
components.html(hero, height=560, scrolling=False)

st.write("")

# ------------------------------------------------------------
# SECTION COMMENCER
# ------------------------------------------------------------
st.subheader("Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

if st.button("Continuer"):
    st.session_state["prefill_email"] = (email or "").strip()
    # Page de connexion : adaptez au nom réel de votre fichier
    st.switch_page("pages/1_Connexion.py")

st.markdown(
    '<div class="fine">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
    unsafe_allow_html=True,
)
