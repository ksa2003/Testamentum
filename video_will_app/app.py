import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

# =========================================================
# THEME NOIR + IMAGE RECUEILLEMENT
# =========================================================
st.markdown("""
<style>

/* --------- Background image (recueillement) --------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
    url("https://images.unsplash.com/photo-1504052434569-70ad5836ab65?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* --------- Variables --------- */
:root{
  --card: rgba(15,15,18,0.75);
  --border: rgba(255,255,255,0.08);
  --text: #F2F4F7;
  --muted: #A0A6B0;
  --accent: #C7CBD1;
}

/* --------- Layout --------- */
section.main > div{
  max-width: 900px;
  padding-top: 2.5rem;
}

html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}

/* --------- Card --------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 30px;
  backdrop-filter: blur(12px);
  box-shadow: 0 12px 50px rgba(0,0,0,0.6);
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn{
  from {opacity:0; transform: translateY(8px);}
  to {opacity:1; transform: translateY(0);}
}

.tm-title{
  font-size: 44px;
  margin: 0;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.tm-sub{
  margin-top: 8px;
  font-size: 14px;
  color: var(--muted);
}

.tm-latin{
  margin-top: 6px;
  font-size: 13px;
  font-style: italic;
  color: #8A9099;
}

.tm-h2{
  margin-top: 22px;
  font-size: 24px;
  font-weight: 500;
}

.tm-p{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.6;
}

.tm-bullets{
  margin-top: 14px;
  color: var(--muted);
  line-height: 1.8;
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
  background: rgba(255,255,255,0.03);
}

/* --------- Inputs --------- */
.stTextInput input{
  background: rgba(20,20,25,0.85) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 10px !important;
}

.stTextInput input:focus{
  border: 1px solid var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(199,203,209,0.15) !important;
  outline: none !important;
}

/* Supprime rouge */
input:invalid{
  border: 1px solid var(--border) !important;
  box-shadow: none !important;
}

/* --------- Buttons --------- */
.stButton button{
  border-radius: 999px !important;
  padding: 0.7rem 1.4rem !important;
  border: 1px solid var(--border) !important;
  background: rgba(255,255,255,0.08) !important;
  color: var(--text) !important;
  font-weight: 500 !important;
}

.stButton button:hover{
  background: rgba(255,255,255,0.15) !important;
}

.tm-primary button{
  background: var(--accent) !important;
  color: black !important;
  border: none !important;
}

.tm-muted{
  margin-top: 12px;
  font-size: 12px;
  color: #7B818C;
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
    <span class="tm-chip">Mémoire</span>
    <span class="tm-chip">Transmission</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Accès contrôlé</span>
  </div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    Le service est conçu pour une transmission respectueuse, avec des règles strictes.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale<br/>
    • Journalisation des actions
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

col1, col2 = st.columns([1,1])

with col1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Continuer"):
        st.success("Redirection (MVP)")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if st.button("Accès bénéficiaire"):
        st.info("Accès bénéficiaire (MVP)")

st.markdown('<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>', unsafe_allow_html=True)
