import streamlit as st
from theme import apply_theme

st.set_page_config(page_title="Kidan Vid", page_icon="🎥", layout="centered")
apply_theme()


def _hero_section() -> None:
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Kidan Vid</div>
          <div class="tm-sub">Plateforme sécurisée de transmission vidéo post-mortem</div>
          <div class="tm-muted" style="margin-top:4px;">Avec Kidan Vid, nos mots ont plus de valeur que nos biens.</div>
          <div class="tm-latin" style="margin-top:6px;">Verba manent. Memoria custoditur.</div>

          <div class="tm-chips">
            <span class="tm-chip">Mémoire</span>
            <span class="tm-chip">Transmission</span>
            <span class="tm-chip">Confidentialité</span>
            <span class="tm-chip">Traçabilité</span>
          </div>

          <div style="margin-top:8px;">
            <div style="font-size:30px; font-weight:750; color:rgba(255,255,255,0.95); margin-bottom:10px;">
              Un message vidéo, transmis au bon moment.
            </div>
            <div class="tm-muted" style="font-size:16px; line-height:1.65;">
              Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires lorsque le décès est déclaré.
              Le service est conçu pour une transmission respectueuse et structurée.
            </div>
            <ul style="margin-top:12px; color:rgba(255,255,255,0.86); font-size:15px; line-height:1.7;">
              <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
              <li>Option de validation notariale</li>
              <li>Journalisation des actions</li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _start_section() -> None:
    st.markdown(
        """
        <div class="tm-card2">
          <div class="tm-h3">Commencer</div>
          <div class="tm-muted" style="margin-top:6px;">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    _hero_section()
    st.write("")
    _start_section()
    st.write("")

    with st.form("start_form", clear_on_submit=False):
        email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
            go = st.form_submit_button("Continuer")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            access = st.form_submit_button("Accès bénéficiaire")

    st.markdown(
        '<div class="tm-muted" style="margin-top:10px;">'
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
        "</div>",
        unsafe_allow_html=True,
    )

    if go:
        if not email.strip():
            st.error("Veuillez saisir une adresse e-mail.")
            st.stop()
        st.session_state["email"] = email.strip()
        st.switch_page("pages/Connexion.py")

    if access:
        st.switch_page("pages/Acces_beneficiaire.py")


if __name__ == "__main__":
    main()
