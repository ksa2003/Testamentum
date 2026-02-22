import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

# --------- CSS ---------
st.markdown(
    """
<style>
/* --------- Background --------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.82)),
    url("https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* --------- Variables --------- */
:root{
  --card: rgba(15,18,22,0.86);
  --card2: rgba(15,18,22,0.80);
  --border: rgba(255,255,255,0.18);

  --text: #FFFFFF;
  --muted: rgba(255,255,255,0.90);
  --muted2: rgba(255,255,255,0.74);

  --btn: rgba(255,255,255,0.12);
  --btnHover: rgba(255,255,255,0.22);
  --btnBorder: rgba(255,255,255,0.28);

  --primaryBg: #F3F4F6;
  --primaryHover: #FFFFFF;
  --primaryText: #0b0f16;
}

/* --------- Base --------- */
html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}

section.main > div{
  max-width: 920px;
  padding-top: 2.3rem;
}

/* Force text color everywhere */
h1,h2,h3,h4,h5,h6,
.stMarkdown, .stMarkdown p,
.stCaption, .stCaption p,
label, .stTextInput label,
[data-testid="stMarkdownContainer"] p{
  color: var(--text) !important;
}
.stCaption, .stCaption p{ color: var(--muted2) !important; }

/* --------- Cards --------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(22px);
  box-shadow: 0 25px 110px rgba(0,0,0,0.75);
  animation: fadeIn 0.55s ease-out;
}
.tm-card-lite{
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px;
  backdrop-filter: blur(20px);
  box-shadow: 0 18px 90px rgba(0,0,0,0.65);
  animation: fadeIn 0.55s ease-out;
}
@keyframes fadeIn{
  from {opacity:0; transform: translateY(10px);}
  to {opacity:1; transform: translateY(0);}
}

/* --------- Typography --------- */
.tm-title{
  font-size: 46px;
  margin: 0;
  font-weight: 700;
  letter-spacing: -0.03em;
  background: linear-gradient(90deg, #FFFFFF 0%, #E5E7EB 50%, #FFFFFF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.tm-sub{
  margin-top: 10px;
  font-size: 14px;
  color: var(--muted);
}
.tm-latin{
  margin-top: 6px;
  font-size: 13px;
  font-style: italic;
  color: var(--muted2);
}
.tm-h2{
  margin-top: 22px;
  font-size: 24px;
  font-weight: 650;
}
.tm-p{
  margin-top: 12px;
  color: var(--muted);
  line-height: 1.7;
  font-size: 15px;
}
.tm-bullets{
  margin-top: 16px;
  color: var(--muted);
  line-height: 1.9;
  font-size: 14px;
}

/* --------- Chips --------- */
.tm-chiprow{
  margin-top: 14px;
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}
.tm-chip{
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 12px;
  color: var(--muted);
  background: rgba(255,255,255,0.07);
}

/* --------- Inputs --------- */
.stTextInput label{
  color: var(--muted) !important;
  font-weight: 600 !important;
}
.stTextInput input{
  background: rgba(0,0,0,0.62) !important;
  border: 1px solid rgba(255,255,255,0.32) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.9rem 1rem !important;
  caret-color: var(--text) !important;
}
.stTextInput input::placeholder{
  color: rgba(255,255,255,0.60) !important;
}
.stTextInput input:focus{
  border: 1px solid rgba(255,255,255,0.55) !important;
  box-shadow: 0 0 0 4px rgba(255,255,255,0.16) !important;
  outline: none !important;
}
input:invalid{
  border: 1px solid rgba(255,255,255,0.32) !important;
  box-shadow: none !important;
}

/* --------- Pixel-perfect button row (HTML, not Streamlit buttons) --------- */
.tm-actions{
  display:flex;
  gap: 14px;
  width:100%;
  margin-top: 14px;
}
.tm-btn{
  flex:1;
  display:flex;
  align-items:center;
  justify-content:center;
  height: 52px;             /* SAME HEIGHT ALWAYS */
  border-radius: 999px;
  border: 1px solid var(--btnBorder);
  background: var(--btn);
  color: var(--text);
  font-weight: 650;
  text-decoration: none;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
}
.tm-btn:hover{ background: var(--btnHover); }

.tm-btn-primary{
  background: var(--primaryBg);
  color: var(--primaryText);
  border: none;
}
.tm-btn-primary:hover{ background: var(--primaryHover); }

.tm-muted{
  margin-top: 14px;
  font-size: 12px;
  color: rgba(255,255,255,0.78);
}

@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
  .tm-card-lite{ padding: 18px; }
  .tm-actions{ gap: 10px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# --------- Actions (via query params) ---------
# Clicking the HTML links reloads the page with ?action=continue or ?action=benef
qp = st.query_params
action = qp.get("action", None)

# HERO
st.markdown(
    """
<div class="tm-card">
  <h1 class="tm-title">Testamentum</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>

  <div class="tm-chiprow">
    <span class="tm-chip">Mémoire</span>
    <span class="tm-chip">Transmission</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
  </div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    Le service est conçu pour une transmission respectueuse et structurée.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale<br/>
    • Journalisation des actions
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# COMMENCER (buttons at the bottom of the section)
st.markdown(
    """
<div class="tm-card-lite">
  <div class="tm-h2" style="margin-top:0;">Commencer</div>
  <div class="tm-p" style="margin-top:6px;">
    Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

# Pixel-perfect row of actions (HTML flex)
st.markdown(
    """
<div class="tm-actions">
  <a class="tm-btn tm-btn-primary" href="?action=continue">Continuer</a>
  <a class="tm-btn" href="?action=benef">Accès bénéficiaire</a>
</div>
""",
    unsafe_allow_html=True,
)

# Feedback after click
if action == "continue":
    st.success("Redirection (MVP)")
    # Optionnel: nettoyer l'URL après affichage
    # st.query_params.clear()
elif action == "benef":
    st.info("Accès bénéficiaire (MVP)")
    # st.query_params.clear()

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True,
)
