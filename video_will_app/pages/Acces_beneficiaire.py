import streamlit as st

from theme import apply_theme

apply_theme()


def sidebar_nav() -> None:
    st.sidebar.markdown("### Navigation")
    try:
        st.sidebar.page_link("app.py", label="Accueil")
        st.sidebar.page_link("pages/Connexion.py", label="Connexion")
        st.sidebar.page_link("pages/Espace_Memoire.py", label="Espace Mémoire")
        st.sidebar.page_link("pages/Acces_beneficiaire.py", label="Accès bénéficiaire")
        st.sidebar.page_link("pages/00_Dossier_Kidan_Vid.py", label="Dossier PDF")
    except Exception:
        # Compat Streamlit Cloud / versions
        pass


sidebar_nav()

st.markdown(
    """
<div class="tm-card">
  <div class="tm-h3">Accès bénéficiaire</div>
  <p class="tm-muted">Entrez un jeton d’accès temporaire. Sans jeton valide, aucun contenu n’est accessible.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

token = st.text_input("Jeton d’accès", placeholder="Ex : ABCD-1234-EFGH")

st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
if st.button("Vérifier le jeton", use_container_width=True):
    # MVP : pas de validation réelle tant que vous n'avez pas une table tokens + logique d'expiration
    if not token.strip():
        st.warning("Veuillez saisir un jeton.")
    else:
        st.error(
            "Jeton invalide (MVP). Prochaine étape : mise en place des jetons sécurisés et expirables."
        )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<div class="tm-footnote">Remarque : cette page est volontairement bloquée tant que les jetons sécurisés ne sont pas implémentés.</div>',
    unsafe_allow_html=True,
)
