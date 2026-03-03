import streamlit as st

st.set_page_config(page_title="Comment ça marche", layout="wide")

st.title("Comment ça marche ?")

st.markdown(
    """
1) Vous téléchargez votre vidéo  
Format sécurisé, chiffrement immédiat.

2) Vous identifiez le destinataire  
Email + téléphone + vérification d’identité.

3) Nous sécurisons l’accès  
Code unique + double authentification.

4) Le destinataire reçoit la vidéo (timing)  
Accès personnel, protégé et traçable.
"""
)

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        st.switch_page("pages/Connexion.py")
with c2:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
