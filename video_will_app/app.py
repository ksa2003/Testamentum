import streamlit as st
from utils.theme import apply_theme

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

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

with st.form("start_form", clear_on_submit=False):
    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        go_continue = st.form_submit_button("Continuer", type="primary", use_container_width=True)
    with col2:
        go_benef = st.form_submit_button("Accès bénéficiaire", use_container_width=True)

if go_continue:
    st.session_state["prefill_email"] = (email or "").strip()
    st.switch_page("pages/Connexion.py")

if go_benef:
    st.switch_page("pages/Acces_beneficiaire.py")

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True,
)
