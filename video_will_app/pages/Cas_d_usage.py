import streamlit as st

st.set_page_config(page_title="Cas d’usage", layout="wide")

st.title("Cas d’usage")

st.markdown(
    """
- Messages personnels confidentiels  
- Transmission de souvenirs familiaux  
- Messages importants programmés  
- Communication sensible  
- Transmission patrimoniale numérique
"""
)

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
