import streamlit as st
from theme import apply_theme

# set_page_config doit être appelé une seule fois, avant tout affichage
st.set_page_config(page_title="Testamentum", layout="wide")

apply_theme()


def home_page() -> None:
    # Bloc haut (présentation)
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Testamentum</div>
          <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
          <div class="tm-latin">Verba manent. Memoria custoditur.</div>

          <div class="tm-chiprow">
            <span class="tm-chip">Mémoire</span>
            <span class="tm-chip">Transmission</span>
            <span class="tm-chip">Confidentialité</span>
            <span class="tm-chip">Traçabilité</span>
          </div>

          <div class="tm-h2">Un message vidéo, transmis au bon moment.</div>

          <div class="tm-text">
            Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
            lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
          </div>

          <ul class="tm-list">
            <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
            <li>Validation notariale</li>
            <li>Journalisation des actions</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    # Bloc "Commencer"
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-h1">Commencer</div>
          <div class="tm-text">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # 2 boutons parfaitement alignés (même largeur/hauteur)
    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown('<div class="tm-btnwrap tm-primary">', unsafe_allow_html=True)
        go_continue = st.button("Continuer", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="tm-btnwrap">', unsafe_allow_html=True)
        go_benef = st.button("Accès bénéficiaire", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="tm-footnote">
          En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Navigation
    if go_continue:
        try:
            st.switch_page("pages/Connexion.py")
        except Exception:
            st.info("Ouvrez la page Connexion dans le menu à gauche.")

    if go_benef:
        try:
            st.switch_page("pages/Acces_beneficiaire.py")
        except Exception:
            st.info("Ouvrez la page Accès bénéficiaire dans le menu à gauche.")


def main() -> None:
    # IMPORTANT :
    # Ne pas recréer un menu "Navigation" ici, car Streamlit affiche déjà les pages dans la sidebar.
    # Sinon tu auras un double menu (comme sur ta capture).
    home_page()


if __name__ == "__main__":
    main()
