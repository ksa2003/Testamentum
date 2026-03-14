import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Kidanmemoris",
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


# LOGO UNIVERSAL FIX (toutes versions streamlit)
def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    try:
        img = Image.open(path)
        st.image(img, width=1100)
    except Exception as e:
        st.error(f"Impossible de charger le logo : {e}")


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


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
        font-size: 2.3rem;
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 10px;
    }}

    .hero-sub {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {BLUE_DARK};
        margin-bottom: 12px;
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
        min-height: 240px;
        box-shadow: 0 8px 22px rgba(10,102,194,0.06);
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
        font-size: 1.4rem;
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 10px;
    }}

    .pillar-text {{
        color: #3e5974;
        font-size: 1rem;
        line-height: 1.7;
    }}

    .example-box {{
        border: 1px solid rgba(10,102,194,0.12);
        border-radius: 16px;
        background: #ffffff;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(10,102,194,0.04);
        height: 100%;
    }}

    .example-title {{
        font-weight: 800;
        color: {BLUE_DARK};
        margin-bottom: 8px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

show_logo(LOGO_PATH)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">Kidanmemoris</div>
        <div class="hero-sub">Les mots les plus importants sont parfois ceux que l’on laisse.</div>
        <div class="hero-text">
            Kidanmemoris est le coffre du patrimoine émotionnel.
            La plateforme permet de transmettre des messages vidéo, des souvenirs familiaux,
            des lettres numériques et des messages pour des moments de vie futurs :
            mariage, naissance, baptême, anniversaire important, réussite scolaire
            ou après-décès.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <div class="legal-title">Point juridique important</div>
        <div>
            En France, une vidéo seule ne constitue pas un testament juridiquement valable.
            Kidanmemoris intègre le notaire comme pilier central pour sécuriser toute transmission
            à portée successorale.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    if st.button("Créer mon coffre Kidanmemoris", use_container_width=True):
        go_to_page("Connexion.py")
with c2:
    if st.button("Se connecter", use_container_width=True):
        go_to_page("Connexion.py")

st.markdown("---")
st.subheader("Points clés")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-box">Coffre numérique sécurisé</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-box">Transmission par moment de vie</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-box">Famille et destinataires</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-box">Intégration notariale</div>', unsafe_allow_html=True)

st.caption("© Kidanmemoris")
