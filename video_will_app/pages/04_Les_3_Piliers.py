import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Les 3 piliers du modèle")

st.title("Les 3 piliers du modèle")

image_path = Path("assets/slides/les_3_piliers.png")

img(image_path)
