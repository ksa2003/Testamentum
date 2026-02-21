import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

st.markdown("""
<style>

/* --------- Background : Forêt / Cimetière brumeux --------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.65)),
    url("https://images.unsplash.com/photo-1475189778702-5ec9941484ae?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* Vignette subtile */
.stApp::after{
  content: "";
  position: fixed;
  inset: 0;
  background: radial-gradient(circle at center, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.55) 85%);
  pointer-events: none;
}

/* --------- Variables --------- */
:root{
  --card: rgba(18,22,26,0.78);
  --border: rgba(255,255,255,0.15);
  --text: #FFFFFF;
  --muted: #E2E5EA;
  --muted2: #B7BDC7;
  --accent: #F0F2F5;
  --accentHover: #FFFFFF;
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

/* --------- Card --------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 28px;
  backdrop-filter: blur(16px);
  box-shadow: 0 20px 80px rgba(0,0,0,0.6);
  animation: fadeIn 0.5s ease-out;
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
  background: linear-gradient(90deg, #FFFFFF 0%, #EAECEF 50%, #FFFFFF 100%);
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
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.65;
  font-size: 15px;
}

.tm-bullets{
  margin-top: 14px;
  color: var(--muted);
  line-height: 1.85;
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
  background: rgba(255,255,255,0.06);
}

/* --------- Inputs --------- */
.stTextInput label{
  color: var(--muted) !important;
}

.stTextInput input{
  background: rgba(0,0,0,0.45) !important;
  border: 1px solid rgba(255,255,255,0.30) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.8rem 1rem !important;
  caret-color: var(--text) !important;
}

.stTextInput input::placeholder{
  color: rgba(255,255,255,0.55) !important;
}

.stTextInput input:focus{
  border: 1px solid var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.15) !important;
  outline: none !important;
}

/* remove red invalid */
input:invalid{
  border: 1px solid rgba(255,255,255,0.30) !important;
  box-shadow: none !important;
}

/* --------- Buttons --------- */
.stButton button{
  width: 100%;
  border-radius: 999px !important;
  padding: 0.9rem 1.2rem !important;
  border: 1px solid rgba(255,255,255,0.30) !important;
  background: rgba(255,255,255,0.12) !important;
  color: var(--text) !important;
  font-weight: 600 !important;
}

.stButton button:hover{
  background: rgba(255,255,255,0.22) !important;
}

.tm-primary button{
  background: var(--accent) !important;
  color: black !important;
  border: none !important;
}

.tm-primary button:hover{
  background: var(--accentHover) !important;
}

.tm-muted{
  margin-top: 12px;
  font-size: 12px;
  color: rgba(255,255,255,0.70);
}

@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
}

</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
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
""", unsafe_allow_html=True)

st.write("")

# COMMENCER
st.markdown("## Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Continuer"):
        st.success("Redirection (MVP)")
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    if st.button("Accès bénéficiaire"):
        st.info("Accès bénéficiaire (MVP)")

st.markdown('<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>', unsafe_allow_html=True)
