import streamlit as st

st.set_page_config(page_title="Pourquoi Kidan Vid", layout="wide")

st.title("Pourquoi Kidan Vid ?")

st.markdown(
    """
- Chiffrement de bout en bout  
- Vidéo non téléchargeable  
- Accès limité dans le temps  
- Traçabilité des ouvertures  
- Option « visionnage unique »  
- Hébergement sécurisé conforme RGPD
"""
)

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
