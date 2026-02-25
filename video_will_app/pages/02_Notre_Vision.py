import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Titre de la page")

s = get_slide(X)

if s:
    img(s.image_path, use_container_width=True)
else:
    st.error("Slide X introuvable")
