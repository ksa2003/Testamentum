import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s4 = get_slide(4)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Modèle économique</div>
      <div class="tm-sub">Formules et offres (particuliers, notaires, entreprises)</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s4.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Résumé</div>
  <p>{s4.text}</p>
</div>
""",
    unsafe_allow_html=True,
)
