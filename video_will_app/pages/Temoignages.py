import streamlit as st
from pathlib import Path
from PIL import Image

# -----------------------------
# Config
# -----------------------------
st.set_page_config(page_title="Témoignages", layout="centered")

BASE_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# -----------------------------
# Helpers
# -----------------------------

def yt_id(url: str) -> str | None:
    """
    Extrait l'ID d'une URL YouTube (formats courants).
    """
    try:
        if "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0].split("&")[0]
        if "watch?v=" in url:
            return url.split("watch?v=")[1].split("&")[0]
        if "/embed/" in url:
            return url.split("/embed/")[1].split("?")[0].split("&")[0]
        return None
    except Exception:
        return None

def yt_thumb(url: str) -> str:
    vid = yt_id(url)
    if not vid:
        # fallback générique (affiche une image neutre si ID non parsé)
        return "https://i.imgur.com/8Q2QZ4B.png"
    return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"

def video_card(title: str, subtitle: str, url: str):
    thumb = yt_thumb(url)
    st.markdown(
        f"""
        <div class="card">
          <a class="thumb-link" href="{url}" target="_blank" rel="noopener noreferrer">
            <img class="thumb" src="{thumb}" alt="{title}">
            <div class="play">▶</div>
          </a>
          <div class="card-body">
            <div class="card-title">{title}</div>
            <div class="card-subtitle">{subtitle}</div>
            <div class="card-actions">
              <a class="btn" href="{url}" target="_blank" rel="noopener noreferrer">Voir la vidéo</a>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Styles (look "site vitrine")
# -----------------------------
st.markdown(
    """
    <style>
      .block-container { max-width: 1000px; padding-top: 1.4rem; padding-bottom: 2.5rem; }
      h1, h2 { letter-spacing: -0.02em; }
      .subtle { color: rgba(0,0,0,0.6); font-size: 0.98rem; margin-top: -0.6rem; }

      .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 18px;
      }

      .card {
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 14px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
      }

      .thumb-link { position: relative; display:block; }
      .thumb {
        width: 100%;
        height: 170px;
        object-fit: cover;
        display:block;
      }
      .play {
        position: absolute;
        inset: 0;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size: 44px;
        color: rgba(255,255,255,0.92);
        text-shadow: 0 8px 20px rgba(0,0,0,0.35);
        opacity: 0.92;
      }

      .card-body { padding: 14px 14px 16px 14px; }
      .card-title { font-weight: 700; font-size: 1.02rem; margin-bottom: 6px; }
      .card-subtitle { color: rgba(0,0,0,0.62); font-size: 0.92rem; line-height: 1.35; min-height: 44px; }

      .card-actions { margin-top: 12px; }
      .btn {
        display:inline-block;
        padding: 9px 12px;
        border-radius: 10px;
        border: 1px solid rgba(0,0,0,0.14);
        text-decoration: none;
        color: rgba(0,0,0,0.78);
        font-weight: 600;
        background: rgba(255,255,255,0.7);
      }
      .btn:hover { border-color: rgba(0,0,0,0.22); }

      .section {
        margin-top: 34px;
        padding-top: 10px;
        border-top: 1px solid rgba(0,0,0,0.06);
      }

      @media (max-width: 980px) {
        .grid { grid-template-columns: repeat(2, 1fr); }
        .thumb { height: 185px; }
      }
      @media (max-width: 640px) {
        .grid { grid-template-columns: 1fr; }
        .thumb { height: 200px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Content
# -----------------------------
show_logo(width=520)

st.title("Témoignages")
st.markdown(
    '<div class="subtle">Des retours d’expérience autour de la transmission, des messages vidéo et de l’héritage numérique.</div>',
    unsafe_allow_html=True,
)

# Ces liens sont des exemples "au hasard".
# Remplace-les par tes propres vidéos / playlists dès que tu as ta sélection.
VIDEOS = [
    {
        "title": "Transmettre un message vidéo dans le temps",
        "subtitle": "Retour d’expérience sur les messages programmés et l’héritage numérique.",
        "url": "https://youtu.be/RwQvEs_PkKA?is=IsEVaW19icHYNTVF",
    },
    {
        "title": "Protéger l’accès à une vidéo privée",
        "subtitle": "Témoignage sur la confidentialité, l’accès contrôlé et la sécurité.",
        "url": "https://youtu.be/oRVvi5xWF1k?is=jp3m7ZNh0adm3xd3",
    },
    {
        "title": "Mémoire familiale et transmission",
        "subtitle": "Partager des souvenirs et documents avec un accès réservé.",
        "url": "https://youtu.be/jr_mf05iJkE?is=s4Vtm3VJThW1QZ0H",
    },
    {
        "title": "Préparer la succession numérique",
        "subtitle": "Approche pratique : documents, bénéficiaires et organisation.",
        "url": "https://youtu.be/bkOKj_hWCj4?is=-KzbtU_4nRh1zaVs",
    },
    {
        "title": "Accès bénéficiaire sécurisé",
        "subtitle": "Comment limiter l’accès dans le temps et tracer les ouvertures.",
        "url": "https://youtu.be/qk4XuiQGAtw?is=aRGdwKJ7DIMVThuC",
    },
    {
        "title": "KYC / Vérification d’identité simplifiée",
        "subtitle": "Pourquoi vérifier l’identité renforce la sécurité globale.",
        "url": "https://youtu.be/ZvaCqzKAy7U?is=0_6qavo5nZK5YGN3",
    },
]

# Grille 3 colonnes via HTML (plus proche d’un site vitrine)
st.markdown('<div class="grid">', unsafe_allow_html=True)
for v in VIDEOS:
    # injecte chaque card dans la grille
    # (Streamlit ne permet pas d’insérer directement du HTML dans une boucle en gardant la grille,
    #  donc on rend la card en HTML avec markdown)
    st.markdown('<div>', unsafe_allow_html=True)
    video_card(v["title"], v["subtitle"], v["url"])
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section “Plus de témoignages”
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("Plus de témoignages")

col1, col2 = st.columns(2)
with col1:
    st.video("https://youtu.be/DBzO5rDAVPw?is=1PhdxiKR2TbLBBMV")
with col2:
    st.video("https://youtu.be/6g0MA6tMlvU?is=avnHaWqL7_nIPIUw")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")

st.caption("© Kidan Vid")
