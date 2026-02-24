import streamlit as st
from theme import apply_theme

apply_theme()

st.markdown(
    """
    <div class="tm-card">
        <div class="tm-title">Espace Mémoire</div>
        <div class="tm-sub">Gérez vos messages vidéo et bénéficiaires.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.text_input("Titre du message")
st.file_uploader("Sélectionner une vidéo")

col1, col2 = st.columns(2)
with col1:
    st.button("Téléverser")
with col2:
    st.button("Gérer bénéficiaires")

if st.button("Se déconnecter"):
    st.switch_page("app.py")
