import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Technologie & sécurité")

s = get_slide(13)
st.title("Technologie & sécurité")
st.write(s.text)
img(str(s.image_path), use_container_width=True)
