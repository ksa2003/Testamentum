import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — L’alliance")

s = get_slide(14)
st.title("L’alliance")
st.write(s.text)
img(str(s.image_path), use_container_width=True)
