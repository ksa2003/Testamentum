import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Modèle économique")

st.title("Modèle économique")

# Chemin vers l'image
image_path = Path("assets/slides/modele_economique.png")

img(image_path)
