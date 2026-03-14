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


def show_logo(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    try:
        img = Image.open(path)
        st.image(img, use_container_width=True)
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

    /* Améliore l'affichage de l'image du haut */
    [data-testid="stImage"] img {{
        border-radius: 20px;
        height: auto;
        object-fit: contain;
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

    @media (max-width: 900px) {{
        .block-container {{
            padding-top: 0.8rem;
            padding-left: 1rem;
            padding-right: 1rem;
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

        .pillar-card {{
            min-height: 220px;
        }}
    }}

    @media (max-width: 640px) {{
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

        .pillar-card {{
            min-height: auto;
        }}

        .stat-box,
        .example-box {{
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
st.subheader("Les 4 piliers Kidanmemoris")

p1, p2 = st.columns(2)
with p1:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-icon">🎥</div>
            <div class="pillar-title">Messages vidéo</div>
            <div class="pillar-text">
                Enregistrez un message pour un enfant, un partenaire ou toute la famille.
                Il peut être enregistré maintenant, téléversé, ou reprogrammé.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p2:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-icon">⏳</div>
            <div class="pillar-title">Moments de vie</div>
            <div class="pillar-text">
                Programmez une transmission pour un mariage, une naissance,
                un baptême, un anniversaire important, une réussite scolaire
                ou après confirmation de décès.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

p3, p4 = st.columns(2)
with p3:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-icon">🌳</div>
            <div class="pillar-title">Arbre de mémoire familiale</div>
            <div class="pillar-text">
                Chaque famille peut créer un arbre familial et associer des messages
                pour chaque génération afin de construire une mémoire familiale numérique.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with p4:
    st.markdown(
        """
        <div class="pillar-card">
            <div class="pillar-icon">⚖️</div>
            <div class="pillar-title">Patrimoine émotionnel et juridique</div>
            <div class="pillar-text">
                Le coffre peut intégrer une logique de succession :
                notaire partenaire, dossier patrimonial, ou vidéo associée
                à un testament.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("Exemples de transmissions")

e1, e2, e3 = st.columns(3)
with e1:
    st.markdown(
        """
        <div class="example-box">
            <div class="example-title">Pour les 18 ans d’un enfant</div>
            Un message à découvrir le jour de sa majorité.
        </div>
        """,
        unsafe_allow_html=True,
    )
with e2:
    st.markdown(
        """
        <div class="example-box">
            <div class="example-title">Pour un mariage futur</div>
            “À regarder le jour de ton mariage.”
        </div>
        """,
        unsafe_allow_html=True,
    )
with e3:
    st.markdown(
        """
        <div class="example-box">
            <div class="example-title">Pour après-décès</div>
            Une transmission émotionnelle sécurisée avec confirmation.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("Témoignage")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

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
    if st.button("Notaire en ligne", use_container_width=True, key="quick_notaire"):
        go_to_page("Notaire_en_ligne.py")

st.markdown("---")
st.caption("© Kidanmemoris")
