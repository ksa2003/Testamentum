import streamlit as st
from theme import apply_theme


apply_theme("Kidan Vid - Connexion")

st.title("Connexion")
st.markdown("Accédez à votre espace sécurisé Kidan Vid.")

# -----------------------------
# Formulaire
# -----------------------------
with st.form("login_form", clear_on_submit=False):
    email = st.text_input("Adresse email", placeholder="votre@email.com")
    password = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("Se connecter")

if submitted:
    if not email:
        st.error("Veuillez saisir votre adresse email.")
    elif not password:
        st.error("Veuillez saisir votre mot de passe.")
    else:
        st.success("Connexion réussie.")
        st.session_state["user_email"] = email

st.markdown("---")

# -----------------------------
# Accès bénéficiaire (sans page_link)
# -----------------------------
st.subheader("Accès bénéficiaire")

st.info(
    "Si vous avez reçu un code d'accès (jeton) pour consulter un message, "
    "utilisez le menu à gauche et ouvrez la page : « Acces beneficiaire »."
)

# Optionnel : bouton qui explique quoi faire (aucun crash)
if st.button("Aller à Accès bénéficiaire (via menu à gauche)"):
    st.toast("Ouvre le menu à gauche → clique « Acces beneficiaire ».", icon=None)
