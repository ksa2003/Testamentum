import streamlit as st

from theme import apply_theme, img
from kidan_content import all_slides


apply_theme("Kidan Vid — Dossier complet")

st.title("Dossier Kidan Vid")
st.caption("Toutes les pages du dossier (images + résumé).")

for s in all_slides():
    with st.expander(f"{s.page:02d} — {s.title}", expanded=(s.page == 1)):
        st.write(s.text)
        img(str(s.image_path), use_container_width=True)
