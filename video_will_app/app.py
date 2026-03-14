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

    logo_bytes = path.read_bytes()
    encoded = base64.b64encode(logo_bytes).decode()

    st.markdown(
        f"""
        <div class="hero-frame">
            <img src="data:image/png;base64,{encoded}" class="hero-logo">
        </div>
        """,
        unsafe_allow_html=True,
    )


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except:
        st.info("Utilisez le menu à gauche.")


st.markdown(f"""
<style>

.block-container {{
    max-width: 1180px;
    padding-top: 1rem;
}}

.hero-frame {{
    width: 100%;
    max-width: 980px;
    margin: 0 auto 1.2rem auto;
    border-radius: 22px;
    overflow: hidden;
    background: #071a63;
    aspect-ratio: 3 / 2;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.hero-logo {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 44%;
}}

.hero-box {{
    border: 1px solid rgba(10,102,194,0.16);
    border-radius: 20px;
    padding: 24px;
    background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
    margin-top: 6px;
}}

.hero-title {{
    font-size: 2.3rem;
    font-weight: 800;
    color: {BLUE_DARK};
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
    padding: 16px;
    border-radius: 12px;
    margin: 18px 0;
}}

.stat-box {{
    border: 1px solid rgba(10,102,194,0.14);
    border-radius: 14px;
    padding: 14px;
    text-align: center;
    font-weight: 700;
    color: {BLUE_DARK};
}}

@media (max-width: 900px) {{
    .hero-frame {{
        aspect-ratio: 4 / 3;
    }}
}}

@media (max-width: 640px) {{
    .hero-frame {{
        border-radius: 14px;
        aspect-ratio: 4 / 3;
    }}

    .hero-logo {{
        object-position: center 46%;
    }}
}}

</style>
""", unsafe_allow_html=True)

show_logo(LOGO_PATH)

st.markdown("""
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
""", unsafe_allow_html=True)

st.markdown("""
<div class="legal-box">
<b>Point juridique important</b><br>
En France, une vidéo seule ne constitue pas un testament juridiquement valable.
Kidanmemoris intègre le notaire comme pilier central.
</div>
""", unsafe_allow_html=True)

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
    st.markdown('<div class="stat-box">Transmission par moment</div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-box">Famille & destinataires</div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-box">Notaire intégré</div>', unsafe_allow_html=True)

st.markdown("---")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.caption("© Kidanmemoris")
