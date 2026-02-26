import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Marché & opportunité")

st.title("Marché & opportunité")

image_path = Path("assets/05_marche_opportunite.png")

img(image_path)
