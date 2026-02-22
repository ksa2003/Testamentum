import streamlit as st
from theme import apply_theme

apply_theme()

if "user_email" not in st.session_state or not st.session_state["user_email"]:
    st.warning("Veuillez vous connecter.")
    st.switch_page("pages/Connexion.py")

st.markdown(f"""
<div class="tm-card">
  <h1 style="margin:0;">Espace Mémoire</h1>
  <div class="tm-sub">Votre espace personnel de messages et de transmission</div>
  <div class="tm-latin">Connecté : {st.session_state["user_email"]}</div>
</div>
""", unsafe_allow_html=True)

st.write("")

st.subheader("Créer un message vidéo")
titre = st.text_input("Titre du message", placeholder="Ex : Pour ma famille")
video = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "webm"])

c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown('<div class="tm-btnwrap tm-primary">', unsafe_allow_html=True)
    televerser = st.button("Téléverser", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown('<div class="tm-btnwrap">', unsafe_allow_html=True)
    gerer = st.button("Gérer les bénéficiaires", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if televerser:
    if not titre.strip():
        st.error("Veuillez renseigner un titre.")
    elif video is None:
        st.error("Veuillez sélectionner une vidéo.")
    else:
        st.success("Téléversement (MVP) : vidéo reçue côté interface.")

st.write("")
st.subheader("Bénéficiaires")

if "beneficiaires" not in st.session_state:
    st.session_state["beneficiaires"] = []

with st.expander("Ajouter un bénéficiaire", expanded=True):
    nom = st.text_input("Nom complet", placeholder="Ex : Marie Dupont")
    email_b = st.text_input("Email (optionnel)", placeholder="Ex : marie@email.com")
    lien = st.text_input("Lien (optionnel)", placeholder="Ex : sœur, ami, conjoint")

    st.markdown('<div class="tm-btnwrap tm-primary">', unsafe_allow_html=True)
    add_b = st.button("Ajouter", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if add_b:
    if nom.strip():
        st.session_state["beneficiaires"].append(
            {"nom": nom.strip(), "email": email_b.strip(), "lien": lien.strip()}
        )
        st.success("Bénéficiaire ajouté.")
    else:
        st.error("Le nom complet est requis.")

if not st.session_state["beneficiaires"]:
    st.info("Aucun bénéficiaire ajouté pour l’instant.")
else:
    for b in st.session_state["beneficiaires"]:
        line = f"• {b['nom']}"
        if b["lien"]:
            line += f" — {b['lien']}"
        if b["email"]:
            line += f" ({b['email']})"
        st.write(line)

st.write("")
st.markdown('<div class="tm-btnwrap">', unsafe_allow_html=True)
if st.button("Se déconnecter", use_container_width=True):
    st.session_state.clear()
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)
