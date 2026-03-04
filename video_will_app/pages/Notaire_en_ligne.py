import streamlit as st
from pathlib import Path
from PIL import Image

# -----------------------------
# Config
# -----------------------------
st.set_page_config(page_title="Notaire en ligne", layout="centered")

# -----------------------------
# Logo loader (local)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

def show_logo():
    if LOGO_PATH.exists():
        img = Image.open(LOGO_PATH)
        st.image(img, width=500)
    else:
        st.warning("Logo introuvable.")

# -----------------------------
# Header
# -----------------------------
show_logo()

st.title("Notaire en ligne")

st.write(
"""
Cette section permet de préparer les informations nécessaires
pour les actes notariés et la transmission sécurisée.
"""
)

st.markdown("---")

st.header("Informations à collecter pour une sécurité maximale")

st.write(
"""
Objectif : protéger l’expéditeur, le destinataire et la plateforme.
"""
)

# -----------------------------
# Abonné
# -----------------------------
st.subheader("Informations demandées à l’abonné (expéditeur)")

st.markdown(
"""
**Identité vérifiée (KYC simplifié)**

Obligatoire :

• Nom complet  
• Date de naissance  
• Pièce d’identité (vérification automatique)  
• Email vérifié  
• Numéro de téléphone vérifié (SMS OTP)  
• Pays de résidence  
• Adresse IP enregistrée  

Pour formule premium :

• Pièce d’identité (vérification automatique)  
• Selfie vidéo de validation  
"""
)

st.markdown("---")

st.subheader("Sécurité du compte")

st.markdown(
"""
• Mot de passe fort obligatoire  
• Double authentification (2FA)  
• Question secrète  
• Code de récupération  
"""
)

st.markdown("---")

# -----------------------------
# Bénéficiaire
# -----------------------------
st.subheader("Informations demandées pour le destinataire")

st.markdown(
"""
Minimum requis :

• Nom complet  
• Nom complet des parents  
• Informations sur sa famille  
• Email  
• Numéro de téléphone  
• Pays  
• Adresse (localité)
"""
)

st.markdown("Sécurité renforcée :")

st.markdown(
"""
• Raconter une histoire commune (authentifier l’auteur de la vidéo)  
• Question secrète personnalisée  
• Code OTP envoyé par SMS  
• Lien à usage unique  
• Date limite d’accès  
• Limitation du nombre de visionnages  
• Option reconnaissance faciale (premium)  
• Lien pour succession (actes notariés)  
"""
)

st.markdown("---")

if st.button("Retour accueil"):
    st.switch_page("app.py")
