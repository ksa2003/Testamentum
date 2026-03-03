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
    """Charge une image de façon sûre (évite les erreurs Streamlit)."""
    try:
        return Image.open(path)
    except Exception:
        return None

def show_logo():
    """
    Affiche le logo depuis /assets.
    Important: ne PAS mélanger width=... et use_container_width=True
    (cela peut provoquer des TypeError selon les versions Streamlit).
    """
    logo_path = ASSETS_DIR / LOGO_FILE

    if logo_path.exists():
        img = load_image(logo_path)
        if img is None:
            st.warning(f"Impossible d'ouvrir l'image : {logo_path}")
            return
        st.image(img, use_container_width=True)
    else:
        st.warning(f"Logo introuvable : {logo_path}")

def go_to_page(page_filename: str):
    """
    Redirige vers une page Streamlit multipage si possible.
    Exemple: pages/Connexion.py -> st.switch_page('pages/Connexion.py')
    """
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        # Fallback: affiche une info plutôt que de planter
        st.info("Navigation indisponible sur cette version Streamlit. Utilisez le menu à gauche pour ouvrir la page.")

# -----------------------------
# Styles
# -----------------------------
st.markdown(
    """
    <style>
      /* Resserre un peu la largeur max du contenu (effet landing page) */
      .block-container { max-width: 900px; padding-top: 1.5rem; }

      /* Petits séparateurs plus discrets */
      hr { margin: 2rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Page content
# -----------------------------
show_logo()

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
    if st.button("Découvrir comment ça marche", use_container_width=True):
        # Si tu as une page pages/Comment_ca_marche.py
        go_to_page("Comment_ca_marche.py")
with colB:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        # Si tu as une page pages/Creer_un_envoi_securise.py
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

# Connexion en bas (comme avant)
st.header("Connexion")
st.write("Accédez à votre espace sécurisé.")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

btn1, btn2 = st.columns(2)
with btn1:
    if st.button("Continuer", use_container_width=True):
        # Redirection vers la page de connexion
        # Si tu as pages/Connexion.py
        go_to_page("Connexion.py")

with btn2:
    if st.button("Accès bénéficiaire", use_container_width=True):
        # Si tu as pages/Acces_beneficiaire.py
        go_to_page("Acces_beneficiaire.py")

st.caption("© Kidan Vid")
