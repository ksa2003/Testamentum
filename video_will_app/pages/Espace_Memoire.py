import streamlit as st
from utils.theme import apply_theme
from utils.auth import require_auth, signout

st.set_page_config(page_title="Espace Mémoire — Testamentum", page_icon="⚖️", layout="centered")
apply_theme()
require_auth()

user_email = st.session_state.get("auth_email", "")

st.markdown(
    f"""
<div class="tm-card">
  <h1 class="tm-title" style="font-size:40px;">Espace Mémoire</h1>
  <div class="tm-sub">Votre espace personnel de messages et de transmission</div>
  <div class="tm-latin" style="margin-top:8px;">Connecté : {user_email}</div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

st.markdown('<div class="tm-card2">', unsafe_allow_html=True)
st.markdown('<div class="tm-h2" style="margin-top:0;">Téléverser une vidéo</div>', unsafe_allow_html=True)
title = st.text_input("Titre du message", placeholder="Ex : Pour ma famille")
video = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "webm", "mpeg4"])

col1, col2 = st.columns(2, gap="large")
with col1:
    if st.button("Téléverser", type="primary", use_container_width=True):
        if not title.strip():
            st.error("Veuillez saisir un titre.")
        elif video is None:
            st.error("Veuillez choisir une vidéo.")
        else:
            # MVP: pas de stockage encore, juste validation UI
            st.success("Vidéo reçue (MVP). Stockage à connecter ensuite.")
with col2:
    if st.button("Gérer les bénéficiaires", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

st.markdown('<div class="tm-card2">', unsafe_allow_html=True)
st.markdown('<div class="tm-h2" style="margin-top:0;">Vos vidéos</div>', unsafe_allow_html=True)
st.caption("Aucune vidéo pour l’instant (MVP).")
st.markdown("</div>", unsafe_allow_html=True)

st.write("")

if st.button("Se déconnecter"):
    signout()
    st.switch_page("pages/Connexion.py")
