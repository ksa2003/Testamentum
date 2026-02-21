import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ------------------------------------------------------------
# THEME: Legal Tech / Fonds d'investissement (noir + argent)
# ------------------------------------------------------------
st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}
      [data-testid="stSidebar"] {display:none;}

      :root{
        --bg:#000000;

        /* Surfaces "X-like" */
        --surface:#0b0f14;
        --surface2:#0f1419;

        /* Bordures / texte */
        --border:#2f3336;
        --text:#e7e9ea;
        --muted:#8b98a5;

        /* Accent "deuil" : argent / gris froid, pas de bleu */
        --accent:#c7cbd1;         /* argent clair */
        --accent2:#9aa3ad;        /* argent plus sombre */
        --accentText:#0b0f14;     /* texte sur bouton */

        --shadow: 0 18px 60px rgba(0,0,0,.55);
      }

      .stApp{ background: var(--bg) !important; }

      section.main > div{
        max-width: 980px !important;
        padding-top: 1.2rem !important;
      }

      /* Inputs lisibles */
      .stTextInput input{
        background: var(--surface2) !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        caret-color: var(--text) !important;
        border-radius: 14px !important;
        padding: 0.95rem 1rem !important;
      }
      .stTextInput input::placeholder{
        color: var(--muted) !important;
      }
      .stTextInput label{
        color: var(--muted) !important;
        font-weight: 800 !important;
      }

      /* Bouton principal (sans bleu) */
      .stButton button{
        background: linear-gradient(180deg, var(--accent) 0%, var(--accent2) 100%) !important;
        color: var(--accentText) !important;
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
        color: var(--muted);
        font-size: 0.86rem;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# HERO: marque forte + monogramme + gradient + latin + fade-in
# ------------------------------------------------------------
hero = """
<style>
  /* Fade-in doux pour le hero */
  @keyframes fadeUp {
    0% { opacity:0; transform: translateY(10px); }
    100% { opacity:1; transform: translateY(0); }
  }
  .tm-hero {
    animation: fadeUp .55s ease-out both;
  }

  /* Logo monogramme T */
  .tm-mark {
    display:flex;
    align-items:center;
    gap:14px;
  }
  .tm-logo {
    width:44px;
    height:44px;
    border-radius:14px;
    border:1px solid rgba(255,255,255,0.14);
    background: radial-gradient(120px circle at 25% 15%, rgba(231,233,234,0.12), rgba(255,255,255,0.02) 42%),
                linear-gradient(180deg, rgba(15,20,25,0.95), rgba(11,15,20,0.95));
    box-shadow: 0 14px 40px rgba(0,0,0,.55);
    display:flex;
    align-items:center;
    justify-content:center;
    position: relative;
    overflow:hidden;
  }
  .tm-logo::after{
    content:"";
    position:absolute;
    inset:-60px;
    background: radial-gradient(160px circle at 50% 20%, rgba(199,203,209,0.18), transparent 55%);
    transform: rotate(12deg);
  }
  .tm-logo span{
    position:relative;
    font-weight:1000;
    letter-spacing:0.02em;
    color: rgba(231,233,234,0.95);
    font-size: 1.25rem;
    line-height: 1;
  }

  /* Dégradé subtil sur le nom */
  .tm-brand {
    font-size: clamp(2.7rem, 6vw, 4.0rem);
    font-weight: 1000;
    letter-spacing: 0.02em;
    line-height: 1;
    margin: 0;
    background: linear-gradient(90deg, #ffffff 0%, #d7dbe0 35%, #aeb6bf 70%, #ffffff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
  }

  .tm-sub {
    margin-top: 6px;
    color: rgba(139,152,165,0.95);
    font-weight: 650;
    font-size: 1.02rem;
  }

  .tm-latin {
    margin-top: 10px;
    color: rgba(139,152,165,0.85);
    font-size: 0.95rem;
    font-style: italic;
    letter-spacing: 0.01em;
  }

  .tm-card {
    border: 1px solid #2f3336;
    background: rgba(0,0,0,1);
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 18px 60px rgba(0,0,0,.55);
  }

  .tm-title {
    margin-top: 20px;
    color: #e7e9ea;
    font-weight: 950;
    font-size: clamp(1.5rem, 3.6vw, 2.25rem);
    line-height: 1.16;
  }

  .tm-body {
    margin-top: 12px;
    color: rgba(231,233,234,0.92);
    line-height: 1.68;
    font-size: 1.04rem;
    max-width: 72ch;
  }

  .tm-bullets {
    margin-top: 14px;
    color: rgba(231,233,234,0.86);
    line-height: 1.75;
    font-size: 1.0rem;
  }

  .tm-pills {
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    justify-content:flex-end;
  }
  .tm-pill{
    border:1px solid #2f3336;
    background: rgba(255,255,255,0.02);
    padding: 6px 12px;
    border-radius: 999px;
    color: #8b98a5;
    font-weight: 850;
    font-size: .88rem;
  }

  .tm-top {
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap: 14px;
    flex-wrap:wrap;
  }

  /* Petit bandeau "legal tech" discret */
  .tm-tag {
    margin-top: 10px;
    display:inline-flex;
    gap:10px;
    align-items:center;
    border:1px solid rgba(255,255,255,0.10);
    border-radius: 999px;
    padding: 6px 12px;
    color: rgba(231,233,234,0.88);
    font-size: .88rem;
    background: rgba(255,255,255,0.02);
  }
  .tm-dot{
    width:6px;height:6px;border-radius:999px;background: rgba(199,203,209,0.95);
    box-shadow: 0 0 0 4px rgba(199,203,209,0.12);
  }

</style>

<div class="tm-hero tm-card">
  <div class="tm-top">
    <div>
      <div class="tm-mark">
        <div class="tm-logo"><span>T</span></div>
        <div>
          <div class="tm-brand">Testamentum</div>
          <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
          <div class="tm-latin">Verba manent. Memoria custoditur.</div>
          <div class="tm-tag"><span class="tm-dot"></span> Legal Tech • Confidentialité • Traçabilité</div>
        </div>
      </div>
    </div>
    <div class="tm-pills">
      <span class="tm-pill">Sécurité</span>
      <span class="tm-pill">Confidentialité</span>
      <span class="tm-pill">Audit</span>
    </div>
  </div>

  <div class="tm-title">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-body">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
    lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse, avec des règles strictes
    et une gouvernance adaptée aux enjeux successoraux.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale (workflow métier, selon juridiction)<br/>
    • Journalisation des actions pour la traçabilité (MVP)
  </div>
</div>
"""

components.html(hero, height=460, scrolling=False)

st.write("")

# ------------------------------------------------------------
# SECTION COMMENCER
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
