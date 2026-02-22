import streamlit as st
from theme import apply_theme


def render_home() -> None:
    apply_theme()

    # Carte principale (titre + pitch + bulles + features)
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Testamentum</div>
          <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
          <div class="tm-latin">Verba manent. Memoria custoditur.</div>

          <div style="height:14px"></div>

          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <span style="padding:6px 12px; border-radius:999px;
                         border:1px solid rgba(255,255,255,0.16);
                         background:rgba(255,255,255,0.08);
                         font-size:12px; color:rgba(255,255,255,0.92);">
              Mémoire
            </span>
            <span style="padding:6px 12px; border-radius:999px;
                         border:1px solid rgba(255,255,255,0.16);
                         background:rgba(255,255,255,0.08);
                         font-size:12px; color:rgba(255,255,255,0.92);">
              Transmission
            </span>
            <span style="padding:6px 12px; border-radius:999px;
                         border:1px solid rgba(255,255,255,0.16);
                         background:rgba(255,255,255,0.08);
                         font-size:12px; color:rgba(255,255,255,0.92);">
              Confidentialité
            </span>
            <span style="padding:6px 12px; border-radius:999px;
                         border:1px solid rgba(255,255,255,0.16);
                         background:rgba(255,255,255,0.08);
                         font-size:12px; color:rgba(255,255,255,0.92);">
              Traçabilité
            </span>
          </div>

          <div style="height:18px"></div>

          <div style="font-size:26px; font-weight:750; letter-spacing:-0.01em; color:rgba(255,255,255,0.96);">
            Un message vidéo, transmis au bon moment.
          </div>

          <div style="height:10px"></div>

          <div style="font-size:14px; line-height:1.55; color:rgba(255,255,255,0.84);">
            Enregistrez un message destiné à vos proches, puis contrôlez précisément l'accès des bénéficiaires
            lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
          </div>

          <div style="height:12px"></div>

          <ul style="margin: 0 0 0 18px; color:rgba(255,255,255,0.86); line-height:1.9; font-size:14px;">
            <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
            <li>Validation notariale</li>
            <li>Journalisation des actions</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,  # <-- INDISPENSABLE pour que les bulles s’affichent
    )

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # Carte “Commencer” (texte en nuances de blanc, pas gris illisible)
    st.markdown(
        """
        <div class="tm-card" style="padding:20px 26px;">
          <div style="font-size:18px; font-weight:750; color:rgba(255,255,255,0.92);">Commencer</div>
          <div style="margin-top:6px; font-size:14px; color:rgba(255,255,255,0.82);">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    email = st.text_input("Adresse e-mail", placeholder="votre-email@example.com")

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # Deux boutons alignés et de même taille (comme tu veux)
    c1, c2 = st.columns(2, gap="large")
    with c1:
        if st.button("Continuer", use_container_width=True):
            st.session_state["email_tmp"] = email
            # navigation vers Connexion (ou ton flux)
            st.switch_page("pages/Connexion.py")
    with c2:
        if st.button("Accès bénéficiaire", use_container_width=True):
            st.switch_page("pages/Acces_beneficiaire.py")

    st.markdown(
        """
        <div style="margin-top:14px; font-size:12px; color:rgba(255,255,255,0.78);">
          En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité.
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    # IMPORTANT : set_page_config doit être appelé UNE seule fois et tout en haut si tu l’utilises ailleurs.
    # Ici on ne l'appelle pas pour éviter tes erreurs StreamlitAPIException.
    render_home()


if __name__ == "__main__":
    main()
