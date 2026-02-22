import streamlit as st
from theme import apply_theme

# IMPORTANT :
# set_page_config doit être appelé une seule fois et avant tout st.* (sauf imports).
st.set_page_config(page_title="Testamentum", layout="wide")

apply_theme()

def home_page() -> None:
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Testamentum</div>
          <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
          <div class="tm-latin">Verba manent. Memoria custoditur.</div>

          <div style="height:14px"></div>

          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <span style="
              padding:6px 12px; border-radius:999px;
              border:1px solid rgba(255,255,255,0.16);
              background:rgba(255,255,255,0.08);
              font-size:12px;">Mémoire</span>

            <span style="
              padding:6px 12px; border-radius:999px;
              border:1px solid rgba(255,255,255,0.16);
              background:rgba(255,255,255,0.08);
              font-size:12px;">Transmission</span>

            <span style="
              padding:6px 12px; border-radius:999px;
              border:1px solid rgba(255,255,255,0.16);
              background:rgba(255,255,255,0.08);
              font-size:12px;">Confidentialité</span>

            <span style="
              padding:6px 12px; border-radius:999px;
              border:1px solid rgba(255,255,255,0.16);
              background:rgba(255,255,255,0.08);
              font-size:12px;">Traçabilité</span>
          </div>

          <div style="height:18px"></div>

          <div style="font-size:20px; font-weight:700;">
            Un message vidéo, transmis au bon moment.
          </div>

          <div style="height:10px"></div>

          <div style="color:rgba(255,255,255,0.86); line-height:1.6; font-size:14px;">
            Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
            lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse et structurée.
          </div>

          <div style="height:12px"></div>

          <ul style="color:rgba(255,255,255,0.86); line-height:1.7; font-size:14px; margin:0; padding-left:18px;">
            <li>Accès bénéficiaires par jeton temporaire sécurisé</li>
            <li>Validation notariale</li>
            <li>Journalisation des actions</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="tm-card">
          <div style="font-size:28px; font-weight:750; margin-bottom:6px;">Commencer</div>
          <div style="color:rgba(255,255,255,0.82); font-size:14px; line-height:1.5;">
            Saisissez votre adresse e-mail pour créer un compte ou vous connecter.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # Boutons parfaitement alignés (même ligne, même hauteur, même largeur)
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
        "<div style='margin-top:10px; color:rgba(255,255,255,0.65); font-size:12px;'>"
        "En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité."
        "</div>",
        unsafe_allow_html=True,
    )

    # Navigation : on redirige vers les pages existantes.
    # (Ça ne crée pas un compte ici : la création/connexion se fait dans la page Connexion.)
    if go_continue:
        # Option simple : pousser l’utilisateur vers la page Connexion
        # (Streamlit multipage)
        try:
            st.switch_page("pages/Connexion.py")
        except Exception:
            # Fallback si switch_page n'est pas dispo (vieilles versions)
            st.info("Ouvrez la page Connexion dans le menu à gauche.")

    if go_benef:
        try:
            st.switch_page("pages/Acces_beneficiaire.py")
        except Exception:
            st.info("Ouvrez la page Accès bénéficiaire dans le menu à gauche.")


def main() -> None:
    # Menu latéral simple (si tu utilises déjà des pages Streamlit, tu peux laisser le menu natif)
    st.sidebar.markdown("Navigation")
    st.sidebar.page_link("app.py", label="Accueil", icon=None)
    st.sidebar.page_link("pages/Connexion.py", label="Connexion", icon=None)
    st.sidebar.page_link("pages/Espace_Memoire.py", label="Espace Mémoire", icon=None)
    st.sidebar.page_link("pages/Acces_beneficiaire.py", label="Accès bénéficiaire", icon=None)

    home_page()


if __name__ == "__main__":
    main()
