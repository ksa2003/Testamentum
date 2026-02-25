import streamlit as st
from theme import apply_theme


# IMPORTANT : toujours en premier
st.set_page_config(
    page_title="Kidan Vid",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    apply_theme("Kidan Vid")

    st.markdown(
        """
        ## Un message vidéo, transmis au bon moment.

        Enregistrez un message destiné à vos proches, puis contrôlez précisément
        l’accès des bénéficiaires lorsque le décès est déclaré.

        - Accès bénéficiaires par jeton temporaire sécurisé  
        - Validation notariale  
        - Journalisation et traçabilité
        """
    )

    st.markdown("### Commencer")

    email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Continuer", use_container_width=True):
            st.session_state["pending_email"] = email
            st.switch_page("pages/Connexion.py")

    with col2:
        if st.button("Accès bénéficiaire", use_container_width=True):
            st.switch_page("pages/Acces_beneficiaire.py")


if __name__ == "__main__":
    main()
