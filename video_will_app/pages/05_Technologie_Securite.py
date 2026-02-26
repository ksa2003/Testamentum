import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Technologie & Sécurité")

s = get_slide(13)

st.title("Technologie & sécurité")

if s:
    img(s.image_path)
else:
    st.warning("Slide introuvable.")
