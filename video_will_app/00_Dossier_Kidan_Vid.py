import streamlit as st

from kidan_content import all_slides
from theme import apply_theme


apply_theme()

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Dossier Kidan Vid</div>
      <p class="tm-muted">
        Retrouvez ici les visuels du PDF (slides) et une transcription lisible des informations.
        Les images font foi (contenu source du document).
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

for s in all_slides():
    with st.expander(f"Page {s.page:02d} — {s.title}", expanded=(s.page == 1)):
        st.image(s.image_path, use_container_width=True)
        st.markdown(f"**Résumé (texte extrait du PDF)** : {s.text}")
