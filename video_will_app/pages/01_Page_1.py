import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid")

s = get_slide(1)
st.title("Page 1")

if s and getattr(s, "image_path", None):
    img(s.image_path, use_container_width=True)
else:
    st.warning("Slide 1 introuvable.")
