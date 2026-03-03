import streamlit as st

st.set_page_config(page_title="Informations – sécurité maximale", layout="wide")

st.title("Informations à collecter pour une sécurité maximale")
st.caption("Objectif : protéger l’expéditeur, le destinataire et la plateforme.")

st.subheader("Informations demandées à l’abonné (expéditeur)")
st.markdown(
    """
Identité vérifiée (KYC simplifié)

Obligatoire :
- Nom complet
- Date de naissance
- Pièce d’identité (vérification automatique)
- Email vérifié
- Numéro de téléphone vérifié (SMS OTP)
- Pays de résidence
- Adresse IP enregistrée

Pour formule premium :
- Pièce d’identité (vérification automatique)
- Selfie vidéo de validation
"""
)

st.subheader("Sécurité compte")
st.markdown(
    """
- Mot de passe fort obligatoire  
- Double authentification (2FA)  
- Question secrète  
- Code de récupération  
"""
)

st.subheader("Informations demandées pour le destinataire")
st.markdown(
    """
Minimum requis :
- Nom complet
- Nom complet de ses parents
- Informations sur sa famille (frère, sœur, cousin, cousine, tante, oncle si besoin)
- Email
- Numéro de téléphone
- Pays
- Adresse (localité)

Sécurité renforcée :
- Raconter une histoire commune (authentifier l’auteur de la vidéo)
- Question secrète personnalisée
- Code OTP envoyé par SMS
- Lien à usage unique
- Date limite d’accès
- Limitation du nombre de visionnages
- Option reconnaissance faciale (premium)
- Lien pour succession (actes notariés)
"""
)

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
