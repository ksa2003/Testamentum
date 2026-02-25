import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s3 = get_slide(3)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Modèle</div>
      <div class="tm-sub">Système en 3 niveaux</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s3.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Résumé</div>
  <p>{s3.text}</p>
</div>
""",
    unsafe_allow_html=True,
)
