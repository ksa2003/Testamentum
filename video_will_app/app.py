import streamlit as st
from pathlib import Path

from theme import apply_theme, img
from kidan_content import get_slide, ASSETS_DIR

apply_theme()

s1 = get_slide(1)

st.markdown(
    f"""
<div class="tm-card">
  <h1 class="tm-title">Kidan Vid</h1>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-latin">Verba manent. Memoria custoditur.</div>

  <div style="margin-top:15px;">
    <span class="tm-chip">Mémoire</span>
    <span class="tm-chip">Transmission</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
  </div>

  <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

  <p style="color:rgba(255,255,255,0.88); font-size:15px;">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
    lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
  </p>

  <ul style="color:rgba(255,255,255,0.86); font-size:15px;">
    <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
    <li>Validation notariale</li>
    <li>Journalisation des actions et traçabilité</li>
  </ul>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# Image Page 1
p = Path(s1.image_path)
if p.exists():
    img(str(p))
else:
    st.warning(
        f"Image {p.name} introuvable.\n\n"
        f"Tu dois mettre tes images dans: {ASSETS_DIR}\n"
        f"(dossier video_will_app/assets/ dans ton dépôt GitHub)."
    )

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
