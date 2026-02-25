import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s1 = get_slide(1)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Page 1</div>
      <div class="tm-sub">Référence visuelle (couverture du dossier)</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s1.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Texte (extrait du PDF)</div>
  <p>{s1.text}</p>
</div>
""",
    unsafe_allow_html=True,
)
