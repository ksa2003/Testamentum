import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

# ------------------ STYLE GLOBAL ------------------
st.markdown("""
<style>

/* --------- Background --------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.80)),
    url("https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* --------- Variables --------- */
:root{
  --card: rgba(15,18,22,0.78);
  --border: rgba(255,255,255,0.12);
  --text: #FFFFFF;
  --muted: rgba(255,255,255,0.82);
  --muted2: rgba(255,255,255,0.70);
  --focus: rgba(229,231,235,0.95);
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
  padding: 26px;
  backdrop-filter: blur(20px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.7);
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn{
  from {opacity:0; transform: translateY(12px);}
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
  background: rgba(255,255,255,0.05);
}

/* --------- Inputs --------- */
.stTextInput label{
  color: var(--muted) !important;
}

.stTextInput input{
  background: rgba(0,0,0,0.45) !important;
  border: 1px solid rgba(255,255,255,0.25) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.8rem 1rem !important;
  caret-color: var(--text) !important;
}

.stTextInput input::placeholder{
  color: rgba(255,255,255,0.55) !important;
}

.stTextInput input:focus{
  border: 1px solid var(--focus) !important;
  box-shadow: 0 0 0 3px rgba(229,231,235,0.18) !important;
  outline: none !important;
}

/* remove red invalid */
input:invalid{
  border: 1px solid rgba(255,255,255,0.25) !important;
  box-shadow: none !important;
}

/* --------- CTA GRID (alignement parfait) --------- */
.tm-cta{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 10px;
  align-items: stretch;
}

.tm-btn{
  width: 100%;
  height: 52px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.25);
  background: rgba(255,255,255,0.10);
  color: #fff;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
}

.tm-btn:hover{
  background: rgba(255,255,255,0.18);
}

.tm-btn:focus{
  outline: none;
  box-shadow: 0 0 0 3px rgba(229,231,235,0.18);
}

.tm-btn-primary{
  background: rgba(229,231,235,0.92);
  color: #0B0F14;
  border: none;
}

.tm-btn-primary:hover{
  background: rgba(243,244,246,0.96);
}

@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
  .tm-cta{ grid-template-columns: 1fr 1fr; } /* garde 2 colonnes, alignées */
}

.tm-muted{
  margin-top: 12px;
  font-size: 12px;
  color: rgba(255,255,255,0.70);
}

</style>
""", unsafe_allow_html=True)

# ------------------ HERO ------------------
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

# ------------------ COMMENCER ------------------
st.markdown('<div class="tm-card">', unsafe_allow_html=True)
st.markdown("## Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

# Boutons HTML alignés (pas de st.columns)
st.markdown(
    f"""
<div class="tm-cta">
  <form action="/Connexion" method="get">
    <input type="hidden" name="email" value="{email}">
    <button class="tm-btn tm-btn-primary" type="submit">Continuer</button>
  </form>

  <form action="/Acces_beneficiaire" method="get">
    <button class="tm-btn" type="submit">Accès bénéficiaire</button>
  </form>
</div>

<div class="tm-muted">
  En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.
</div>
""",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)
