import streamlit as st
from theme import apply_theme

apply_theme()

# -----------------------------------------------------------------------------
# Connexion / Création de compte (Supabase)
# - Ne jamais afficher de détails techniques côté utilisateur
# - Afficher des messages neutres, et stopper si secrets manquants
# - Vraie vérification: on utilise Supabase Auth (sign_in / sign_up)
# -----------------------------------------------------------------------------

def _get_supabase_client():
    """
    Retourne un client Supabase si la config existe, sinon None.
    On ne leak jamais l'infra côté UI.
    """
    try:
        from supabase import create_client
    except Exception:
        return None

    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
        if not url or not key:
            return None
        return create_client(url, key)
    except Exception:
        return None


def _set_logged_in(email: str):
    st.session_state["user_email"] = email


def _redirect_to_memory():
    # Streamlit multipage: chemin page
    try:
        st.switch_page("pages/Espace_Memoire.py")
    except Exception:
        # fallback si switch_page pas dispo / chemin différent
        st.page_link("pages/Espace_Memoire.py", label="Aller à Espace Mémoire")


# -----------------------------------------------------------------------------
# UI Header
# -----------------------------------------------------------------------------
st.markdown(
    """
<div class="tm-card">
  <h1 style="margin:0; font-size:44px; font-weight:780;">Connexion</h1>
  <div class="tm-sub">Connectez-vous pour accéder à votre espace personnel, ou créez un compte.</div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------------------------------------------------------
# Supabase config check (sans fuite)
# -----------------------------------------------------------------------------
supabase = _get_supabase_client()
if supabase is None:
    st.error("Le service d’authentification n’est pas disponible pour le moment.")
    st.info("Réessayez dans quelques instants.")
    st.stop()

# -----------------------------------------------------------------------------
# Tabs (Connexion / Créer un compte)
# -----------------------------------------------------------------------------
tab_login, tab_signup = st.tabs(["Se connecter", "Créer un compte"])

with tab_login:
    st.markdown("<div class='tm-card'>", unsafe_allow_html=True)
    email = st.text_input("Adresse e-mail", placeholder="ex : nom@domaine.com", key="login_email")
    password = st.text_input("Mot de passe", type="password", placeholder="Votre mot de passe", key="login_pwd")

    st.write("")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    do_login = st.button("Se connecter", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if do_login:
        if not email.strip() or not password:
            st.error("Veuillez renseigner une adresse e-mail et un mot de passe.")
        else:
            try:
                res = supabase.auth.sign_in_with_password({"email": email.strip(), "password": password})
                # res.user peut être None si échec
                if getattr(res, "user", None) is None:
                    st.error("Identifiants incorrects.")
                else:
                    _set_logged_in(res.user.email or email.strip())
                    st.success("Connexion réussie.")
                    _redirect_to_memory()
            except Exception:
                # On ne leak pas l'erreur
                st.error("Connexion impossible. Vérifiez vos identifiants et réessayez.")


with tab_signup:
    st.markdown("<div class='tm-card'>", unsafe_allow_html=True)
    email2 = st.text_input("Adresse e-mail", placeholder="ex : nom@domaine.com", key="signup_email")
    password2 = st.text_input("Mot de passe", type="password", placeholder="Choisissez un mot de passe", key="signup_pwd")
    password3 = st.text_input("Confirmer le mot de passe", type="password", placeholder="Confirmez", key="signup_pwd2")

    st.caption("Un e-mail de confirmation peut être requis selon la configuration du projet.")

    st.write("")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    do_signup = st.button("Créer mon compte", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if do_signup:
        if not email2.strip() or not password2 or not password3:
            st.error("Veuillez remplir tous les champs.")
        elif password2 != password3:
            st.error("Les mots de passe ne correspondent pas.")
        elif len(password2) < 8:
            st.error("Le mot de passe doit contenir au moins 8 caractères.")
        else:
            try:
                # IMPORTANT: si "Confirm email" est activé sur Supabase,
                # l’utilisateur devra confirmer avant de pouvoir se connecter.
                res = supabase.auth.sign_up({"email": email2.strip(), "password": password2})

                # Certaines configs renvoient user None tant que non confirmé.
                if getattr(res, "user", None) is None:
                    st.success("Compte créé. Vérifiez votre e-mail pour confirmer votre inscription.")
                else:
                    st.success("Compte créé. Vous pouvez maintenant accéder à votre espace.")
                    _set_logged_in(res.user.email or email2.strip())
                    _redirect_to_memory()

            except Exception:
                st.error("Impossible de créer le compte. Cette adresse est peut-être déjà utilisée.")


# -----------------------------------------------------------------------------
# Note: on ne met aucun texte “Supabase / secrets” visible utilisateur ici.
# -----------------------------------------------------------------------------
