# video_will_app/pages/Connexion.py
from __future__ import annotations

import streamlit as st
from theme import apply_theme


# Toujours config AVANT st.* si ce fichier peut être exécuté seul
st.set_page_config(
    page_title="Connexion - Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)


apply_theme("Connexion", "Accédez à votre espace sécurisé")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Connexion")
    email = st.text_input("Adresse email", placeholder="votre@email.com")
    password = st.text_input("Mot de passe", type="password", placeholder="********")

    # Ici tu mets ta logique réelle d'auth (Supabase etc.)
    # Pour éviter de planter, on garde un bouton neutre.
    if st.button("Se connecter", use_container_width=True):
        # Exemple : tu peux rediriger vers une page après auth validée
        st.success("Connexion envoyée (à relier à ton backend).")

with col2:
    st.subheader("Accès bénéficiaire")
    st.info(
        "Si vous avez reçu un code d’accès, vous pouvez ouvrir la page Accès bénéficiaire."
    )

    # IMPORTANT : page_link plante souvent si le chemin/nom n'est pas reconnu.
    # switch_page est plus fiable.
    if st.button("Aller à Accès bénéficiaire", use_container_width=True):
        # Le fichier doit exister exactement sous /pages avec ce nom.
        st.switch_page("pages/Acces beneficiaire.py")


st.divider()
st.caption("Kidan Vid - Transmission sécurisée et traçable.")
