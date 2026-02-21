import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

# =========================================================
# THEME GRIS PREMIUM + FOND IMAGE
# =========================================================
st.markdown("""
<style>

/* ---------- Background image ---------- */
.stApp {
  background: 
    linear-gradient(rgba(242,244,247,0.88), rgba(242,244,247,0.88)),
    url("https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* ---------- Variables ---------- */
:root{
  --card:#FFFFFF;
  --border:#E4E7EC;
  --text:#1F2937;
  --muted:#667085;
  --accent:#475467;
  --accentSoft:#D0D5DD;
}

/* ---------- Layout ---------- */
section.main > div{
  max-width: 900px;
  padding-top: 2rem;
}

/* ---------- Card ---------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 28px;
  box-shadow: 0 8px 30px rgba(16,24,40,0.08);
  animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn{
  from {opacity:0; transform: translateY(6px);}
  to {opacity:1; transform: translateY(0);}
}

.tm-title{
  font-size: 42px;
  margin: 0;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text);
}

.tm-sub{
  margin-top: 6px;
  font-size: 14px;
  color: var(--muted);
}

.tm-latin{
  margin-top: 4px;
  font-size: 13px;
  font-style: italic;
  color: #98A2B3;
}

.tm-h2{
  margin-top: 18px;
  font-size: 24px;
  font-weight: 600;
}

.tm-p{
  margin-top: 8px;
  color: var(--muted);
  line-height: 1.6;
}

.tm-bullets{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.7;
}

/* ---------- Chips ---------- */
.tm-chiprow{
  margin-top: 12px;
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}

.tm-chip{
  background: #F9FAFB;
  border: 1px solid var(--border);
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
  color: var(--muted);
}

/* ---------- Inputs ---------- */
.stTextInput input{
  background: #FFFFFF !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: 10px !important;
}

.stTextInput input:focus{
  border: 1px solid var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(71,84,103,0.12) !important;
  outline: none !important;
}

input:invalid{
  border: 1px solid var(--border) !important;
  box-shadow: none !important;
}

/* ---------- Buttons ---------- */
.stButton button{
  border-radius: 999px !important;
  padding: 0.7rem 1.2rem !important;
  border: 1px solid var(--border) !important;
  background: var(--accentSoft) !important;
  color: var(--text) !important;
  font-weight: 600 !important;
}

.stButton button:hover{
  background: #E4E7EC !important;
}

.tm-primary button{
  background: var(--accent) !important;
  color: #FFFFFF !important;
  border: none !important;
}

.tm-muted{
  margin-top: 10px;
  font-size: 12px;
  color: var(--muted);
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
    Le service est conçu pour une transmission respectueuse, avec des règles strictes.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale (workflow métier)<br/>
    • Journalisation des actions pour la traçabilité
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
