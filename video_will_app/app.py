import streamlit as st
from theme import apply_theme
from pathlib import Path
import base64

st.set_page_config(page_title="Kidan Vid", page_icon="🎥", layout="centered")
apply_theme()


def show_page1():
    img_path = Path("video_will_app/assets/kidan_page_01.png")
    if img_path.exists():
        img_base64 = base64.b64encode(img_path.read_bytes()).decode()
        st.markdown(
            f'<img src="data:image/png;base64,{img_base64}" class="tm-image" width="100%">',
            unsafe_allow_html=True
        )


def main():
    st.markdown(
        """
        <div class="tm-card">
            <div class="tm-title">Kidan Vid</div>
            <div class="tm-sub">
                Transmettez vos mots. Préservez vos volontés. Sécurisez votre héritage.
            </div>
            <div style="margin-top:15px;">
                <span class="tm-chip">Mémoire</span>
                <span class="tm-chip">Transmission</span>
                <span class="tm-chip">Confidentialité</span>
                <span class="tm-chip">Traçabilité</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    show_page1()
    st.write("")

    with st.form("start"):
        email = st.text_input("Adresse e-mail", placeholder="votre@email.com")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
            continue_btn = st.form_submit_button("Continuer")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            access_btn = st.form_submit_button("Accès bénéficiaire")

    st.markdown(
        '<div style="color:rgba(255,255,255,0.85);font-size:13px;margin-top:10px;">'
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
        "</div>",
        unsafe_allow_html=True,
    )

    if continue_btn:
        st.session_state["email"] = email
        st.switch_page("pages/Connexion.py")

    if access_btn:
        st.switch_page("pages/Acces_beneficiaire.py")


if __name__ == "__main__":
    main()
