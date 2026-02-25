import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Page 1")

s = get_slide(1)
st.title("Page 1")
st.caption("Référence visuelle (couverture du dossier)")
img(str(s.image_path), use_container_width=True)
