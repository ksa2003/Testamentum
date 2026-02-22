import streamlit as st
from utils.theme import apply_theme

st.set_page_config(page_title="Accès bénéficiaire — Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

st.markdown(
    """
<div class="tm-card">
  <h1 class="tm-title" style="font-size:40px;">Accès bénéficiaire</h1>
  <div class="tm-p" style="margin-top:8px;">
    Saisissez un jeton d’accès transmis par la famille ou le notaire.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

with st.form("benef_form"):
    token = st.text_input("Jeton", placeholder="Ex : TM-9F4K-2Q7A")
    submitted = st.form_submit_button("Accéder", type="primary", use_container_width=True)

if submitted:
    if not token.strip():
        st.error("Veuillez saisir un jeton.")
    else:
        st.info("Vérification du jeton (MVP).")
