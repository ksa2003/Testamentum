import streamlit as st

from image_loader import show_asset_image


st.set_page_config(page_title="Notaire en ligne", layout="centered")


# Logo (assets/logo_kidan_vid.png)
show_asset_image("logo_kidan_vid.png", use_container_width=True)

st.title("Notaire en ligne")
st.write("Contenu à compléter : informations, partenaires, prise de rendez-vous, etc.")
