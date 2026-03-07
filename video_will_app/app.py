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
def show_logo(path: Path, width: int = 420):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    try:
        img = Image.open(path)
        st.image(img, width=width)
    except Exception as e:
        st.error(f"Impossible de charger le logo : {e}")


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


# -----------------------------------------------------
# STYLE GLOBAL BLEU
# -----------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg,#0A66C2 0%,#084C95 100%);
    }

    html, body, [class*="css"] {
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 980px;
    }

    a.anchor-link {
        display: none !important;
    }

    .card {
        background: rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 24px;
        border: 1px solid rgba(255,255,255,0.15);
    }

    .hero-box {
        background: rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 24px;
        border: 1px solid rgba(255,255,255,0.20);
    }

    .legal-box {
        border-left: 5px solid #ffffff;
        background: rgba(255,255,255,0.08);
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
    }

    .pill-card {
        background: rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.14);
        min-height: 170px;
    }

    .stButton > button {
        background: white;
        color: #0A66C2;
        border-radius: 10px;
        border: none;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #eaf4ff;
        color: #084C95;
    }

    section[data-testid="stSidebar"] {
        background: #063970;
    }

    input, textarea {
        background: rgba(255,255,255,0.10) !important;
        color: white !important;
    }

    div[data-baseweb="select"] {
        background: rgba(255,255,255,0.10);
    }

    button[data-baseweb="tab"] {
        color: white;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background: #0A66C2;
    }

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
show_logo(LOGO_PATH, width=420)

st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin-bottom:10px;">Kidan Vid</h1>
        <div style="font-size:1.08rem; margin-bottom:12px;">
            Plateforme de transmission vidéo, audio et documentaire sécurisée.
        </div>
        <div style="font-size:1.02rem; line-height:1.6;">
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
# BLOCS RAPIDES
# -----------------------------------------------------
st.markdown("### Points clés")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="card" style="text-align:center;padding:16px;">
            <b>100% sécurisé</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="card" style="text-align:center;padding:16px;">
            <b>Accès unique et contrôlé</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="card" style="text-align:center;padding:16px;">
            <b>Programmation possible</b>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        """
        <div class="card" style="text-align:center;padding:16px;">
            <b>Notaire intégré</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------
# 4 PILIERS
# -----------------------------------------------------
st.markdown("## Les 4 piliers Kidan Vid")

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pill-card" title="Transmission vidéo sécurisée, messages programmés et consultation contrôlée.">
            <div style="font-size:30px;">🎥</div>
            <h4>Vidéo</h4>
            <div>Messages vidéo personnels programmés et délivrés au bon moment.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with p2:
    st.markdown(
        """
        <div class="pill-card" title="Enregistrements vocaux, mémoire sonore et messages audio.">
            <div style="font-size:30px;">🎙️</div>
            <h4>Audio</h4>
            <div>Souvenirs vocaux, témoignages sonores et compléments de transmission.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

p3, p4 = st.columns(2)
with p3:
    st.markdown(
        """
        <div class="pill-card" title="Chiffrement, double authentification, OTP et traçabilité.">
            <div style="font-size:30px;">🛡️</div>
            <h4>Sécurisation</h4>
            <div>Protection technique : chiffrement, double authentification et traçabilité.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with p4:
    st.markdown(
        """
        <div class="pill-card" title="La vidéo seule n’a pas de valeur testamentaire en France. Le notaire structure juridiquement la transmission.">
            <div style="font-size:30px;">⚖️</div>
            <h4>Notaires</h4>
            <div>Le pilier juridique central pour articuler la transmission avec le droit.</div>
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
