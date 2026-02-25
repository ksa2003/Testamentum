import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Page 1")

s = get_slide(1)

if s:
    img(s.image_path, use_container_width=True)
else:
    st.error("Slide 1 introuvable dans kidan_content.py")
