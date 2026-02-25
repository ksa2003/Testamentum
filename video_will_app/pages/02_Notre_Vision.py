import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s12 = get_slide(12)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Notre vision</div>
      <div class="tm-sub">Humaniser la succession</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s12.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Résumé</div>
  <p>{s12.text}</p>
</div>
""",
    unsafe_allow_html=True,
)
