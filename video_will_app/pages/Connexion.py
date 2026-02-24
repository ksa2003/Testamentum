import streamlit as st
from theme import apply_theme

apply_theme()

st.markdown(
    """
    <div class="tm-card">
        <div class="tm-title">Connexion</div>
        <div class="tm-sub">Accédez à votre espace sécurisé.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

email = st.text_input("Adresse e-mail")
password = st.text_input("Mot de passe", type="password")

col1, col2 = st.columns(2)
with col1:
    st.button("Se connecter")
with col2:
    if st.button("Retour"):
        st.switch_page("app.py")
