from pathlib import Path

import streamlit as st
from PIL import Image

# -----------------------------------------------------
# CONFIG PAGE
# -----------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# -----------------------------------------------------
# HELPERS
# -----------------------------------------------------
def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return

    try:
        img = Image.open(path)
        col1, col2, col3 = st.columns([1.2, 4.6, 1.2])
        with col2:
            st.image(img, width=560)
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
    .stApp {
        background: linear-gradient(180deg, #0b2240 0%, #091a31 100%);
    }

    html, body, [class*="css"] {
        color: white !important;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 1.3rem;
        padding-bottom: 3rem;
    }

    a.anchor-link {
        display: none !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #06162a;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Titres */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }

    /* Paragraphes standard */
    p, li, label {
        color: #eef4fb !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;
    }

    /* Logo */
    .logo-wrap {
        margin-bottom: 24px;
        padding-top: 4px;
        padding-bottom: 2px;
    }

    /* Bloc principal */
    .hero-box {
        background: #244472;
        border-radius: 18px;
        padding: 28px;
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 10px 24px rgba(0,0,0,0.18);
        margin-bottom: 18px;
    }

    .hero-box h1 {
        font-size: 2.4rem !important;
        margin-bottom: 12px !important;
    }

    .hero-box .hero-sub {
        color: #ffffff !important;
        font-size: 1.08rem !important;
        margin-bottom: 12px !important;
        font-weight: 600 !important;
    }

    .hero-box .hero-text {
        color: #f4f8fc !important;
        font-size: 1.02rem !important;
        line-height: 1.8 !important;
    }

    /* Bloc juridique corrigé */
    .legal-box {
        background: #21406b;
        border-left: 5px solid #58a6ff;
        padding: 20px 18px;
        border-radius: 12px;
        margin: 18px 0 22px 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.14);
    }

    .legal-title {
        color: #ffffff !important;
        font-size: 1.08rem !important;
        font-weight: 800 !important;
        margin-bottom: 10px !important;
    }

    .legal-text {
        color: #ffffff !important;
        font-size: 1rem !important;
        line-height: 1.75 !important;
        font-weight: 500 !important;
    }

    /* Boutons */
    .stButton > button {
        background: #ffffff !important;
        color: #0a1e36 !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: 700 !important;
        min-height: 46px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.12) !important;
    }

    .stButton > button:hover {
        background: #e8f2ff !important;
        color: #0a1e36 !important;
    }

    .stButton > button * {
        color: #0a1e36 !important;
    }

    /* Points clés */
    .small-stat {
        background: #244472;
        border-radius: 14px;
        padding: 18px 12px;
        border: 1px solid rgba(255,255,255,0.10);
        text-align: center;
        font-weight: 700;
        color: white !important;
        box-shadow: 0 6px 16px rgba(0,0,0,0.14);
        min-height: 82px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Piliers */
    .pill-card {
        background: #31558b;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.12);
        min-height: 205px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
        margin-bottom: 12px;
    }

    .pill-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 30px rgba(0,0,0,0.28);
    }

    .pill-title {
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 10px;
        color: white !important;
    }

    .pill-text {
        color: #f5f9ff !important;
        line-height: 1.7;
        font-size: 1.02rem;
    }

    /* Inputs */
    input, textarea {
        background: #112745 !important;
        color: white !important;
    }

    div[data-baseweb="select"] {
        background: #112745 !important;
        color: white !important;
    }

    /* Ligne */
    hr {
        border-color: rgba(255,255,255,0.12);
    }

    /* Caption */
    .stCaption {
        color: rgba(255,255,255,0.78) !important;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# LOGO
# -----------------------------------------------------
st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
show_logo(LOGO_PATH)
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# HERO
# -----------------------------------------------------
st.markdown(
    """
    <div class="hero-box">
        <h1>Kidan Vid</h1>
        <div class="hero-sub">
            Plateforme de transmission vidéo, audio et documentaire sécurisée.
        </div>
        <div class="hero-text">
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
        <div class="legal-title">Point juridique important</div>
        <div class="legal-text">
            En France, une vidéo seule ne constitue pas un testament juridiquement valable.
            Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# BOUTONS PRINCIPAUX
# -----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche", key="home_how"):
        go_to_page("Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé", key="home_create"):
        go_to_page("Creer_un_envoi_securise.py")

# -----------------------------------------------------
# POINTS CLÉS
# -----------------------------------------------------
st.markdown("<h2>Points clés</h2>", unsafe_allow_html=True)

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
st.markdown("<h2>Les 4 piliers Kidan Vid</h2>", unsafe_allow_html=True)

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pill-card" title="Transmission vidéo sécurisée, messages programmés et consultation contrôlée.">
            <div style="font-size:36px;">🎥</div>
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
            <div style="font-size:36px;">🎙️</div>
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
            <div style="font-size:36px;">🛡️</div>
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
            <div style="font-size:36px;">⚖️</div>
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
st.markdown("<h2>Témoignages</h2>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

# -----------------------------------------------------
# ACCÈS RAPIDES
# -----------------------------------------------------
st.markdown("---")
st.markdown("<h2>Accès rapides</h2>", unsafe_allow_html=True)

q1, q2, q3, q4 = st.columns(4)
with q1:
    if st.button("Qui sommes-nous", key="quick_about"):
        go_to_page("Qui_sommes_nous.py")
with q2:
    if st.button("Nous contacter", key="quick_contact"):
        go_to_page("Nous_contacter.py")
with q3:
    if st.button("Informations légales", key="quick_info_legal"):
        go_to_page("Informations_legales.py")
with q4:
    if st.button("Mentions légales", key="quick_mentions"):
        go_to_page("Mentions_legales.py")

# -----------------------------------------------------
# CONNEXION EN BAS
# -----------------------------------------------------
st.markdown("---")
st.markdown("<h2>Connexion</h2>", unsafe_allow_html=True)
st.write("Accédez à votre espace sécurisé.")

st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer", key="btn_continue_home"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire", key="btn_benef_home"):
        go_to_page("Acces_beneficiaire.py")

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------
st.markdown("---")
st.caption("© Kidan Vid")
