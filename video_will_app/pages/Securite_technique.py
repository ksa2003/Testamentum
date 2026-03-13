import streamlit as st

st.set_page_config(page_title="Sécurité technique", layout="centered")

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
      .hero-box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 18px;
        padding: 20px;
        background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
        margin-bottom: 18px;
      }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
      .sec-card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        padding: 16px;
        background: #ffffff;
        height: 100%;
      }}
      .sec-title {{
        font-weight: 700;
        color: {BLUE_DARK};
        margin-bottom: 8px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Sécurité technique")

st.markdown(
    """
    <div class="hero-box">
        Kidanmemoris protège le coffre du patrimoine émotionnel avec une logique de sécurité multicouche :
        chiffrement, accès limité, authentification forte, durée de consultation encadrée et traçabilité.
        La plateforme sécurise les messages vidéo, les souvenirs familiaux, les lettres numériques
        et les contenus transmis pour des moments de vie importants.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
        <div class="sec-card">
            <div class="sec-title">Protection du contenu</div>
            - Chiffrement des vidéos, lettres numériques et documents<br>
            - Chiffrement SSL/TLS des échanges<br>
            - Hébergement sécurisé selon l’infrastructure retenue
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="sec-card">
            <div class="sec-title">Contrôle d’accès</div>
            - OTP<br>
            - Double authentification (2FA)<br>
            - Liens uniques et accès limités dans le temps
        </div>
        """,
        unsafe_allow_html=True,
    )

c3, c4 = st.columns(2)
with c3:
    st.markdown(
        """
        <div class="sec-card">
            <div class="sec-title">Traçabilité</div>
            - Logs d’accès horodatés<br>
            - Historique des ouvertures<br>
            - Option de visionnage unique ou limité
        </div>
        """,
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        """
        <div class="sec-card">
            <div class="sec-title">Mesures avancées</div>
            - Filigrane invisible personnalisé<br>
            - Suppression automatique après délai si configurée<br>
            - Restrictions techniques complémentaires selon les besoins de transmission
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="legal-box">
        <strong>Rappel juridique</strong><br>
        La sécurité technique ne remplace pas la validité juridique.
        En France, une vidéo seule ne constitue pas un testament juridiquement valable ;
        l’intervention du notaire reste centrale pour toute transmission successorale.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Témoignage lié à la sécurité")
st.video("https://www.youtube.com/watch?v=qk4XuiQGAtw")

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
