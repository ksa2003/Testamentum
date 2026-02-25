import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide
from pathlib import Path

apply_theme()

s1 = get_slide(1)

st.markdown("""
<div class="tm-card">
  <div class="tm-title">Kidan Vid</div>
  <div class="tm-sub">
    Coffre numérique sécurisé pour transmission vidéo posthume
  </div>

  <div style="margin-top:15px;">
    <span class="tm-chip">Mémoire</span>
    <span class="tm-chip">Transmission</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
  </div>

  <div class="tm-h2">
    Un message vidéo, transmis au bon moment.
  </div>

  <p>
    Enregistrez un message destiné à vos proches, puis contrôlez précisément
    l’accès des bénéficiaires lorsque le décès est déclaré.
  </p>

  <ul>
    <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
    <li>Validation notariale</li>
    <li>Journalisation des actions et traçabilité</li>
  </ul>
</div>
""", unsafe_allow_html=True)


# ✅ Affichage image sécurisé
if Path(s1.image_path).exists():
    img(s1.image_path)
else:
    st.warning("Image kidan_page_01.png introuvable dans assets/")


st.write("")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

col1, col2 = st.columns(2, gap="large")

with col1:
    go = st.button("Continuer", use_container_width=True, type="primary")

with col2:
    go_benef = st.button("Accès bénéficiaire", use_container_width=True)

if go:
    st.switch_page("pages/Connexion.py")

if go_benef:
    st.switch_page("pages/Acces_beneficiaire.py")
