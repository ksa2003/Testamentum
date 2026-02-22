import streamlit as st
from theme import apply_theme

st.set_page_config(page_title="Accès bénéficiaire — Testamentum", page_icon="⚖️", layout="centered")
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

st.markdown(
    """
<div class="tm-card2">
  <h2 style="margin:0; font-size:34px; font-weight:800; color:rgba(255,255,255,0.93);">Accès bénéficiaire</h2>
  <div class="tm-p" style="margin-top:8px;">
    Entrez un jeton d’accès temporaire. Sans jeton valide, aucun contenu n’est accessible.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

token = st.text_input("Jeton d’accès", placeholder="Ex : ABCD-1234-EFGH")

st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
if st.button("Vérifier le jeton", use_container_width=True):
    # MVP : pas de validation réelle tant que vous n'avez pas une table tokens + logique d'expiration
    st.error("Jeton invalide (MVP). Prochaine étape : mise en place des jetons sécurisés et expirables.")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    '<div class="tm-muted">Remarque : cette page est volontairement bloquée tant que les jetons sécurisés ne sont pas implémentés.</div>',
    unsafe_allow_html=True,
)
