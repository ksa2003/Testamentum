import streamlit as st
from supabase import create_client, Client
from theme import apply_theme

st.set_page_config(page_title="Connexion — Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

def sidebar_nav():
    st.sidebar.markdown("### Navigation")
    try:
        st.sidebar.page_link("app.py", label="Accueil")
        st.sidebar.page_link("pages/Connexion.py", label="Connexion")
        st.sidebar.page_link("pages/Tableau_de_bord.py", label="Espace Mémoire")
        st.sidebar.page_link("pages/Acces_beneficiaire.py", label="Accès bénéficiaire")
    except Exception:
        pass

sidebar_nav()

def get_supabase() -> Client:
    # IMPORTANT: on lit le format [supabase] url/key
    if "supabase_client" in st.session_state:
        return st.session_state["supabase_client"]

    if "supabase" not in st.secrets:
        st.error("Secrets manquants : ajoutez [supabase].url et [supabase].key dans les Secrets Streamlit.")
        st.stop()

    url = st.secrets["supabase"].get("url")
    key = st.secrets["supabase"].get("key")
    if not url or not key:
        st.error("Secrets incomplets : [supabase].url et [supabase].key sont requis.")
        st.stop()

    client = create_client(url, key)
    st.session_state["supabase_client"] = client
    return client

def set_auth(session):
    st.session_state["auth_session"] = session
    st.session_state["user"] = session.user if session else None

supabase = get_supabase()

st.markdown(
    """
<div class="tm-card2">
  <h2 style="margin:0; font-size:34px; font-weight:800; color:rgba(255,255,255,0.93);">Connexion</h2>
  <div class="tm-p" style="margin-top:8px;">
    Connectez-vous pour accéder à votre espace personnel, ou créez un compte.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Pré-remplissage depuis la landing page
prefill = st.session_state.get("prefill_email", "")

tab_login, tab_signup = st.tabs(["Se connecter", "Créer un compte"])

with tab_login:
    email = st.text_input("Adresse e-mail", value=prefill, key="login_email")
    password = st.text_input("Mot de passe", type="password", key="login_password")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Se connecter", use_container_width=True):
        if not email or not password:
            st.error("Veuillez renseigner e-mail et mot de passe.")
        else:
            try:
                res = supabase.auth.sign_in_with_password({"email": email.strip(), "password": password})
                set_auth(res.session)
                st.success("Connexion réussie.")
                st.switch_page("pages/Tableau_de_bord.py")
            except Exception:
                st.error("Connexion impossible. Identifiants invalides ou email non confirmé.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab_signup:
    email2 = st.text_input("Adresse e-mail", value=prefill, key="signup_email")
    password2 = st.text_input("Mot de passe", type="password", key="signup_password")
    password3 = st.text_input("Confirmer le mot de passe", type="password", key="signup_password2")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Créer le compte", use_container_width=True):
        if not email2 or not password2:
            st.error("Veuillez renseigner e-mail et mot de passe.")
        elif password2 != password3:
            st.error("Les mots de passe ne correspondent pas.")
        else:
            try:
                supabase.auth.sign_up({"email": email2.strip(), "password": password2})
                st.success("Compte créé. Vérifiez votre email pour confirmer l’inscription, puis connectez-vous.")
            except Exception:
                st.error("Impossible de créer le compte (email déjà utilisé ou configuration Supabase).")
    st.markdown("</div>", unsafe_allow_html=True)

# Petite info (sans barre noire inutile)
st.markdown(
    '<div class="tm-muted">Conseil : utilisez un mot de passe unique. Si “Confirm email” est activé sur Supabase, la connexion est impossible avant confirmation.</div>',
    unsafe_allow_html=True,
)
