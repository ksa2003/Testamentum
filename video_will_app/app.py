import streamlit as st
from pathlib import Path
from PIL import Image

# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="K",
    layout="centered",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# -------------------------------------------------
# CSS : Empêche tout débordement + logo responsive
# -------------------------------------------------
st.markdown(
    """
    <style>
      /* Empêche le scroll horizontal (cause principale du titre "coupé") */
      html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        overflow-x: hidden !important;
      }

      /* Largeur et padding adaptés */
      .block-container {
        max-width: 980px;
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
      }

      /* Logo responsive : jamais coupé, jamais trop grand sur mobile */
      .kidan-logo-wrap {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 0.2rem 0 0.8rem 0;
      }
      .kidan-logo-wrap img {
        width: 100%;
        max-width: 900px;
        max-height: 55vh;     /* Important : le logo ne dépasse pas l'écran mobile */
        height: auto;
        object-fit: contain;  /* Important : pas de recadrage */
        display: block;
      }

      /* Séparateurs plus propres sur mobile */
      hr {
        margin: 1rem 0 1rem 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# NAVIGATION
# -------------------------------------------------
def go_to_page(page_name: str):
    try:
        st.switch_page(f"pages/{page_name}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")

# -------------------------------------------------
# LOGO (affiché via HTML pour contrôler la taille)
# -------------------------------------------------
def show_logo():
    if not LOGO_PATH.exists():
        st.warning(f"Logo introuvable : {LOGO_PATH}")
        return

    # On charge l'image juste pour valider qu'elle est lisible
    try:
        Image.open(LOGO_PATH)
    except Exception:
        st.warning("Le fichier logo existe, mais il est illisible (PNG corrompu ou format non supporté).")
        return

    # Affichage via HTML (contrôle total du rendu mobile)
    st.markdown(
        f"""
        <div class="kidan-logo-wrap">
          <img src="app/static?path={LOGO_PATH.as_posix()}" alt="Kidan Vid logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit Cloud ne sert pas toujours ce "static?path".
    # Donc on fait un fallback invisible qui marche toujours :
    st.image(str(LOGO_PATH), use_container_width=True)

# -------------------------------------------------
# CONTENU
# -------------------------------------------------
show_logo()

st.title("Kidan Vid")
st.write("Plateforme de transmission vidéo sécurisée.")
st.write("Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Découvrir comment ça marche"):
        go_to_page("Comment_ca_marche.py")
with col2:
    if st.button("Créer un envoi sécurisé"):
        go_to_page("Creer_un_envoi_securise.py")

st.divider()

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("**100% sécurisé**")
with c2:
    st.markdown("**Accès unique et contrôlé**")
with c3:
    st.markdown("**Programmation possible**")
with c4:
    st.markdown("**Accessible partout**")

st.divider()

st.header("Comment ça marche ?")

st.markdown("**I. Vous téléchargez votre vidéo**")
st.write("Format sécurisé, cryptage immédiat.")

st.markdown("**II. Vous identifiez le destinataire**")
st.write("Email + téléphone + vérification d’identité.")

st.markdown("**III. Nous sécurisons l’accès**")
st.write("Code unique + double authentification (2FA).")

st.markdown("**IV. Le destinataire reçoit la vidéo**")
st.write("Accès personnel, protégé et traçable.")

st.divider()

st.header("Pourquoi Kidan Vid ?")
st.markdown(
    """
- Cryptage de bout en bout
- Vidéo non téléchargeable
- Accès limité dans le temps
- Traçabilité des ouvertures
- Visionnage unique possible
- Hébergement conforme RGPD
"""
)

st.divider()

st.header("Nos offres")
st.markdown(
    """
- Abonnement mensuel
- Abonnement annuel
- Envoi unique premium
"""
)

st.divider()

# -------------------------------------------------
# CONNEXION EN BAS
# -------------------------------------------------
st.header("Connexion")
st.write("Accédez à votre espace sécurisé.")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

colA, colB = st.columns(2)
with colA:
    if st.button("Continuer"):
        go_to_page("Connexion.py")
with colB:
    if st.button("Accès bénéficiaire"):
        go_to_page("Acces_beneficiaire.py")

st.caption("© Kidan Vid")
