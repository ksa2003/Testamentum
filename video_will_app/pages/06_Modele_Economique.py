import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Modèle économique")

st.title("Modèle économique")

image_path = Path("assets/07_modele_economique.png")

img(image_path)
