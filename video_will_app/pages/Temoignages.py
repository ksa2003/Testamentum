import streamlit as st

st.set_page_config(page_title="Témoignages", layout="wide")

st.title("Témoignages")

st.write(
"Retours d’expérience autour de la transmission vidéo, de la mémoire audio, de la sécurité et du cadre notarial."
)

st.warning(
"""
Point juridique important

En France, une vidéo seule ne constitue pas un testament juridiquement valable.
Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
"""
)

videos = [
    {
        "titre": "Transmission vidéo",
        "texte": "Message vidéo et transmission personnelle.",
        "url": "https://www.youtube.com/watch?v=RwQvEs_PkKA",
    },
    {
        "titre": "Souvenirs et voix",
        "texte": "L’importance émotionnelle de la parole enregistrée.",
        "url": "https://www.youtube.com/watch?v=jr_mf05iJkE",
    },
    {
        "titre": "Protection et accès",
        "texte": "Contrôle d’accès et confidentialité.",
        "url": "https://www.youtube.com/watch?v=ZvaCqzKAy7U",
    },
    {
        "titre": "Succession et cadre juridique",
        "texte": "Pourquoi le notaire reste central.",
        "url": "https://www.youtube.com/watch?v=bkOKj_hWCj4",
    },
]

for v in videos:
    st.video(v["url"])
    st.subheader(v["titre"])
    st.write(v["texte"])
    st.markdown("---")
