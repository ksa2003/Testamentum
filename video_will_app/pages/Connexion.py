import streamlit as st
from theme import apply_theme

apply_theme("Connexion")

st.title("Connexion")

email = st.text_input("Adresse email")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter", use_container_width=True):
    if email and password:
        st.success("Connexion simulée (backend à connecter).")
    else:
        st.error("Veuillez remplir tous les champs.")

st.divider()

if st.button("Accès bénéficiaire", use_container_width=True):
    st.switch_page("pages/Acces beneficiaire.py")
