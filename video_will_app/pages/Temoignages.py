import streamlit as st

st.set_page_config(page_title="Témoignages", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"

def yt_id(url: str):
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

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 1040px;
        padding-top: 1.4rem;
        padding-bottom: 2.8rem;
      }}
      a.anchor-link {{
        display: none !important;
      }}
      .subtle {{
        color: rgba(0,0,0,0.65);
        font-size: 0.98rem;
        margin-top: -0.4rem;
        margin-bottom: 1rem;
      }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
      .grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 18px;
      }}
      .card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
      }}
      .thumb-link {{
        position: relative;
        display:block;
      }}
      .thumb {{
        width: 100%;
        height: 170px;
        object-fit: cover;
        display:block;
      }}
      .play {{
        position: absolute;
        inset: 0;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size: 44px;
        color: rgba(255,255,255,0.92);
        text-shadow: 0 8px 20px rgba(0,0,0,0.35);
      }}
      .card-body {{
        padding: 14px;
      }}
      .card-title {{
        font-weight: 700;
        color:{BLUE_DARK};
        margin-bottom: 6px;
      }}
      .card-subtitle {{
        color: rgba(0,0,0,0.62);
        font-size: 0.92rem;
        line-height: 1.35;
        min-height: 44px;
      }}
      .btn {{
        display:inline-block;
        margin-top: 10px;
        padding: 9px 12px;
        border-radius: 10px;
        border: 1px solid rgba(10,102,194,0.18);
        text-decoration: none;
        color: {BLUE_DARK};
        font-weight: 600;
        background: #f7fbff;
      }}
      @media (max-width: 980px) {{
        .grid {{ grid-template-columns: repeat(2, 1fr); }}
      }}
      @media (max-width: 640px) {{
        .grid {{ grid-template-columns: 1fr; }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Témoignages")
st.markdown(
    '<div class="subtle">Retours d’expérience autour de la transmission vidéo, de la mémoire audio, de la sécurité et du cadre notarial.</div>',
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

VIDEOS = [
    {
        "title": "Transmission vidéo",
        "subtitle": "Message vidéo, temporalité et transmission personnelle.",
        "url": "https://youtu.be/RwQvEs_PkKA",
    },
    {
        "title": "Souvenirs et voix",
        "subtitle": "L’importance émotionnelle de la parole enregistrée.",
        "url": "https://youtu.be/jr_mf05iJkE",
    },
    {
        "title": "Protection et accès",
        "subtitle": "Contrôle d’accès, confidentialité et identité.",
        "url": "https://youtu.be/ZvaCqzKAy7U",
    },
    {
        "title": "Préparer la transmission",
        "subtitle": "Documents, bénéficiaires et organisation.",
        "url": "https://youtu.be/bkOKj_hWCj4",
    },
    {
        "title": "Sécuriser un accès bénéficiaire",
        "subtitle": "Limiter l’accès dans le temps et tracer les ouvertures.",
        "url": "https://youtu.be/qk4XuiQGAtw",
    },
    {
        "title": "Cadre juridique",
        "subtitle": "Pourquoi la transmission doit être encadrée.",
        "url": "https://youtu.be/oRVvi5xWF1k",
    },
]

st.markdown('<div class="grid">', unsafe_allow_html=True)
for v in VIDEOS:
    st.markdown("<div>", unsafe_allow_html=True)
    video_card(v["title"], v["subtitle"], v["url"])
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
