import streamlit as st
from theme import apply_theme

apply_theme("Connexion")

st.title("Connexion")
st.write("Accédez à votre espace sécurisé.")

# Initialisation session
if "auth" not in st.session_state:
    st.session_state["auth"] = False
if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""

email = st.text_input("Adresse email", value=st.session_state["user_email"])
password = st.text_input("Mot de passe", type="password")

# IMPORTANT : ici c’est une connexion “simulée”.
# Pour une vraie connexion, on branchera Supabase (ou autre).
if st.button("Se connecter", use_container_width=True):
    if email and password:
        st.session_state["auth"] = True
        st.session_state["user_email"] = email
        st.success("Connexion réussie.")
        st.switch_page("pages/Espace_Memoire.py")
    else:
        st.error("Veuillez remplir l’email et le mot de passe.")

st.divider()

col1, col2 = st.columns(2)
with col1:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces beneficiaire.py")

with col2:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
