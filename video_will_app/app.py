import streamlit as st
from pathlib import Path
import base64

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


def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    try:
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        st.markdown(
            f"""
            <div class="hero-logo-wrap">
                <img src="data:image/png;base64,{encoded}" class="hero-logo">
            </div>
            """,
            unsafe_allow_html=True,
        )
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
        padding-top: 1rem;
    }}

    .hero-logo-wrap {{
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 1rem;
    }}

    .hero-logo {{
        width: 100%;
        max-width: 900px;
        height: auto;
        border-radius: 20px;
    }}

    .hero-box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 20px;
        padding: 24px;
        background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
        margin-bottom: 18px;
    }}

    .hero-title {{
        font-size: 2.2rem;
        font-weight: 800;
        color: {BLUE_DARK};
    }}

    .hero-sub {{
        font-size: 1.15rem;
        font-weight: 700;
        color: {BLUE_DARK};
        margin-top: 6px;
    }}

    .hero-text {{
        margin-top: 12px;
        line-height: 1.7;
        color: #27435f;
    }}

    .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 22px;
    }}

    .stat-box {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        background: #ffffff;
        padding: 14px;
        text-align: center;
        font-weight: 700;
        color: {BLUE_DARK};
    }}

    .pillar-card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 18px;
        background: {CARD_BG};
        padding: 22px;
        margin-bottom: 18px;
    }}

    .pillar-title {{
        font-size: 1.3rem;
        font-weight: 800;
        color: {BLUE_DARK};
    }}

    .pillar-text {{
        color: #3e5974;
        margin-top: 8px;
    }}

    .example-box {{
        border: 1px solid rgba(10,102,194,0.12);
        border-radius: 16px;
        background: #ffffff;
        padding: 18px;
        margin-bottom: 10px;
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
            La plateforme permet de transmettre des messages vidéo,
            souvenirs familiaux et lettres numériques pour les moments de vie.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <b>Point juridique important</b><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris intègre le notaire pour sécuriser toute transmission successorale.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    if st.button("Créer mon coffre"):
        go_to_page("Connexion.py")
with c2:
    if st.button("Se connecter"):
        go_to_page("Connexion.py")

st.markdown("---")
st.subheader("Points clés")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-box">Coffre sécurisé</div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-box">Transmission programmée</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-box">Famille & héritiers</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-box">Notaire intégré</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("Les piliers")

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-title">Messages vidéo</div>
            <div class="pillar-text">Transmission émotionnelle différée.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-title">Moments de vie</div>
            <div class="pillar-text">Mariage, naissance, décès.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("Témoignage")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.markdown("---")
st.caption("© Kidanmemoris")
