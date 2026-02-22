from __future__ import annotations
import re
import streamlit as st
from supabase import create_client

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def get_supabase():
    url = st.secrets.get("SUPABASE_URL")
    key = st.secrets.get("SUPABASE_KEY")
    if not url or not key:
        st.error("Configuration Supabase manquante. Ajoute SUPABASE_URL et SUPABASE_KEY dans secrets.toml.")
        st.stop()
    return create_client(url, key)

def is_valid_email(email: str) -> bool:
    return bool(email and EMAIL_RE.match(email.strip()))

def set_session(user_email: str) -> None:
    st.session_state["auth_email"] = user_email

def clear_session() -> None:
    st.session_state.pop("auth_email", None)

def is_authed() -> bool:
    return bool(st.session_state.get("auth_email"))

def require_auth() -> None:
    if not is_authed():
        st.warning("Veuillez vous connecter pour accéder à cette page.")
        st.switch_page("pages/Connexion.py")

def signup(email: str, password: str) -> tuple[bool, str]:
    supabase = get_supabase()
    try:
        resp = supabase.auth.sign_up({"email": email, "password": password})
        # Selon la config Supabase, un email de confirmation peut être requis.
        if getattr(resp, "user", None) is None:
            return True, "Compte créé. Vérifiez votre e-mail pour confirmer (si activé)."
        return True, "Compte créé."
    except Exception as e:
        return False, f"Impossible de créer le compte : {e}"

def signin(email: str, password: str) -> tuple[bool, str]:
    supabase = get_supabase()
    try:
        resp = supabase.auth.sign_in_with_password({"email": email, "password": password})
        user = getattr(resp, "user", None)
        if user is None:
            return False, "Identifiants invalides."
        set_session(email)
        return True, "Connexion réussie."
    except Exception:
        return False, "Identifiants invalides ou compte inexistant."

def signout() -> None:
    # On efface la session Streamlit (MVP). Plus tard tu peux aussi appeler supabase.auth.sign_out()
    clear_session()
