import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Les 3 piliers")
st.title("Les 3 piliers du modèle")

ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets"

img(ASSETS_DIR / "09_pilier_juridique.png")
img(ASSETS_DIR / "10_pilier_transmission.png")
img(ASSETS_DIR / "11_pilier_emotion.png")
