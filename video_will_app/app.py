import streamlit as st
from pathlib import Path
from PIL import Image

# -------------------------------------------------
# CONFIG PAGE
# -------------------------------------------------

st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🔒",
    layout="centered"
)

# -------------------------------------------------
# CHEMIN LOGO
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
logo_path = BASE_DIR / "logo_kidan_vid.png"

# -------------------------------------------------
# AFFICHAGE LOGO GRAND FORMAT
# -------------------------------------------------

if logo_path.exists():
    img = Image.open(logo_path)
    st.image(img, width=900)  # Ajuste ici si besoin
else:
    st.warning("Logo introuvable : logo_kidan_vid.png")

# -------------------------------------------------
# CONTENU PRINCIPAL
# -------------------------------------------------

st.markdown("## Kidan Vid")
st.markdown("Plateforme de transmission vidéo sécurisée.")

st.write(
    """
Envoyez des vidéos personnelles en toute confidentialité.  

La première plateforme sécurisée qui permet d’envoyer une vidéo privée  
à une personne, accessible uniquement par elle, lorsque vous reposez en paix.
"""
)

col1, col2, col3, col4 = st.columns(4)

col1.markdown("**100% sécurisé**")
col2.markdown("**Accès unique et contrôlé**")
col3.markdown("**Programmation possible**")
col4.markdown("**Accessible partout**")

# -------------------------------------------------
# COMMENT CA MARCHE
# -------------------------------------------------

st.markdown("---")
st.markdown("## Comment ça marche ?")

st.markdown("""
**I. Vous téléchargez votre vidéo**  
Format sécurisé, cryptage immédiat.

**II. Vous identifiez le destinataire**  
Email + téléphone + vérification d’identité.

**III. Nous sécurisons l’accès**  
Code unique + double authentification (2FA).

**IV. Le destinataire reçoit la vidéo**  
Accès personnel, protégé et traçable.
""")

# -------------------------------------------------
# POURQUOI KIDAN VID
# -------------------------------------------------

st.markdown("---")
st.markdown("## Pourquoi Kidan Vid ?")

st.markdown("""
- Cryptage de bout en bout  
- Vidéo non téléchargeable  
- Accès limité dans le temps  
- Traçabilité des ouvertures  
- Hébergement conforme RGPD  
""")

# -------------------------------------------------
# NOS OFFRES
# -------------------------------------------------

st.markdown("---")
st.markdown("## Nos offres")

st.markdown("""
- Abonnement mensuel  
- Abonnement annuel  
- Envoi unique premium  
""")

# -------------------------------------------------
# CONNEXION EN BAS
# -------------------------------------------------

st.markdown("---")
st.markdown("## Connexion")

email = st.text_input("Adresse e-mail")

colA, colB = st.columns(2)

with colA:
    if st.button("Continuer"):
        st.switch_page("pages/Connexion.py")

with colB:
    if st.button("Accès bénéficiaire"):
        st.switch_page("pages/Acces_beneficiaire.py")

st.markdown("---")
st.caption("© Kidan Vid")
