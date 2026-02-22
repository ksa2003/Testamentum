import streamlit as st
from theme import apply_theme

apply_theme()

st.markdown("""
<div class="tm-card">
  <h1 class="tm-title">Testamentum</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>
</div>
""", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="tm-card">', unsafe_allow_html=True)
st.markdown("## Commencer")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

st.markdown("""
<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Continuer", use_container_width=True):
        st.session_state["prefill_email"] = email
        st.switch_page("pages/Connexion.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if st.button("Accès Bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_Beneficiaire.py")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
