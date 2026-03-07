from pathlib import Path

import streamlit as st
from PIL import Image

# -----------------------------------------------------
# CONFIG PAGE
# -----------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    layout="centered",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# -----------------------------------------------------
# HELPERS
# -----------------------------------------------------
def show_logo(path: Path, width: int = 620):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    try:
        img = Image.open(path)
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.image(img, width=width)
    except Exception as e:
        st.error(f"Impossible de charger le logo : {e}")


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


# -----------------------------------------------------
# STYLE GLOBAL
# -----------------------------------------------------
st.markdown(
    """
    <style>
    /* fond principal */
    .stApp {
        background: linear-gradient(180deg, #0f2747 0%, #0a1e36 100%);
    }

    /* texte global */
    html, body, [class*="css"] {
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1000px;
    }

    a.anchor-link {
        display: none !important;
    }

    /* sidebar */
    section[data-testid="stSidebar"] {
        background: #081b30;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* zone logo */
    .logo-wrap {
        background: #102c4f;
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 18px;
        padding: 26px 18px 18px 18px;
        margin-bottom: 22px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    /* hero */
    .hero-box {
        background: #1c3d66;
        border-radius: 18px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.14);
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    /* bloc juridique */
    .legal-box {
        background: #193a5f;
        border-left: 5px solid #4da3ff;
        padding: 16px;
        border-radius: 10px;
        margin: 18px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }

    /* cartes standards */
    .card {
        background: #204c7a;
        border-radius: 14px;
        padding: 18px;
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 8px 20px rgba(0,0,0,0.14);
    }

    /* cartes piliers */
    .pill-card {
        background: #244f80;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.12);
        min-height: 185px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }

    .pill-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 30px rgba(0,0,0,0.28);
    }

    .pill-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-top: 8px;
        margin-bottom: 10px;
        color: white;
    }

    .pill-text {
        color: rgba(255,255,255,0.92);
        line-height: 1.6;
        font-size: 1rem;
    }

    .small-stat {
        background: #1b446d;
        border-radius: 14px;
        padding: 18px 12px;
        border: 1px solid rgba(255,255,255,0.10);
        text-align: center;
        font-weight: 700;
        color: white;
        box-shadow: 0 6px 18px rgba(0,0,0,0.14);
        min-height: 82px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* champs */
    input, textarea {
        background: #132c4a !important;
        color: white !important;
    }

    label, .stTextInput label, .stTextArea label {
        color: white !important;
    }

    div[data-baseweb="select"] {
        background: #132c4a !important;
        color: white !important;
    }

    /* boutons */
    .stButton > button {
        background: white;
        color: #0a1e36;
        border-radius: 10px;
        border: none;
        font-weight: 700;
        min-height: 44px;
    }

    .stButton > button:hover {
        background: #e5f1ff;
        color: #0a1e36;
    }

    /* hr */
    hr {
        border-color: rgba(255,255,255,0.12);
    }

    /* caption */
    .stCaption {
        color: rgba(255,255,255,0.70) !important;
    }

    /* masquer footer streamlit */
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# HEADER / LOGO
# -----------------------------------------------------
st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
show_logo(LOGO_PATH, width=620)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin-bottom:10px; color:white;">Kidan Vid</h1>
        <div style="font-size:1.08rem; margin-bottom:12px; color:white;">
            Plateforme de transmission vidéo, audio et documentaire sécurisée.
        </div>
        <div style="font-size:1.02rem; line-height:1.7; color:rgba(255,255,255,0.95);">
            Envoyez des messages personnels en toute confidentialité.
            Vidéos, audios, documents et accès bénéficiaire sont organisés
            dans une logique humaine, technique et juridique.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# AVERTISSEMENT JURIDIQUE
# -----------------------------------------------------
st.markdown(
    """
    <div class="legal-box">
        <b>Point juridique important</b><br><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# BOUTONS PRINCIPAUX
# -----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche", use_container_width=True):
        go_to_page("Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        go_to_page("Creer_un_envoi_securise.py")

# -----------------------------------------------------
# POINTS CLÉS
# -----------------------------------------------------
st.markdown("### Points clés")
s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown('<div class="small-stat">100% sécurisé</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="small-stat">Accès unique et contrôlé</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="small-stat">Programmation possible</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="small-stat">Notaire intégré</div>', unsafe_allow_html=True)

# -----------------------------------------------------
# 4 PILIERS
# -----------------------------------------------------
st.markdown("## Les 4 piliers Kidan Vid")

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pill-card" title="Transmission vidéo sécurisée, messages programmés et consultation contrôlée.">
            <div style="font-size:34px;">🎥</div>
            <div class="pill-title">Vidéo</div>
            <div class="pill-text">
                Messages vidéo personnels programmés et délivrés au bon moment.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        """
        <div class="pill-card" title="Enregistrements vocaux, mémoire sonore et messages audio.">
            <div style="font-size:34px;">🎙️</div>
            <div class="pill-title">Audio</div>
            <div class="pill-text">
                Souvenirs vocaux, témoignages sonores et compléments de transmission.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

p3, p4 = st.columns(2)
with p3:
    st.markdown(
        """
        <div class="pill-card" title="Chiffrement, double authentification, OTP et traçabilité.">
            <div style="font-size:34px;">🛡️</div>
            <div class="pill-title">Sécurisation</div>
            <div class="pill-text">
                Protection technique : chiffrement, double authentification et traçabilité.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p4:
    st.markdown(
        """
        <div class="pill-card" title="La vidéo seule n’a pas de valeur testamentaire en France. Le notaire structure juridiquement la transmission.">
            <div style="font-size:34px;">⚖️</div>
            <div class="pill-title">Notaires</div>
            <div class="pill-text">
                Le pilier juridique central pour articuler la transmission avec le droit.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------
# TEMOIGNAGES
# -----------------------------------------------------
st.markdown("## Témoignages")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

# -----------------------------------------------------
# ACCÈS RAPIDES
# -----------------------------------------------------
st.markdown("---")
st.markdown("## Accès rapides")

q1, q2, q3, q4 = st.columns(4)
with q1:
    if st.button("Qui sommes-nous", use_container_width=True):
        go_to_page("Qui_sommes_nous.py")
with q2:
    if st.button("Nous contacter", use_container_width=True):
        go_to_page("Nous_contacter.py")
with q3:
    if st.button("Informations légales", use_container_width=True):
        go_to_page("Informations_legales.py")
with q4:
    if st.button("Mentions légales", use_container_width=True):
        go_to_page("Mentions_legales.py")

# -----------------------------------------------------
# CONNEXION EN BAS
# -----------------------------------------------------
st.markdown("---")
st.markdown("## Connexion")
st.write("Accédez à votre espace sécurisé.")

st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer", use_container_width=True, key="btn_continue_home"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire", use_container_width=True, key="btn_benef_home"):
        go_to_page("Acces_beneficiaire.py")

# -----------------------------------------------------
# FOOTER SIMPLE
# -----------------------------------------------------
st.markdown("---")
st.caption("© Kidan Vid")
