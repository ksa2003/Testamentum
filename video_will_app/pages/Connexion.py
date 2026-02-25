import streamlit as st
from theme import apply_theme


# -------------------------------------------------------
# PAGE CONNEXION
# -------------------------------------------------------

apply_theme("Kidan Vid - Connexion")


st.title("Connexion")

st.markdown("Accédez à votre espace sécurisé Kidan Vid.")


# -------------------------------------------------------
# Formulaire sécurisé (évite rerun instable)
# -------------------------------------------------------

with st.form("login_form", clear_on_submit=False):

    email = st.text_input(
        "Adresse email",
        placeholder="votre@email.com"
    )

    password = st.text_input(
        "Mot de passe",
        type="password"
    )

    submitted = st.form_submit_button("Se connecter")


# -------------------------------------------------------
# Logique après soumission
# -------------------------------------------------------

if submitted:

    if not email:
        st.error("Veuillez saisir votre adresse email.")
    elif not password:
        st.error("Veuillez saisir votre mot de passe.")
    else:
        # Ici tu pourras brancher Supabase / base utilisateurs plus tard
        st.success("Connexion réussie.")
        st.session_state["user_email"] = email


# -------------------------------------------------------
# Lien vers accès bénéficiaire
# -------------------------------------------------------

st.markdown("---")
st.page_link("pages/Acces beneficiaire.py", label="Accès bénéficiaire")
