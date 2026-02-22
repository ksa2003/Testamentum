import streamlit as st
from theme import apply_theme


def _hero_section() -> None:
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

          <div style="margin-top:8px;">
            <div style="font-size:30px; font-weight:750; color:rgba(255,255,255,0.95); margin-bottom:10px;">
              Un message vidéo, transmis au bon moment.
            </div>
            <div class="tm-muted" style="font-size:16px; line-height:1.65;">
              Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des
              bénéficiaires lorsque le décès est déclaré. Le service est conçu pour une transmission
              respectueuse et structurée.
            </div>
            <div style="margin-top:14px;">
              <ul style="margin:0; padding-left:18px; color:rgba(255,255,255,0.85); font-size:16px; line-height:1.8;">
                <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
                <li>Validation notariale</li>
                <li>Journalisation des actions</li>
              </ul>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _start_section() -> None:
    st.markdown(
        """
        <div class="tm-card" style="padding:22px 26px;">
          <div style="font-size:18px; font-weight:750; color:rgba(255,255,255,0.92); margin-bottom:6px;">
            Commencer
          </div>
          <div class="tm-muted" style="font-size:15px;">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # FORM = alignement parfait des 2 boutons (même composant)
    with st.form("start_form", clear_on_submit=False):
        email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

        c1, c2 = st.columns(2, gap="small")
        with c1:
            go_continue = st.form_submit_button("Continuer", use_container_width=True)
        with c2:
            go_benef = st.form_submit_button("Accès bénéficiaire", use_container_width=True)

    st.markdown(
        '<div class="tm-muted" style="font-size:13px; margin-top:10px;">'
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
        "</div>",
        unsafe_allow_html=True,
    )

    # Actions
    if go_benef:
        st.switch_page("pages/Acces_beneficiaire.py")

    if go_continue:
        # Ici tu branches ta logique de connexion/inscription réelle.
        # Pour l’instant on redirige vers la page Connexion (si tu as cette page).
        st.switch_page("pages/Connexion.py")


def main() -> None:
    # IMPORTANT: set_page_config une seule fois, ici (pas dans theme.py)
    st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

    apply_theme()

    _hero_section()
    st.write("")  # petit espace
    _start_section()


if __name__ == "__main__":
    main()
