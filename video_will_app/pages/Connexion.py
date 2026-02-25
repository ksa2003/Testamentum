import streamlit as st

from theme import apply_theme


def _goto(page: str):
    """Navigate to another page with compatibility fallbacks."""
    # Streamlit >= 1.22
    try:
        st.switch_page(page)
        return
    except Exception:
        pass

    # Fallback: show a direct link (works in Streamlit Cloud)
    st.info("Navigation indisponible sur cette version : utilisez le menu à gauche.")


apply_theme("Kidan Vid")

st.markdown("<div class='tm-card'>", unsafe_allow_html=True)
st.markdown("<h1 class='tm-title'>Connexion</h1>", unsafe_allow_html=True)
st.markdown("<div class='tm-sub'>Accédez à votre espace sécurisé.</div>", unsafe_allow_html=True)

with st.form("login_form", clear_on_submit=False):
    email = st.text_input("Adresse email", placeholder="votre@email.com")
    password = st.text_input("Mot de passe", type="password")
    submitted = st.form_submit_button("Se connecter", type="primary")

if submitted:
    # Démo : on ne valide pas réellement (pas de backend ici).
    if not email or not password:
        st.error("Veuillez renseigner l'email et le mot de passe.")
    else:
        st.success("Connexion simulée réussie (mode démo).")
        # Exemple : diriger vers l'espace mémoire
        _goto("pages/Espace_Memoire.py")

st.markdown("<hr style='border:0;border-top:1px solid rgba(255,255,255,0.15);margin:22px 0;'/>", unsafe_allow_html=True)

st.markdown("<h2 class='tm-h2'>Accès bénéficiaire</h2>", unsafe_allow_html=True)
st.markdown(
    "<div class='tm-sub'>Si vous avez reçu un code d'accès, utilisez le menu à gauche ou cliquez ci-dessous.</div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Aller à Accès bénéficiaire", use_container_width=True):
        _goto("pages/Acces_beneficiaire.py")
with col2:
    if st.button("Créer un compte (bientôt)", use_container_width=True):
        st.info("Fonction à venir.")

st.markdown("</div>", unsafe_allow_html=True)
