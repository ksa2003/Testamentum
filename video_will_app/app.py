import streamlit as st

# ============================================================
# Testamentum — Landing (MVP)
# Thème sombre + photo "souvenir / départ" (avec silhouette)
# UI type "X-card" + boutons parfaitement alignés
# ============================================================

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

st.markdown(
    """
<style>
/* --------- Background --------- */
.stApp {
  background:
    linear-gradient(rgba(0,0,0,0.70), rgba(0,0,0,0.78)),
    url("https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* --------- Variables --------- */
:root{
  --card: rgba(15,18,22,0.82);
  --card2: rgba(15,18,22,0.76);
  --border: rgba(255,255,255,0.14);
  --text: #FFFFFF;
  --muted: #E3E6EB;     /* plus clair */
  --muted2: #B8C0CC;    /* plus clair */
  --hint: rgba(255,255,255,0.75);
  --accent: #EDEFF2;    /* primary button */
  --accentHover: #FFFFFF;
  --focus: rgba(237,239,242,0.22);
  --chipBg: rgba(255,255,255,0.06);
  --inputBg: rgba(0,0,0,0.42);
  --inputBorder: rgba(255,255,255,0.26);
  --inputBorderFocus: rgba(237,239,242,0.60);
}

/* --------- Base --------- */
html, body, [class*="css"]{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}

section.main > div{
  max-width: 920px;
  padding-top: 2.1rem;
}

/* Hide Streamlit default header/footer */
header, footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* --------- Card --------- */
.tm-card{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.70);
  animation: fadeIn 0.6s ease-out;
}

.tm-card2{
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px 26px 26px;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.60);
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn{
  from {opacity:0; transform: translateY(10px);}
  to   {opacity:1; transform: translateY(0);}
}

/* --------- Typography --------- */
.tm-title{
  font-size: 46px;
  margin: 0;
  font-weight: 750;
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
  margin-top: 18px;
  font-size: 24px;
  font-weight: 700;
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
  background: var(--chipBg);
}

/* --------- Inputs --------- */
.stTextInput label{
  color: var(--muted) !important;
}

.stTextInput input{
  background: var(--inputBg) !important;
  border: 1px solid var(--inputBorder) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.82rem 1rem !important;
  caret-color: var(--text) !important;
}

.stTextInput input::placeholder{
  color: rgba(255,255,255,0.50) !important;
}

/* Focus ring: remove red + keep theme */
.stTextInput input:focus{
  border: 1px solid var(--inputBorderFocus) !important;
  box-shadow: 0 0 0 3px var(--focus) !important;
  outline: none !important;
}

/* remove red invalid (mobile browser) */
input:invalid{
  border: 1px solid var(--inputBorder) !important;
  box-shadow: none !important;
  outline: none !important;
}

/* --------- Buttons (default) --------- */
.stButton button,
div[data-testid="stFormSubmitButton"] button{
  width: 100% !important;
  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,0.20) !important;
  background: rgba(255,255,255,0.08) !important;
  color: var(--text) !important;
  font-weight: 650 !important;
  height: 52px !important;
  min-height: 52px !important;
  padding: 0 !important;
}

.stButton button:hover,
div[data-testid="stFormSubmitButton"] button:hover{
  background: rgba(255,255,255,0.14) !important;
}

/* Primary button: neutral (no blue) */
button[kind="primary"]{
  background: var(--accent) !important;
  color: #0b0f16 !important;
  border: none !important;
}
button[kind="primary"]:hover{
  background: var(--accentHover) !important;
}

/* Disabled state */
button:disabled{
  opacity: 0.55 !important;
  cursor: not-allowed !important;
}

/* --------- Small muted line --------- */
.tm-muted{
  margin-top: 10px;
  font-size: 12px;
  color: rgba(255,255,255,0.72);
}

/* --------- PERFECT ALIGNMENT FOR 2 BUTTONS IN COLUMNS --------- */
div[data-testid="stHorizontalBlock"]{
  align-items: stretch !important;
}

div[data-testid="column"]{
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-end !important; /* align at bottom */
}

div[data-testid="stFormSubmitButton"]{
  margin-top: 0 !important;
  padding-top: 0 !important;
}

/* --------- Responsive --------- */
@media (max-width: 520px){
  .tm-title{ font-size: 38px; }
  .tm-card{ padding: 22px; }
  .tm-card2{ padding: 20px 22px 22px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# HERO
# =========================
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

# =========================
# COMMENCER (FORM)
# =========================
st.markdown(
    """
<div class="tm-card2">
  <div class="tm-h2" style="margin-top:0;">Commencer</div>
  <div class="tm-p" style="margin-top:6px;">
    Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Put the form inside the second card visually (Streamlit elements follow)
with st.form("start_form", clear_on_submit=False):
    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        go_continue = st.form_submit_button(
            "Continuer",
            type="primary",
            use_container_width=True,
            disabled=(not email or not email.strip()),
        )

    with col2:
        go_benef = st.form_submit_button(
            "Accès bénéficiaire",
            use_container_width=True,
        )

# Actions (MVP)
if go_continue:
    st.success("Redirection (MVP)")
elif go_benef:
    st.info("Accès bénéficiaire (MVP)")

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True,
)
```0
