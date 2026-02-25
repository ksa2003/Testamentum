import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Modèle : système en 3 niveaux")

s = get_slide(8)
st.title("Modèle : système en 3 niveaux")
st.write(s.text)
img(str(s.image_path), use_container_width=True)
