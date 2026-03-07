import streamlit as st

st.set_page_config(page_title="Comment ça marche", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 920px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
      }}
      a.anchor-link {{
        display: none !important;
      }}
      .step-card {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 16px;
        padding: 18px;
        background: #ffffff;
        margin-bottom: 14px;
      }}
      .step-title {{
        font-weight: 700;
        color: {BLUE_DARK};
        margin-bottom: 6px;
      }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
      .hero-box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 18px;
        padding: 20px;
        background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
        margin-bottom: 18px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Comment ça marche ?")

st.markdown(
    """
    <div class="hero-box">
        La plateforme guide l’abonné depuis le dépôt du contenu jusqu’à l’ouverture sécurisée
        par le bénéficiaire, avec un encadrement technique et, si nécessaire, notarial.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step-card">
        <div class="step-title">1) Vous déposez votre contenu</div>
        Vidéo, audio ou document. Le contenu entre dans un parcours sécurisé.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step-card">
        <div class="step-title">2) Vous identifiez le destinataire</div>
        Vous reliez le contenu à un bénéficiaire désigné avec ses informations de contact.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step-card">
        <div class="step-title">3) Vous définissez les règles d’accès</div>
        OTP, double authentification, date limite, nombre maximal de visionnages, accès immédiat ou programmé.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step-card">
        <div class="step-title">4) Le contenu est transmis selon vos paramètres</div>
        Le bénéficiaire reçoit un accès personnel, protégé et traçable.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="step-card">
        <div class="step-title">5) Le notaire intervient si nécessaire</div>
        Pour les contenus ou intentions à portée successorale, la plateforme s’appuie sur un pilier notarial.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Témoignage lié à la transmission")
st.video("https://www.youtube.com/watch?v=RwQvEs_PkKA")

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
