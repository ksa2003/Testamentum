import streamlit as st

from theme import apply_theme, img
from kidan_content import get_slide


def main() -> None:
    apply_theme("Kidan Vid")

    s1 = get_slide(1)

    # Hero / Cover
    img(str(s1.image_path), caption=None, use_container_width=True)

    st.markdown(
        """
        ## Un message vidéo, transmis au bon moment.
        Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
        lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.

        - Accès bénéficiaires par jeton temporaire sécurisé
        - Validation notariale (selon le niveau choisi)
        - Journalisation des actions et traçabilité
        """
    )

    st.markdown("### Commencer")
    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    # Buttons on same line, same width
    col1, col2 = st.columns(2, gap="large")
    with col1:
        if st.button("Continuer", use_container_width=True, type="primary"):
            st.session_state["pending_email"] = email
            st.switch_page("pages/Connexion.py")
    with col2:
        if st.button("Accès bénéficiaire", use_container_width=True):
            st.switch_page("pages/Acces_beneficiaire.py")

    st.caption(
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
    )


if __name__ == "__main__":
    main()
