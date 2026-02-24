import streamlit as st
from theme import apply_theme
from supabase import create_client, Client
import os
import re

apply_theme()

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def signup(email: str, password: str):
    return supabase.auth.sign_up({"email": email, "password": password})


def login(email: str, password: str):
    return supabase.auth.sign_in_with_password({"email": email, "password": password})


def main():
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Kidan Vid</div>
          <div class="tm-sub">Connexion sécurisée</div>
          <div class="tm-latin">Accédez à votre espace et gérez vos messages.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    tab1, tab2 = st.tabs(["Se connecter", "Créer un compte"])

    with tab1:
        with st.form("login_form"):
            email = st.text_input("Adresse e-mail", value=st.session_state.get("email", ""))
            password = st.text_input("Mot de passe", type="password")
            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
                submit = st.form_submit_button("Connexion")
                st.markdown("</div>", unsafe_allow_html=True)
            with c2:
                back = st.form_submit_button("Retour")

        if submit:
            if not is_valid_email(email):
                st.error("Adresse e-mail invalide.")
            elif not password:
                st.error("Veuillez saisir votre mot de passe.")
            else:
                try:
                    res = login(email, password)
                    st.session_state["user"] = res.user
                    st.switch_page("pages/Espace_Memoire.py")
                except Exception:
                    st.error("Connexion impossible. Vérifiez vos identifiants.")

        if back:
            st.switch_page("app.py")

    with tab2:
        with st.form("signup_form"):
            email = st.text_input("Adresse e-mail", key="signup_email")
            password = st.text_input("Mot de passe", type="password", key="signup_password")
            st.markdown(
                '<div class="tm-muted" style="margin-top:-6px;">'
                "Conseil : utilisez un mot de passe long et unique."
                "</div>",
                unsafe_allow_html=True,
            )
            c1, c2 = st.columns(2, gap="large")
            with c1:
                st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
                submit = st.form_submit_button("Créer mon compte")
                st.markdown("</div>", unsafe_allow_html=True)
            with c2:
                back = st.form_submit_button("Retour")

        if submit:
            if not is_valid_email(email):
                st.error("Adresse e-mail invalide.")
            elif len(password) < 8:
                st.error("Mot de passe trop court (8 caractères minimum).")
            else:
                try:
                    signup(email, password)
                    st.success("Compte créé. Vous pouvez vous connecter.")
                except Exception:
                    st.error("Création du compte impossible. Essayez avec une autre adresse e-mail.")

        if back:
            st.switch_page("app.py")


if __name__ == "__main__":
    main()
