import streamlit as st
from theme import apply_theme


def render_home() -> None:
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Testamentum</div>
          <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
          <div class="tm-latin">Verba manent. Memoria custoditur.</div>

          <div class="tm-chips">
            <span class="tm-chip">Mémoire</span>
            <span class="tm-chip">Transmission</span>
            <span class="tm-chip">Confidentialité</span>
            <span class="tm-chip">Traçabilité</span>
          </div>

          <div style="font-size:28px; font-weight:750; color: rgba(255,255,255,0.95); margin: 0 0 10px 0;">
            Un message vidéo, transmis au bon moment.
          </div>

          <div class="tm-muted" style="font-size:16px; line-height:1.55; margin-bottom: 12px;">
            Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
            lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
          </div>

          <ul class="tm-muted" style="margin: 0 0 0 18px; line-height:1.8; font-size:16px;">
            <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
            <li>Validation notariale</li>
            <li>Journalisation des actions</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div style="height:14px"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-strong" style="font-size:18px; margin-bottom:6px;">Commencer</div>
          <div class="tm-muted" style="font-size:15px;">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)

    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
        go_connexion = st.button("Continuer", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        go_benef = st.button("Accès bénéficiaire", use_container_width=True)

    st.markdown(
        '<div class="tm-muted" style="font-size:13px; margin-top:10px;">'
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
        "</div>",
        unsafe_allow_html=True,
    )

    if go_connexion:
        st.switch_page("pages/Connexion.py")

    if go_benef:
        st.switch_page("pages/Acces_beneficiaire.py")


def main() -> None:
    st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")
    apply_theme()
    render_home()


if __name__ == "__main__":
    main()
