import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s9 = get_slide(9)
s10 = get_slide(10)
s11 = get_slide(11)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Marché &amp; opportunité</div>
      <div class="tm-sub">Pourquoi maintenant ?</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s9.image_path, use_container_width=True)
st.markdown(f"**Extrait PDF** : {s9.text}")

st.image(s10.image_path, use_container_width=True)
st.markdown(f"**Extrait PDF** : {s10.text}")

st.image(s11.image_path, use_container_width=True)
st.markdown(f"**Extrait PDF** : {s11.text}")
