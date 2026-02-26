import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Alliance")

st.title("L’alliance")

# Slide 14 = alliance_institutionnelle (selon ta liste)
s = get_slide(14)

if s:
    img(s.image_path)
else:
    st.warning("Slide introuvable (14). Vérifie le dossier video_will_app/assets et le nom du fichier.")
