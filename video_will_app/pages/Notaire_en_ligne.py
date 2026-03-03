import streamlit as st

st.set_page_config(page_title="Notaire en ligne", layout="wide")

st.title("Pourquoi utiliser un notaire en ligne ?")

st.markdown("""
### Commodité
Les signataires peuvent faire authentifier leurs documents à distance,
depuis un appareil mobile ou un ordinateur avec webcam.

### Rapidité
Une séance de notarisation en ligne prend généralement entre 5 et 15 minutes.

### Sécurité
Les documents sont scellés numériquement afin de prévenir toute fraude ou altération.

### Accessibilité internationale
Le service peut s’adapter aux cadres juridiques des différents pays,
selon la réglementation locale en vigueur.
""")

st.markdown("---")

st.caption(
    "La disponibilité de la notarisation en ligne dépend des lois en vigueur dans chaque pays."
)

if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
