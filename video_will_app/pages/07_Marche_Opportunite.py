import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Marché & opportunité")
st.title("Marché & opportunité")

ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets"
img(ASSETS_DIR / "05_marche_opportunite.png")
