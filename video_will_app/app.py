import streamlit as st

from kidan_content import get_slide
from theme import apply_theme


apply_theme()

s1 = get_slide(1)

st.markdown(
    f"""
    <div class="tm-card">
      <div class="tm-title">Kidan Vid</div>
      <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
      <div class="tm-latin">Verba manent. Memoria custoditur.</div>

      <div class="tm-chips">
        <span class="tm-chip">Mémoire</span>
        <span class="tm-chip">Transmission</span>
        <span class="tm-chip">Confidentialité</span>
        <span class="tm-chip">Traçabilité</span>
      </div>

      <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>
      <p>
        Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
        lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
      </p>
      <ul>
        <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
        <li>Validation notariale (selon le niveau choisi)</li>
        <li>Journalisation des actions et traçabilité</li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Visuel couverture (slide 1)
st.image(s1.image_path, use_container_width=True)

st.markdown(
    """
    <div class="tm-card" style="margin-top: 18px;">
      <div class="tm-h3">Commencer</div>
      <p class="tm-muted">Saisissez votre adresse e-mail pour créer un compte ou vous connecter.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

# Deux boutons STRICTEMENT alignés (même row, même hauteur)
col_a, col_b = st.columns(2, gap="small")

with col_a:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    go = st.button("Continuer", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_b:
    go_benef = st.button("Accès bénéficiaire", use_container_width=True)

st.markdown(
    '<div class="tm-footnote">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.</div>',
    unsafe_allow_html=True,
)

if go:
    st.session_state["start_email"] = email
    st.switch_page("pages/Connexion.py")

if go_benef:
    st.switch_page("pages/Acces_beneficiaire.py")
