import streamlit as st
from pathlib import Path

# ----------------------------
# Helpers
# ----------------------------
APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"

def asset_path(filename: str) -> Path:
    return ASSETS_DIR / filename

def show_image_if_exists(path: Path, *, caption: str | None = None, width: int | None = None, use_container_width: bool = False) -> bool:
    if not path.exists():
        st.warning(f"Image introuvable : {path.as_posix()}")
        return False

    # IMPORTANT: Streamlit n'accepte pas width + use_container_width en même temps.
    if use_container_width:
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        if width is not None:
            st.image(str(path), caption=caption, width=width)
        else:
            st.image(str(path), caption=caption)
    return True

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# Styles
# ----------------------------
st.markdown(
    """
    <style>
      .block-container { padding-top: 1.2rem; }
      section[data-testid="stSidebar"] { min-width: 260px !important; width: 260px !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Header (logo grand)
# ----------------------------
logo = asset_path("logo_kidan_vid.png")
show_image_if_exists(logo, use_container_width=True)

# ----------------------------
# Hero
# ----------------------------
st.title("Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

colA, colB, colC, colD = st.columns(4)
with colA:
    st.markdown("- 100% sécurisé")
with colB:
    st.markdown("- Accès unique et contrôlé")
with colC:
    st.markdown("- Programmation possible")
with colD:
    st.markdown("- Accessible partout")

st.markdown("")

# Boutons (haut de page)
cta1, cta2 = st.columns([1, 1])
with cta1:
    if st.button("Découvrir comment ça marche", use_container_width=True):
        st.switch_page("pages/01_Comment_ca_marche.py")
with cta2:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        st.switch_page("pages/02_Creer_un_envoi_securise.py")

st.markdown("---")

# ----------------------------
# Aperçu "Comment ça marche"
# ----------------------------
st.subheader("Comment ça marche ?")
steps = [
    ("I. Vous téléchargez votre vidéo", "Format sécurisé, cryptage immédiat."),
    ("II. Vous identifiez le destinataire", "Email + téléphone + vérification d’identité."),
    ("III. Nous sécurisons l’accès", "Code unique + double authentification (2FA)."),
    ("IV. Le destinataire reçoit la vidéo (timing)", "Accès personnel, protégé et traçable."),
]
for title, desc in steps:
    st.markdown(f"**{title}**  \n{desc}")

st.markdown("---")

# ----------------------------
# Pourquoi Kidan Vid
# ----------------------------
st.subheader("Pourquoi Kidan Vid ?")
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

# ----------------------------
# Cas d’usage
# ----------------------------
st.subheader("Cas d’usage")
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

# ----------------------------
# Nos offres
# ----------------------------
st.subheader("Nos offres")
st.markdown(
    """
- Abonnement mensuel
- Abonnement annuel
- Envoi unique premium
"""
)

st.markdown("---")

# ----------------------------
# Connexion tout en bas
# ----------------------------
st.subheader("Connexion")
st.write("Accédez à votre espace pour gérer vos envois et vos paramètres de sécurité (2FA, codes de récupération).")

if st.button("Se connecter", use_container_width=True):
    st.switch_page("pages/Connexion.py")
