import streamlit as st

st.set_page_config(page_title="Témoignages", layout="wide")

st.markdown(
    """
    <style>
    .block-container{
        max-width: 1100px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }
    a.anchor-link{
        display:none !important;
    }
    .legal-box{
        background:#f5faff;
        border-left:5px solid #58a6ff;
        padding:18px;
        border-radius:12px;
        margin:18px 0 28px 0;
    }
    .video-card{
        background:#f7f9fc;
        border-radius:18px;
        overflow:hidden;
        margin:20px 0 28px 0;
        box-shadow:0 10px 24px rgba(0,0,0,0.08);
        border:1px solid rgba(0,0,0,0.06);
    }
    .video-card-body{
        padding:18px 18px 12px 18px;
    }
    .video-title{
        color:#18457a !important;
        font-size:1.15rem;
        font-weight:800;
        margin-bottom:8px;
    }
    .video-text{
        color:#4b5a6d !important;
        font-size:1rem;
        line-height:1.65;
        margin-bottom:14px;
    }
    .video-link{
        display:inline-block;
        background:#eaf3ff;
        color:#2b7de9 !important;
        text-decoration:none;
        padding:10px 16px;
        border-radius:10px;
        font-weight:700;
        border:1px solid #d3e5ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Témoignages")
st.write("Retours d’expérience autour de la mémoire familiale, des messages programmés et du cadre sécurisé.")

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

videos = [
    {
        "titre": "Messages pour des moments de vie",
        "texte": "Un message destiné à un mariage, une naissance ou un anniversaire important.",
        "url": "https://www.youtube.com/watch?v=RwQvEs_PkKA",
    },
    {
        "titre": "Souvenirs et transmission familiale",
        "texte": "L’émotion d’une mémoire familiale qui traverse les générations.",
        "url": "https://www.youtube.com/watch?v=jr_mf05iJkE",
    },
    {
        "titre": "Protection et accès",
        "texte": "Contrôle d’accès, confidentialité et sécurité du coffre numérique.",
        "url": "https://www.youtube.com/watch?v=ZvaCqzKAy7U",
    },
    {
        "titre": "Patrimoine émotionnel et juridique",
        "texte": "Pourquoi l’accompagnement juridique et notarial reste central.",
        "url": "https://www.youtube.com/watch?v=bkOKj_hWCj4",
    },
]

for v in videos:
    st.markdown('<div class="video-card">', unsafe_allow_html=True)
    st.video(v["url"])
    st.markdown(
        f"""
        <div class="video-card-body">
            <div class="video-title">{v["titre"]}</div>
            <div class="video-text">{v["texte"]}</div>
            <a class="video-link" href="{v["url"]}" target="_blank">Voir la vidéo</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
