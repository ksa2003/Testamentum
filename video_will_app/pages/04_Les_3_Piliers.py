import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


apply_theme("Kidan Vid — Les 3 piliers")

st.title("Les 3 piliers du modèle")

s_j = get_slide(9)
st.subheader(s_j.title)
st.write(s_j.text)
img(str(s_j.image_path), use_container_width=True)

st.divider()

s_t = get_slide(10)
st.subheader(s_t.title)
st.write(s_t.text)
img(str(s_t.image_path), use_container_width=True)

st.divider()

s_e = get_slide(11)
st.subheader(s_e.title)
st.write(s_e.text)
img(str(s_e.image_path), use_container_width=True)
