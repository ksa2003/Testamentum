import streamlit as st

st.set_page_config(page_title="Nos offres", layout="wide")

st.title("Nos offres")

st.markdown(
    """
- Abonnement mensuel  
- Abonnement annuel  
- Envoi unique premium
"""
)

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
