import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

# =========================================================
# THEME : noir sobre + image non religieuse + lisible mobile
# =========================================================
st.markdown("""
<style>

/* --------- Background image (non religieux) ---------
   Thème : mémoire / deuil / recueillement (silhouette, brume, cimetière flou, nature)
*/
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.92)),
    url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* --------- Variables --------- */
:root{
  --card: rgba(15, 18, 22, 0.82);
  --border: rgba(255,255,255,0.10);
  --text: #F7F8FA;       /* texte principal : très lisible */
  --muted: #C6CBD3;      /* texte secondaire : clair */
  --muted2: #9AA3AF;     /* encore plus discret, mais lisible */
  --accent: #D6D9DE;     /* gris “silver” */
  --accent2: #B9C0CA;    /* hover */
}

/* --------- Base --------- */
html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}

section.main > div{
  max-width: 920px;
  padding-top: 2.2rem;
}

/* --------- Card --------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(14px);
  box-shadow: 0 18px 70px rgba(0,0,0,0.55);
  animation: fadeIn 0.55s ease-out;
}

@keyframes fadeIn{
  from {opacity:0; transform: translateY(10px);}
  to {opacity:1; transform: translateY(0);}
}

/* --------- Typo --------- */
.tm-title{
  font-size: 44px;
  margin: 0;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.02;
  /* dégradé subtil sur le texte */
  background: linear-gradient(90deg, #FFFFFF 0%, #D7DCE3 45%, #FFFFFF 100%);
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
  margin-top: 18px;
  font-size: 24px;
  font-weight: 650;
  color: var(--text);
}

.tm-p{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.65;
  font-size: 15px;
}

.tm-bullets{
  margin-top: 12px;
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
  background: rgba(255,255,255,0.04);
}

/* --------- Inputs (no red, strong readability) --------- */
.stTextInput label{
  color: var(--muted) !important;
}

.stTextInput input{
  background: rgba(10,12,15,0.85) !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.75rem 0.9rem !important;
  caret-color: var(--text) !important;
}

.stTextInput input::placeholder{
  color: rgba(198,203,211,0.55) !important;
}

.stTextInput input:focus{
  border: 1px solid var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(214,217,222,0.15) !important;
  outline: none !important;
}

/* supprime les styles “invalid” (rouge) du navigateur */
input:invalid, textarea:invalid{
  box-shadow: none !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
}

/* --------- Buttons (silver, no blue/red) --------- */
.stButton button{
  width: 100%;
  border-radius: 999px !important;
  padding: 0.85rem 1.1rem !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
  background: rgba(255,255,255,0.06) !important;
  color: var(--text) !important;
  font-weight: 600 !important;
}

.stButton button:hover{
  background: rgba(255,255,255,0.12) !important;
}

.tm-primary button{
  background: var(--accent) !important;
  color: #0b0f14 !important;
  border: none !important;
}

.tm-primary button:hover{
  background: var(--accent2) !important;
}

.tm-muted{
  margin-top: 12px;
  font-size: 12px;
  color: rgba(198,203,211,0.70);
}

/* --------- Mobile spacing --------- */
@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="tm-card">
  <h1 class="tm-title">Testamentum</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>

  <div class="tm-chiprow">
    <span class="tm-chip">LegalTech</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
    <span class="tm-chip">Accès contrôlé</span>
  </div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    Le service est conçu pour une transmission respectueuse, avec une gouvernance adaptée aux enjeux successoraux.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale (selon juridiction)<br/>
    • Journalisation des actions pour la traçabilité (MVP)
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================================================
# COMMENCER
# =========================================================
st.markdown("## Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

c1, c2 = st.columns([1, 1])

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Continuer"):
        st.success("Redirection (MVP)")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    if st.button("Accès bénéficiaire"):
        st.info("Accès bénéficiaire (MVP)")

st.markdown('<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>', unsafe_allow_html=True)
