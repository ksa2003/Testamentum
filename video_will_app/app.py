import streamlit as st
from pathlib import Path
from PIL import Image

# -----------------------------------------------------
# CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#123C73"
BLUE_SOFT = "#EAF4FF"
CARD_BG = "#F7FAFE"

# -----------------------------------------------------
# HELPERS
# -----------------------------------------------------
def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return

    try:
        img = Image.open(path)
        # grande largeur, sans use_container_width pour compatibilité
        st.image(img, width=1200)
    except Exception as e:
        st.error(f"Impossible de charger le logo : {e}")


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


# -----------------------------------------------------
# STYLE
# -----------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background: #ffffff;
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }}

    a.anchor-link {{
        display: none !important;
    }}

    h1, h2, h3 {{
        color: #111827 !important;
    }}

    p, li, label {{
        color: #1f2937 !important;
        line-height: 1.7 !important;
    }}

    .hero-box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 20px;
        padding: 24px;
        background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
        margin-top: 6px;
        margin-bottom: 18px;
    }}

    .hero-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 10px;
    }}

    .hero-text {{
        font-size: 1.03rem;
        color: #27435f;
        line-height: 1.8;
    }}

    .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 16px 18px;
        border-radius: 12px;
        margin: 18px 0 22px 0;
    }}

    .legal-title {{
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 8px;
    }}

    .stat-box {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        background: #ffffff;
        padding: 16px 12px;
        text-align: center;
        font-weight: 700;
        color: {BLUE_DARK};
        min-height: 78px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 6px 18px rgba(10,102,194,0.05);
    }}

    .pillar-card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 18px;
        background: {CARD_BG};
        padding: 22px;
        min-height: 220px;
        box-shadow: 0 8px 22px rgba(10,102,194,0.06);
        transition: transform 0.15s ease;
    }}

    .pillar-card:hover {{
        transform: translateY(-2px);
    }}

    .pillar-icon {{
        width: 62px;
        height: 62px;
        border-radius: 50%;
        background: {BLUE_SOFT};
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        margin-bottom: 14px;
    }}

    .pillar-title {{
        font-size: 1.45rem;
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 10px;
    }}

    .pillar-text {{
        color: #3e5974;
        font-size: 1rem;
        line-height: 1.7;
    }}

    .section-space {{
        margin-top: 8px;
        margin-bottom: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# LOGO
# -----------------------------------------------------
show_logo(LOGO_PATH)

# -----------------------------------------------------
# HERO
# -----------------------------------------------------
st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-title">Kidan Vid</div>
        <div class="hero-text">
            Plateforme de transmission vidéo, audio et documentaire sécurisée.<br><br>
            Envoyez des messages personnels en toute confidentialité. Vidéos, audios,
            documents et accès bénéficiaire sont organisés dans une logique humaine,
            technique et juridique.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# LEGAL
# -----------------------------------------------------
st.markdown(
    f"""
    <div class="legal-box">
        <div class="legal-title">Point juridique important</div>
        <div>
            En France, une vidéo seule ne constitue pas un testament juridiquement valable.
            Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------
# ACTIONS
# -----------------------------------------------------
c1, c2 = st.columns(2)
with c1:
    if st.button("Découvrir comment ça marche", use_container_width=True):
        go_to_page("Comment_ca_marche.py")
with c2:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        go_to_page("Creer_un_envoi_securise.py")

# -----------------------------------------------------
# POINTS CLES
# -----------------------------------------------------
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.subheader("Points clés")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-box">100% sécurisé</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-box">Accès unique et contrôlé</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-box">Programmation possible</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-box">Notaire intégré</div>', unsafe_allow_html=True)

# -----------------------------------------------------
# 4 PILIERS
# -----------------------------------------------------
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.subheader("Les 4 piliers Kidan Vid")

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pillar-card" title="Messages vidéo personnels, programmés et délivrés au bon moment.">
            <div class="pillar-icon">🎥</div>
            <div class="pillar-title">Vidéo</div>
            <div class="pillar-text">
                Messages vidéo personnels programmés et délivrés au bon moment.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        """
        <div class="pillar-card" title="Souvenirs vocaux, témoignages sonores et compléments de transmission.">
            <div class="pillar-icon">🎙️</div>
            <div class="pillar-title">Audio</div>
            <div class="pillar-text">
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
        <div class="pillar-card" title="Protection technique : chiffrement, double authentification et traçabilité.">
            <div class="pillar-icon">🛡️</div>
            <div class="pillar-title">Sécurisation</div>
            <div class="pillar-text">
                Protection technique : chiffrement, double authentification et traçabilité.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p4:
    st.markdown(
        """
        <div class="pillar-card" title="Le pilier juridique central pour articuler la transmission avec le droit.">
            <div class="pillar-icon">⚖️</div>
            <div class="pillar-title">Notaires</div>
            <div class="pillar-text">
                Le pilier juridique central pour articuler la transmission avec le droit.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------
# TEMOIGNAGE
# -----------------------------------------------------
st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)
st.subheader("Témoignage")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

# -----------------------------------------------------
# ACCES RAPIDES
# -----------------------------------------------------
st.markdown("---")
st.subheader("Accès rapides")

q1, q2, q3, q4 = st.columns(4)
with q1:
    if st.button("Qui sommes-nous", use_container_width=True, key="quick_about"):
        go_to_page("Qui_sommes_nous.py")
with q2:
    if st.button("Nous contacter", use_container_width=True, key="quick_contact"):
        go_to_page("Nous_contacter.py")
with q3:
    if st.button("Informations légales", use_container_width=True, key="quick_info"):
        go_to_page("Informations_legales.py")
with q4:
    if st.button("Mentions légales", use_container_width=True, key="quick_mentions"):
        go_to_page("Mentions_legales.py")

# -----------------------------------------------------
# CONNEXION
# -----------------------------------------------------
st.markdown("---")
st.subheader("Connexion")
st.write("Accédez à votre espace sécurisé.")

st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer", use_container_width=True, key="btn_continue_home"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire", use_container_width=True, key="btn_benef_home"):
        go_to_page("Acces_beneficiaire.py")

st.markdown("---")
st.caption("© Kidan Vid")
