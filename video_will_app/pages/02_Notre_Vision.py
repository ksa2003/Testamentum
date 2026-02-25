import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Notre vision")

s = get_slide(2)
st.title("Notre vision")
st.write(s.text)
img(str(s.image_path), use_container_width=True)
