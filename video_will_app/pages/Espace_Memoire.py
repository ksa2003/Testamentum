import streamlit as st
from theme import apply_theme

apply_theme()

if "user_email" not in st.session_state:
    st.warning("Veuillez vous connecter.")
    st.switch_page("pages/Connexion.py")

st.markdown(f"""
<div class="tm-card">
<h1>Espace Mémoire</h1>
<div class="tm-sub">Connecté : {st.session_state["user_email"]}</div>
</div>
""", unsafe_allow_html=True)

st.write("")

st.subheader("Créer un message vidéo")

titre = st.text_input("Titre du message")

video = st.file_uploader("Sélectionner une vidéo", type=["mp4","mov","webm"])

c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    st.button("Téléverser", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.button("Gérer les bénéficiaires", use_container_width=True)

st.write("")

st.subheader("Bénéficiaires")

if "beneficiaires" not in st.session_state:
    st.session_state["beneficiaires"] = []

nom = st.text_input("Nom complet")
email_b = st.text_input("Email (optionnel)")
lien = st.text_input("Lien (optionnel)")

if st.button("Ajouter", use_container_width=True):
    st.session_state["beneficiaires"].append(
        {"nom": nom, "email": email_b, "lien": lien}
    )

if not st.session_state["beneficiaires"]:
    st.info("Aucun bénéficiaire ajouté.")
else:
    for b in st.session_state["beneficiaires"]:
        st.write(f"• {b['nom']} ({b['email']})")

st.write("")

if st.button("Se déconnecter", use_container_width=True):
    st.session_state.clear()
    st.switch_page("app.py")
