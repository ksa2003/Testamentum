import streamlit as st

st.set_page_config(page_title="Notaire en ligne – New York", layout="wide")

st.title("Pourquoi utiliser un notaire en ligne ?")

st.subheader("Commodité")
st.write("Les signataires de New York peuvent obtenir leurs documents notariés à distance en ligne avec un appareil mobile ou une webcam.")

st.subheader("Vitesse")
st.write("La séance moyenne de notaire en ligne ne prend pas plus de 5 à 10 minutes.")

st.subheader("Sécurité")
st.write("Les documents sont scellés numériquement pour se protéger contre la fraude et l'altération.")

st.subheader("Facilité d'utilisation")
st.write("Cliquez sur un lien pour rejoindre la session de notaire avec votre téléphone ou votre navigateur d'ordinateur.")

st.markdown("---")
st.caption("Ce contenu est un exemple de marché et de fonctionnement. La conformité exacte doit être validée juridiquement par pays.")

if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
