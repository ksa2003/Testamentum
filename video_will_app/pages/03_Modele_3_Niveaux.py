import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Modèle 3 niveaux")

s = get_slide(8)

st.title("Modèle : système en 3 niveaux")

if s:
    img(s.image_path)
else:
    st.warning("Slide introuvable.")
