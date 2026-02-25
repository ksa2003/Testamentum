import streamlit as st
from theme import apply_theme

apply_theme()

st.markdown("""
<div class="tm-card">
  <h1 style="margin:0;">Connexion</h1>
  <div class="tm-sub">Accédez à votre espace sécurisé</div>
</div>
""", unsafe_allow_html=True)

st.write("")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")
password = st.text_input("Mot de passe", type="password", placeholder="••••••••")

st.markdown('<div class="tm-btnwrap tm-primary">', unsafe_allow_html=True)
login = st.button("Se connecter", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

if login:
    if not email.strip():
        st.error("Veuillez saisir un e-mail.")
    else:
        # MVP: pas d'auth réelle
        st.session_state["user_email"] = email.strip()
        st.success("Connecté.")
        st.switch_page("pages/Espace_Memoire.py")
