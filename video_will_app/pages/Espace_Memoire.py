import streamlit as st
from theme import apply_theme

apply_theme("Espace Mémoire")

# Garde-fou : si pas connecté -> Connexion
if not st.session_state.get("auth", False):
    st.warning("Vous devez être connecté pour accéder à l’Espace Mémoire.")
    st.switch_page("pages/Connexion.py")

st.title("Espace Mémoire")

st.write(f"Connecté en tant que : {st.session_state.get('user_email','')}")

st.info("Zone privée (à connecter ensuite à Supabase : vidéos, documents, coffre-fort, etc.).")

if st.button("Se déconnecter", use_container_width=True):
    st.session_state["auth"] = False
    st.switch_page("pages/Connexion.py")
