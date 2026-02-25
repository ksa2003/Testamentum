import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide


def main():
    apply_theme("Kidan Vid")

    # -----------------------------
    # SLIDE DE PRÉSENTATION (HAUT)
    # -----------------------------
    st.markdown("## Présentation")

    # Slider pour parcourir les 15 slides
    slide_id = st.slider(
        "Parcourir les slides",
        min_value=1,
        max_value=15,
        value=1,
        step=1,
    )

    s = get_slide(slide_id)
    if s and getattr(s, "image_path", None):
        img(s.image_path, use_container_width=True)
    else:
        st.warning(f"Slide {slide_id} introuvable (image_path manquant).")

    st.divider()

    # -----------------------------
    # CONTENU HOME (COMME AVANT)
    # -----------------------------
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
