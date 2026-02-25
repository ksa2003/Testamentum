import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


def main():
    apply_theme("Kidan Vid")

    # PHOTO DE PRÉSENTATION FIXE (slide 1)
    s0 = get_slide(1)
    if s0 and getattr(s0, "image_path", None):
        img(s0.image_path, caption=None, use_container_width=True)

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

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Continuer", use_container_width=True):
            st.session_state["email"] = email
            st.switch_page("pages/Connexion.py")

    with c2:
        if st.button("Accès bénéficiaire", use_container_width=True):
            st.switch_page("pages/Acces beneficiaire.py")


if __name__ == "__main__":
    main()
