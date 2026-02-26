import streamlit as st
from pathlib import Path
from theme import apply_theme, img

apply_theme("Les 3 piliers")

st.title("Les 3 piliers du modèle")

img(Path("assets/09_pilier_juridique.png"))
img(Path("assets/10_pilier_transmission.png"))
img(Path("assets/11_pilier_emotion.png"))
