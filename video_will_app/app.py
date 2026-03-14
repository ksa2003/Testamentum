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


def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return

    logo_bytes = path.read_bytes()
    encoded = base64.b64encode(logo_bytes).decode()

    st.markdown(
        f"""
        <div class="hero-logo-wrap">
            <img src="data:image/png;base64,{encoded}" class="hero-logo" alt="Logo Kidanmemoris">
        </div>
        """,
        unsafe_allow_html=True,
    )


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


st.markdown(
    f"""
    <style>
    .block-container {{
        max-width: 1180px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }}

    .hero-logo-wrap {{
        width: 100%;
        max-width: 980px;
        margin: 0 auto 1.2rem auto;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .hero-logo {{
        width: 100%;
        max-width: 980px;
        height: auto;
        display: block;
        border-radius: 22px;
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

    @media (max-width: 900px) {{
        .block-container {{
            padding-top: 0.8rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .hero-logo {{
            border-radius: 18px;
        }}

        .hero-title {{
            font-size: 2rem;
        }}

        .hero-sub {{
            font-size: 1.08rem;
        }}

        .hero-box {{
            padding: 20px;
        }}
    }}

    @media (max-width: 640px) {{
        .hero-logo-wrap {{
            margin-bottom: 1rem;
        }}

        .hero-logo {{
            border-radius: 14px;
        }}

        .hero-title {{
            font-size: 1.75rem;
            line-height: 1.2;
        }}

        .hero-sub {{
            font-size: 1rem;
            line-height: 1.5;
        }}

        .hero-text {{
            font-size: 0.98rem;
        }}

        .hero-box {{
            padding: 18px;
            border-radius: 16px;
        }}

        .stat-box {{
            min-height: auto;
        }}
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

st.markdown("---")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.caption("© Kidanmemoris")
