import streamlit as st
from theme import apply_theme

st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

def sidebar_nav():
    st.sidebar.markdown("### Navigation")
    try:
        st.sidebar.page_link("app.py", label="Accueil")
        st.sidebar.page_link("pages/Connexion.py", label="Connexion")
        st.sidebar.page_link("pages/Tableau_de_bord.py", label="Espace Mémoire")
        st.sidebar.page_link("pages/Acces_beneficiaire.py", label="Accès bénéficiaire")
    except Exception:
        st.sidebar.markdown("- Accueil")
        st.sidebar.markdown("- Connexion")
        st.sidebar.markdown("- Espace Mémoire")
        st.sidebar.markdown("- Accès bénéficiaire")

sidebar_nav()

st.markdown(
    """
<div class="tm-card">
  <h1 class="tm-title">Testamentum</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>

  <div class="tm-chiprow">
    <span class="tm-chip">Mémoire</span>
    <span class="tm-chip">Transmission</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
  </div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <div class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
    Le service est conçu pour une transmission respectueuse et structurée.
  </div>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale<br/>
    • Journalisation des actions
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

st.markdown(
    """
<div class="tm-card2">
  <div class="tm-h2" style="margin-top:0;">Commencer</div>
  <div class="tm-p" style="margin-top:6px;">
    Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
  </div>
</div>
""",
    unsafe_allow_html=True,
)

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Continuer", use_container_width=True):
        if not email:
            st.error("Veuillez saisir une adresse e-mail.")
        else:
            st.session_state["prefill_email"] = email.strip()
            st.switch_page("pages/Connexion.py")
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    # Accès bénéficiaire : page dédiée (mais elle vérifiera la présence d'un token)
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")

st.markdown(
    '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True,
)
