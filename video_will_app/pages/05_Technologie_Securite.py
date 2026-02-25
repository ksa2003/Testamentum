import streamlit as st

from kidan_content import get_slide
from theme import apply_theme

apply_theme()

s8 = get_slide(8)

st.markdown(
    """
    <div class="tm-card">
      <div class="tm-title" style="font-size:40px;">Technologie &amp; Sécurité</div>
      <div class="tm-sub">Infrastructure chiffrée, MFA, horodatage, traçabilité</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image(s8.image_path, use_container_width=True)

st.markdown(
    f"""
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Résumé</div>
  <p>{s8.text}</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="tm-card" style="margin-top: 14px;">
  <div class="tm-h3">Si vous voulez aller plus loin (blockchain &amp; IA)</div>
  <ul>
    <li><b>Traçabilité blockchain</b> : stocker uniquement des empreintes (hash) et des horodatages, jamais les vidéos brutes.</li>
    <li><b>Horodatage certifié</b> : service d’horodatage + conservation des preuves (hash + certificat) associées aux vidéos.</li>
    <li><b>IA avancée</b> : aide à la rédaction (résumés), détection d’incohérences, mais validation finale humaine/notariale.</li>
  </ul>
  <p class="tm-muted">Je peux vous fournir un plan d’implémentation technique (étapes, tables, API) quand vous me dites l’architecture cible (Supabase / autre, stockage vidéo, etc.).</p>
</div>
""",
    unsafe_allow_html=True,
)
