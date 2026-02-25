import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Marché & opportunité")

s = get_slide(5)
st.title("Marché & opportunité")
st.write(s.text)
img(str(s.image_path), use_container_width=True)
