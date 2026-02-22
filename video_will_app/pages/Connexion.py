import streamlit as st
from utils.theme import apply_theme
from utils.auth import is_valid_email, signup, signin, is_authed

st.set_page_config(page_title="Connexion — Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

st.markdown(
    """
<div class="tm-card">
  <h1 class="tm-title" style="font-size:40px;">Connexion</h1>
  <div class="tm-p" style="margin-top:8px;">
    Connectez-vous pour accéder à votre espace personnel, ou créez un compte.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

prefill = st.session_state.get("prefill_email", "")

tab1, tab2 = st.tabs(["Se connecter", "Créer un compte"])

with tab1:
    st.markdown('<div class="tm-card2">', unsafe_allow_html=True)
    with st.form("signin_form"):
        email = st.text_input("Adresse e-mail", value=prefill, placeholder="votre-email@exemple.com")
        password = st.text_input("Mot de passe", type="password", placeholder="Votre mot de passe")
        submitted = st.form_submit_button("Se connecter", type="primary", use_container_width=True)

    if submitted:
        email = (email or "").strip().lower()
        if not is_valid_email(email):
            st.error("Adresse e-mail invalide.")
        elif not password or len(password) < 8:
            st.error("Mot de passe invalide.")
        else:
            ok, msg = signin(email, password)
            if ok:
                st.success(msg)
                st.switch_page("pages/Espace_Memoire.py")
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="tm-card2">', unsafe_allow_html=True)
    with st.form("signup_form"):
        email2 = st.text_input("Adresse e-mail", value=prefill, placeholder="votre-email@exemple.com")
        pass1 = st.text_input("Mot de passe (8 caractères minimum)", type="password")
        pass2 = st.text_input("Confirmer le mot de passe", type="password")
        submitted2 = st.form_submit_button("Créer mon compte", type="primary", use_container_width=True)

    if submitted2:
        email2 = (email2 or "").strip().lower()
        if not is_valid_email(email2):
            st.error("Adresse e-mail invalide.")
        elif not pass1 or len(pass1) < 8:
            st.error("Mot de passe trop court (8 caractères minimum).")
        elif pass1 != pass2:
            st.error("Les mots de passe ne correspondent pas.")
        else:
            ok, msg = signup(email2, pass1)
            if ok:
                st.success(msg)
                st.info("Vous pouvez maintenant vous connecter.")
            else:
                st.error(msg)
    st.markdown("</div>", unsafe_allow_html=True)

if is_authed():
    st.info("Vous êtes déjà connecté.")
    if st.button("Aller à mon espace", type="primary"):
        st.switch_page("pages/Espace_Memoire.py")
