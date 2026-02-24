import streamlit as st
from theme import apply_theme

apply_theme()

st.markdown(
    """
    <div class="tm-card">
        <div class="tm-title">Accès bénéficiaire</div>
        <div class="tm-sub">Entrez votre jeton sécurisé.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

token = st.text_input("Jeton d’accès")

if st.button("Accéder"):
    st.success("Jeton reçu (MVP).")

if st.button("Retour"):
    st.switch_page("app.py")
