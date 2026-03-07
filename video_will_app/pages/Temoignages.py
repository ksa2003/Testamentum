import streamlit as st

st.set_page_config(page_title="Témoignages", layout="wide")

st.markdown("""
<style>
.stApp{
    background: linear-gradient(180deg,#0b2240 0%,#091a31 100%);
}

html, body, [class*="css"]{
    color:white !important;
}

.block-container{
    max-width: 1100px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

h1,h2,h3{
    color:white !important;
}

p, li, label, span{
    color:#eef4fb !important;
}

a.anchor-link{
    display:none !important;
}

/* bloc juridique */
.legal-box{
    background:#21406b;
    border-left:5px solid #58a6ff;
    padding:18px;
    border-radius:12px;
    margin:18px 0 28px 0;
    box-shadow:0 8px 20px rgba(0,0,0,0.14);
}

.legal-title{
    color:#ffffff !important;
    font-size:1.05rem;
    font-weight:800;
    margin-bottom:10px;
}

.legal-text{
    color:#ffffff !important;
    font-size:1rem;
    line-height:1.75;
    font-weight:500;
}

/* cartes vidéos */
.video-card{
    background:#f7f9fc;
    border-radius:18px;
    overflow:hidden;
    margin:20px 0 28px 0;
    box-shadow:0 10px 24px rgba(0,0,0,0.18);
    border:1px solid rgba(255,255,255,0.08);
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

/* bouton lien */
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

.video-link:hover{
    background:#dfeeff;
    color:#185ec0 !important;
}

footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("Témoignages")
st.write("Retours d’expérience autour de la transmission vidéo, de la mémoire audio, de la sécurité et du cadre notarial.")

st.markdown("""
<div class="legal-box">
    <div class="legal-title">Point juridique important</div>
    <div class="legal-text">
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
</div>
""", unsafe_allow_html=True)

videos = [
    {
        "titre": "Transmission vidéo",
        "texte": "Message vidéo, temporalité et transmission personnelle.",
        "url": "https://www.youtube.com/watch?v=RwQvEs_PkKA",
    },
    {
        "titre": "Souvenirs et voix",
        "texte": "L’importance émotionnelle de la parole enregistrée.",
        "url": "https://www.youtube.com/watch?v=jr_mf05iJkE",
    },
    {
        "titre": "Protection et accès",
        "texte": "Contrôle d’accès, confidentialité et identité.",
        "url": "https://www.youtube.com/watch?v=ZvaCqzKAy7U",
    },
    {
        "titre": "Succession et cadre juridique",
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
