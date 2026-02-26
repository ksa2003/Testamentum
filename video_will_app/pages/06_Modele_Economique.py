import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Modèle économique")
st.title("Modèle économique")

ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets"
img(ASSETS_DIR / "07_modele_economique.png")
