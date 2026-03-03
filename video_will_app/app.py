import streamlit as st
from pathlib import Path
from PIL import Image

# -----------------------------
# Config
# -----------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_FILE = "logo_kidan_vid.png"

# -----------------------------
# Helpers
# -----------------------------
def load_image(path: Path):
    try:
        return Image.open(path)
    except Exception:
        return None

def show_logo(width: int = 720):
    """
    Affiche le logo depuis /assets en évitant use_container_width
    (certaines versions Streamlit lèvent TypeError).
    """
    logo_path = ASSETS_DIR / LOGO_FILE

    if not logo_path.exists():
        st.warning(f"Logo introuvable : {logo_path}")
        return

    img = load_image(logo_path)
    if img is None:
        st.warning(f"Impossible d'ouvrir l'image : {logo_path}")
        return

    # Version compatible : pas de use_container_width
    st.image(img, width=width)

def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour ouvrir la page (navigation auto indisponible ici).")

# -----------------------------
# Styles
# -----------------------------
st.markdown(
    """
    <style>
      .block-container { max-width: 900px; padding-top: 1.5rem; }
      hr { margin: 2rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Page content
# -----------------------------
show_logo(width=760)

st.title("Kidan Vid")
st.write("Plateforme de transmission vidéo sécurisée.")
st.write("Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

# Boutons d'action
colA, colB = st.columns(2)
with colA:
    if st.button("Découvrir comment ça marche"):
        go_to_page("Comment_ca_marche.py")
with colB:
    if st.button("Créer un envoi sécurisé"):
        go_to_page("Creer_un_envoi_securise.py")

st.markdown("---")

# Points clés
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("**100% sécurisé**")
with c2:
    st.markdown("**Accès unique et contrôlé**")
with c3:
    st.markdown("**Programmation possible**")
with c4:
    st.markdown("**Accessible partout**")

st.markdown("---")

# Comment ça marche
st.header("Comment ça marche ?")

st.markdown("**I. Vous téléchargez votre vidéo**")
st.write("Format sécurisé, cryptage immédiat.")

st.markdown("**II. Vous identifiez le destinataire**")
st.write("Email + téléphone + vérification d’identité.")

st.markdown("**III. Nous sécurisons l’accès**")
st.write("Code unique + double authentification (2FA).")

st.markdown("**IV. Le destinataire reçoit la vidéo**")
st.write("Accès personnel, protégé et traçable.")

st.markdown("---")

# Pourquoi
st.header("Pourquoi Kidan Vid ?")
st.markdown(
    """
- Cryptage de bout en bout
- Vidéo non téléchargeable
- Accès limité dans le temps
- Traçabilité des ouvertures
- Option "visionnage unique"
- Hébergement sécurisé conforme RGPD
"""
)

st.markdown("---")

# Cas d'usage
st.header("Cas d’usage")
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

# Offres
st.header("Nos offres")
st.markdown(
    """
- Abonnement mensuel
- Abonnement annuel
- Envoi unique premium
"""
)

st.markdown("---")

# Connexion en bas
st.header("Connexion")
st.write("Accédez à votre espace sécurisé.")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire"):
        go_to_page("Acces_beneficiaire.py")

st.caption("© Kidan Vid")
