import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


def main():
    apply_theme("Kidan Vid")

    # Slide de présentation (cover)
    s0 = get_slide(1)
    if s0:
        img(s0.image_path)

    st.markdown("# Un message vidéo, transmis au bon moment.")
    st.write(
        "Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré."
    )

    st.markdown(
        """
- Accès bénéficiaires par jeton temporaire sécurisé  
- Validation notariale  
- Journalisation et traçabilité  
"""
    )

    st.markdown("## Commencer")
    email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Continuer", use_container_width=True):
            st.session_state["email"] = email
            st.switch_page("pages/Connexion.py")

    with col2:
        if st.button("Accès bénéficiaire", use_container_width=True):
            st.switch_page("pages/Acces beneficiaire.py")


if __name__ == "__main__":
    main()
