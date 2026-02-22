import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

st.markdown("""
<style>

/* ---------- Background ---------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.82)),
    url("https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* ---------- Base Typography ---------- */
html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: #FFFFFF;
}

section.main > div{
  max-width: 920px;
  padding-top: 2.3rem;
}

h1,h2,h3,h4,h5,h6,
.stMarkdown, .stMarkdown p,
.stCaption, .stCaption p,
label, .stTextInput label{
  color: #FFFFFF !important;
}

/* ---------- Cards ---------- */
.tm-card{
  background: rgba(15,18,22,0.86);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(22px);
  box-shadow: 0 25px 110px rgba(0,0,0,0.75);
}

.tm-card-lite{
  background: rgba(15,18,22,0.80);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 18px;
  padding: 22px;
  backdrop-filter: blur(20px);
  box-shadow: 0 18px 90px rgba(0,0,0,0.65);
}

/* ---------- Title ---------- */
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
  color: rgba(255,255,255,0.88);
}

.tm-latin{
  margin-top: 6px;
  font-size: 13px;
  font-style: italic;
  color: rgba(255,255,255,0.70);
}

.tm-h2{
  margin-top: 22px;
  font-size: 24px;
  font-weight: 650;
}

.tm-p{
  margin-top: 12px;
  color: rgba(255,255,255,0.88);
  line-height: 1.7;
  font-size: 15px;
}

.tm-bullets{
  margin-top: 16px;
  color: rgba(255,255,255,0.88);
  line-height: 1.9;
  font-size: 14px;
}

/* ---------- Chips ---------- */
.tm-chiprow{
  margin-top: 14px;
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}

.tm-chip{
  border: 1px solid rgba(255,255,255,0.18);
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 12px;
  color: rgba(255,255,255,0.85);
  background: rgba(255,255,255,0.07);
}

/* ---------- Input ---------- */
.stTextInput input{
  background: rgba(0,0,0,0.62) !important;
  border: 1px solid rgba(255,255,255,0.32) !important;
  color: #FFFFFF !important;
  border-radius: 12px !important;
  padding: 0.9rem 1rem !important;
  caret-color: #FFFFFF !important;
}

.stTextInput input::placeholder{
  color: rgba(255,255,255,0.60) !important;
}

.stTextInput input:focus{
  border: 1px solid rgba(255,255,255,0.55) !important;
  box-shadow: 0 0 0 4px rgba(255,255,255,0.16) !important;
  outline: none !important;
}

/* remove red validation */
input:invalid{
  box-shadow: none !important;
  border: 1px solid rgba(255,255,255,0.32) !important;
}

/* ---------- Symmetrical HTML Buttons ---------- */
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
  height: 52px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.28);
  background: rgba(255,255,255,0.12);
  color: #FFFFFF !important;
  text-decoration: none !important;
  font-weight: 600;
  transition: 0.2s ease;
}

.tm-btn:hover{
  background: rgba(255,255,255,0.22);
  color: #FFFFFF !important;
}

.tm-btn:visited,
.tm-btn:active,
.tm-btn:focus{
  color: #FFFFFF !important;
  text-decoration: none !important;
  outline: none;
}

.tm-btn-primary{
  background: #F3F4F6;
  color: #0b0f16 !important;
  border: none;
}

.tm-btn-primary:hover{
  background: #FFFFFF;
  color: #0b0f16 !important;
}

.tm-muted{
  margin-top: 14px;
  font-size: 12px;
  color: rgba(255,255,255,0.78);
}

@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
  .tm-card-lite{ padding: 18px; }
}

</style>
""", unsafe_allow_html=True)

# --------- Query Action ---------
qp = st.query_params
action = qp.get("action", None)

# --------- HERO ---------
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

# --------- COMMENCER ---------
st.markdown("""
<div class="tm-card-lite">
  <div class="tm-h2" style="margin-top:0;">Commencer</div>
  <div class="tm-p" style="margin-top:6px;">
    Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
  </div>
</div>
""", unsafe_allow_html=True)

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

st.markdown("""
<div class="tm-actions">
  <a class="tm-btn tm-btn-primary" href="?action=continue">Continuer</a>
  <a class="tm-btn" href="?action=benef">Accès bénéficiaire</a>
</div>
""", unsafe_allow_html=True)

if action == "continue":
    st.success("Redirection (MVP)")
elif action == "benef":
    st.info("Accès bénéficiaire (MVP)")

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True
)
