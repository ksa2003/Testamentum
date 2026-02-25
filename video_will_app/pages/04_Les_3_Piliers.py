import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s14 = get_slide(14)
s15 = get_slide(15)
s7 = get_slide(7)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Les 3 piliers</div>
      <div class="tm-sub">Émotion • Juridique • Transmission</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s14.image_path, use_container_width=True)
st.markdown(f"**Émotion (extrait PDF)** : {s14.text}")

st.image(s15.image_path, use_container_width=True)
st.markdown(f"**Juridique (extrait PDF)** : {s15.text}")

st.image(s7.image_path, use_container_width=True)
st.markdown(f"**Transmission (extrait PDF)** : {s7.text}")
