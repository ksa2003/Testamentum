import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s5 = get_slide(5)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">L’Alliance</div>
      <div class="tm-sub">Transformer l’héritage en présence</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s5.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Extrait</div>
  <p>{s5.text}</p>
</div>
""",
    unsafe_allow_html=True,
)
