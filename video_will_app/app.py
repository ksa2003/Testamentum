import base64
from pathlib import Path

import streamlit as st

# -----------------------------
# Config
# -----------------------------
st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

BLUE_MAIN = "#0A66C2"     # inspiré du bleu LinkedIn
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"
TEXT_DARK = "#12344D"


# -----------------------------
# Helpers
# -----------------------------
def show_logo_html(path: Path):
    if not path.exists():
        st.warning(f"Logo introuvable : {path}")
        return
    data = base64.b64encode(path.read_bytes()).decode("utf-8")
    ext = path.suffix.lower().replace(".", "") or "png"
    st.markdown(
        f"""
        <div class="hero-logo-wrap">
            <img class="hero-logo" src="data:image/{ext};base64,{data}" alt="Kidan Vid">
        </div>
        """,
        unsafe_allow_html=True,
    )


def go_to_page(page_filename: str):
    try:
        st.switch_page(f"pages/{page_filename}")
    except Exception:
        st.info("Utilisez le menu à gauche pour naviguer.")


def section_link_button(label: str, filename: str, key: str):
    if st.button(label, use_container_width=True, key=key):
        go_to_page(filename)


# -----------------------------
# Styles
# -----------------------------
st.markdown(
    f"""
    <style>
      :root {{
        --blue-main: {BLUE_MAIN};
        --blue-dark: {BLUE_DARK};
        --blue-soft: {BLUE_SOFT};
        --text-dark: {TEXT_DARK};
      }}

      .block-container {{
        max-width: 1180px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
      }}

      a.anchor-link {{
        display: none !important;
      }}

      .hero-logo-wrap {{
        display: flex;
        justify-content: center;
        margin-bottom: 1rem;
      }}

      .hero-logo {{
        max-width: 820px;
        width: 100%;
        height: auto;
        display: block;
      }}

      .topbar {{
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:16px;
        padding:12px 14px;
        background:#ffffff;
        border:1px solid rgba(10,102,194,0.14);
        border-radius:16px;
        margin-bottom:18px;
      }}

      .topbar-left {{
        font-weight:700;
        color:var(--blue-dark);
        font-size:1.05rem;
      }}

      .topbar-right {{
        color:#4c657d;
        font-size:0.96rem;
      }}

      .hero-box {{
        background: linear-gradient(180deg, #ffffff 0%, var(--blue-soft) 100%);
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 20px;
        padding: 26px;
        margin-bottom: 1.4rem;
      }}

      .legal-box {{
        border-left: 5px solid var(--blue-main);
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}

      .section-box {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 16px;
        padding: 18px;
        background: #fff;
        margin-bottom: 18px;
      }}

      .stats-grid {{
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:14px;
        margin: 14px 0 18px 0;
      }}

      .stat-card {{
        border-radius:14px;
        background:#fff;
        border:1px solid rgba(10,102,194,0.14);
        padding:16px;
        text-align:center;
        color:var(--text-dark);
        font-weight:600;
      }}

      .k-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 18px;
        margin-bottom: 22px;
      }}

      .k-card {{
        position: relative;
        border-radius: 16px;
        border: 1px solid rgba(10,102,194,0.18);
        background: white;
        min-height: 175px;
        padding: 16px;
        overflow: hidden;
        transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
      }}

      .k-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(10,102,194,0.14);
        border-color: rgba(10,102,194,0.32);
      }}

      .k-icon {{
        width: 58px;
        height: 58px;
        border-radius: 999px;
        background: var(--blue-soft);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 12px;
        font-size: 28px;
      }}

      .k-title {{
        font-weight: 700;
        color: var(--blue-dark);
        margin-bottom: 6px;
      }}

      .k-hover {{
        color: #28435f;
        font-size: 0.95rem;
        line-height: 1.35;
      }}

      .yt-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
      }}

      .yt-card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        padding: 12px;
        background: white;
      }}

      .footer-wrap {{
        background:#0f1d2b;
        color:#f5f7fb;
        border-radius:22px;
        padding:26px 20px;
        margin-top:28px;
      }}

      .footer-grid {{
        display:grid;
        grid-template-columns:repeat(4,1fr);
        gap:22px;
      }}

      .footer-title {{
        font-weight:700;
        margin-bottom:10px;
        color:#ffffff;
      }}

      .footer-item {{
        color:#d9e3ee;
        margin-bottom:8px;
        font-size:0.95rem;
      }}

      .footer-small {{
        color:#c7d3df;
        font-size:0.92rem;
        margin-top:18px;
        line-height:1.45;
      }}

      .footer-cta {{
        margin-top:20px;
      }}

      .bottom-login {{
        border: 1px solid rgba(10,102,194,0.18);
        border-radius: 16px;
        padding: 18px;
        background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
      }}

      @media (max-width: 980px) {{
        .k-grid {{
          grid-template-columns: repeat(2, 1fr);
        }}
        .yt-grid {{
          grid-template-columns: 1fr;
        }}
        .stats-grid {{
          grid-template-columns: repeat(2,1fr);
        }}
        .footer-grid {{
          grid-template-columns:repeat(2,1fr);
        }}
      }}

      @media (max-width: 640px) {{
        .k-grid {{
          grid-template-columns: 1fr;
        }}
        .stats-grid {{
          grid-template-columns: 1fr;
        }}
        .footer-grid {{
          grid-template-columns:1fr;
        }}
        .topbar {{
          flex-direction:column;
          align-items:flex-start;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Top quick access
# -----------------------------
st.markdown(
    """
    <div class="topbar">
        <div class="topbar-left">Kidan Vid</div>
        <div class="topbar-right">
            Transmission vidéo sécurisée · Audio · Sécurité · Notaires
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Hero
# -----------------------------
show_logo_html(LOGO_PATH)

st.markdown(
    """
    <div class="hero-box">
        <h1 style="margin-bottom:8px;color:#084C95;">Kidan Vid</h1>
        <div style="font-size:1.1rem;color:#143b63;margin-bottom:8px;">
            Plateforme de transmission vidéo, audio et documentaire sécurisée.
        </div>
        <div style="font-size:1.05rem;color:#183650;">
            Envoyez des messages personnels en toute confidentialité.
            Vidéos, audios, documents et accès bénéficiaire sont organisés dans une logique
            humaine, technique et juridique.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    section_link_button("Découvrir comment ça marche", "Comment_ca_marche.py", "home_how")
with c2:
    section_link_button("Créer un envoi sécurisé", "Creer_un_envoi_securise.py", "home_create")

st.markdown(
    """
    <div class="stats-grid">
        <div class="stat-card">100% sécurisé</div>
        <div class="stat-card">Accès unique et contrôlé</div>
        <div class="stat-card">Programmation possible</div>
        <div class="stat-card">Notaire intégré</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 4 piliers / 4 logos conceptuels
# -----------------------------
st.markdown("## Les 4 piliers Kidan Vid")
st.markdown(
    """
    <div class="k-grid">
        <div class="k-card" title="Transmission vidéo sécurisée, lecture contrôlée et accès traçable.">
            <div class="k-icon">🎥</div>
            <div class="k-title">Vidéo</div>
            <div class="k-hover">
                Messages vidéo personnels, programmés et délivrés au bon moment.
            </div>
        </div>
        <div class="k-card" title="Enregistrements audio, messages vocaux et mémoire sonore.">
            <div class="k-icon">🎙️</div>
            <div class="k-title">Audio</div>
            <div class="k-hover">
                Souvenirs vocaux, témoignages sonores et compléments de transmission.
            </div>
        </div>
        <div class="k-card" title="Chiffrement, journalisation, OTP, 2FA, limitation des accès.">
            <div class="k-icon">🛡️</div>
            <div class="k-title">Sécurisation</div>
            <div class="k-hover">
                Protection technique : chiffrement, double authentification et traçabilité.
            </div>
        </div>
        <div class="k-card" title="La vidéo seule n’a pas de valeur testamentaire en France. Le notaire structure juridiquement la transmission.">
            <div class="k-icon">⚖️</div>
            <div class="k-title">Notaires</div>
            <div class="k-hover">
                Le pilier juridique central pour articuler la transmission avec le droit.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Témoignages
# -----------------------------
st.markdown("## Témoignages")
st.markdown(
    """
    <div class="yt-grid">
        <div class="yt-card">
            <div style="font-weight:700;color:#084C95;margin-bottom:8px;">Transmission vidéo</div>
    """,
    unsafe_allow_html=True,
)
st.video("https://www.youtube.com/watch?v=RwQvEs_PkKA")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
        <div class="yt-card">
            <div style="font-weight:700;color:#084C95;margin-bottom:8px;">Sécurité et identité</div>
    """,
    unsafe_allow_html=True,
)
st.video("https://www.youtube.com/watch?v=ZvaCqzKAy7U")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
        <div class="yt-card">
            <div style="font-weight:700;color:#084C95;margin-bottom:8px;">Mémoire audio et émotion</div>
    """,
    unsafe_allow_html=True,
)
st.video("https://www.youtube.com/watch?v=jr_mf05iJkE")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
        <div class="yt-card">
            <div style="font-weight:700;color:#084C95;margin-bottom:8px;">Cadre notarial</div>
    """,
    unsafe_allow_html=True,
)
st.video("https://www.youtube.com/watch?v=bkOKj_hWCj4")
st.markdown("</div></div>", unsafe_allow_html=True)

# -----------------------------
# Raccourcis inspiration portail
# -----------------------------
st.markdown("---")
st.markdown("## Accès rapides")

r1, r2, r3, r4 = st.columns(4)
with r1:
    section_link_button("Qui sommes-nous", "Qui_sommes_nous.py", "quick_about")
with r2:
    section_link_button("Nous contacter", "Nous_contacter.py", "quick_contact")
with r3:
    section_link_button("Informations légales", "Informations_legales.py", "quick_info_legal")
with r4:
    section_link_button("Mentions légales", "Mentions_legales.py", "quick_mentions")

# -----------------------------
# Connexion en bas
# -----------------------------
st.markdown("---")
st.markdown('<div class="bottom-login">', unsafe_allow_html=True)
st.header("Connexion")
st.write("Accédez à votre espace sécurisé.")

st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")

b1, b2 = st.columns(2)
with b1:
    if st.button("Continuer", use_container_width=True, key="home_continue"):
        go_to_page("Connexion.py")
with b2:
    if st.button("Accès bénéficiaire", use_container_width=True, key="home_benef"):
        go_to_page("Acces_beneficiaire.py")

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Footer inspiré structure portail
# -----------------------------
st.markdown(
    """
    <div class="footer-wrap">
        <div class="footer-grid">
            <div>
                <div class="footer-title">Offres & Services</div>
                <div class="footer-item">Créer un envoi sécurisé</div>
                <div class="footer-item">Espace Mémoire</div>
                <div class="footer-item">Accès bénéficiaire</div>
                <div class="footer-item">Témoignages</div>
            </div>
            <div>
                <div class="footer-title">Abonné</div>
                <div class="footer-item">Connexion</div>
                <div class="footer-item">Documents</div>
                <div class="footer-item">Vidéos</div>
                <div class="footer-item">Paramètres</div>
            </div>
            <div>
                <div class="footer-title">Aide & Contact</div>
                <div class="footer-item">Nous contacter</div>
                <div class="footer-item">Informations légales</div>
                <div class="footer-item">Mentions légales</div>
                <div class="footer-item">FAQ / Sécurité technique</div>
            </div>
            <div>
                <div class="footer-title">Société</div>
                <div class="footer-item">Qui sommes-nous</div>
                <div class="footer-item">Pourquoi Kidan Vid</div>
                <div class="footer-item">Notaire en ligne</div>
                <div class="footer-item">Cas d’usage</div>
            </div>
        </div>
        <div class="footer-small">
            Kidan Vid organise une transmission numérique sécurisée de messages, souvenirs et documents.
            En France, une vidéo seule ne constitue pas un testament juridiquement valable :
            l’intervention du notaire reste un pilier central.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("© Kidan Vid")
