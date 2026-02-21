import streamlit as st

st.set_page_config(
    page_title="Testamentum",
    page_icon="⚖️",
    layout="centered"
)

st.markdown("""
<style>

/* ===========================
   BACKGROUND — HORIZON SOBRE
   =========================== */

.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.78), rgba(0,0,0,0.85)),
    url("https://images.unsplash.com/photo-1496307653780-42ee777d4833?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* vignette légère */
.stApp::after{
  content:"";
  position:fixed;
  inset:0;
  background: radial-gradient(circle at center,
              rgba(0,0,0,0.2) 0%,
              rgba(0,0,0,0.65) 85%);
  pointer-events:none;
}

/* ===========================
   VARIABLES
   =========================== */

:root{
  --card: rgba(22,26,32,0.78);
  --border: rgba(255,255,255,0.12);
  --text: #FFFFFF;
  --muted: #E6E9EE;
  --muted2: #AEB7C2;
  --accent: #F2F4F7;
}

/* ===========================
   BASE
   =========================== */

html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}

section.main > div{
  max-width: 920px;
  padding-top: 2.5rem;
}

/* ===========================
   HERO CARD
   =========================== */

.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 32px;
  backdrop-filter: blur(20px);
  box-shadow: 0 30px 120px rgba(0,0,0,0.7);
}

.tm-title{
  font-size: 50px;
  font-weight: 700;
  letter-spacing: -0.03em;
  margin: 0;
  background: linear-gradient(90deg,#FFFFFF,#DDE3EA,#FFFFFF);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tm-sub{
  margin-top: 12px;
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
  margin-top: 26px;
  font-size: 24px;
  font-weight: 600;
}

.tm-p{
  margin-top: 12px;
  line-height: 1.7;
  font-size: 15px;
  color: var(--muted);
}

.tm-bullets{
  margin-top: 18px;
  line-height: 1.9;
  font-size: 14px;
  color: var(--muted);
}

/* ===========================
   INPUT
   =========================== */

.stTextInput input{
  background: rgba(0,0,0,0.45) !important;
  border: 1px solid rgba(255,255,255,0.3) !important;
  color: white !important;
  border-radius: 16px !important;
  padding: 1rem !important;
}

.stTextInput input:focus{
  border: 1px solid white !important;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.15) !important;
}

/* ===========================
   BUTTONS
   =========================== */

.stButton button{
  width: 100%;
  border-radius: 999px !important;
  padding: 1rem !important;
  border: 1px solid rgba(255,255,255,0.3) !important;
  background: rgba(255,255,255,0.12) !important;
  color: white !important;
  font-weight: 600 !important;
}

.stButton button:hover{
  background: rgba(255,255,255,0.22) !important;
}

.tm-muted{
  margin-top: 15px;
  font-size: 12px;
  color: rgba(255,255,255,0.7);
}

@media (max-width:520px){
  .tm-title{ font-size: 40px; }
}

</style>
""", unsafe_allow_html=True)

# ===========================
# HERO
# ===========================

st.markdown("""
<div class="tm-card">
  <h1 class="tm-title">Testamentum</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès
    des bénéficiaires lorsque le décès est déclaré. 
    Le service est conçu pour une transmission respectueuse, sécurisée et conforme aux standards internationaux.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton sécurisé<br/>
    • Validation notariale selon juridiction<br/>
    • Journalisation complète des actions
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===========================
# CONNEXION
# ===========================

st.markdown("## Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

col1, col2 = st.columns(2)

with col1:
    if st.button("Continuer"):
        st.success("Redirection (MVP)")

with col2:
    if st.button("Accès bénéficiaire"):
        st.info("Accès bénéficiaire (MVP)")

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True
)
