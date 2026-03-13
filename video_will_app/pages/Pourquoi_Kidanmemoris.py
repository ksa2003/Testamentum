import streamlit as st

st.set_page_config(page_title="Pourquoi Kidanmemoris", layout="centered")

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
      .feature-card {{
        border: 1px solid rgba(10,102,194,0.14);
        border-radius: 14px;
        padding: 16px;
        background: #ffffff;
        height: 100%;
      }}
      .feature-title {{
        font-weight: 700;
        color: {BLUE_DARK};
        margin-bottom: 6px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Pourquoi Kidanmemoris ?")

st.markdown(
    """
    <div class="hero-box">
        <div style="font-size:1.05rem;color:#12344D;">
            Kidanmemoris unit mémoire humaine, sécurité technologique et cadre juridique.
            La plateforme devient une capsule temporelle familiale numérique,
            permettant de transmettre des messages émotionnels et patrimoniaux.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Rappel juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris intègre le notaire comme pilier central pour sécuriser toute transmission patrimoniale.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Transmission émotionnelle</div>
            Préserver une voix, un message, une mémoire familiale au-delà du simple écrit.
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Sécurité numérique avancée</div>
            Chiffrement, authentification forte, limitation d’accès et traçabilité.
        </div>
        """,
        unsafe_allow_html=True,
    )

c3, c4 = st.columns(2)
with c3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Arbre de mémoire familiale</div>
            Organisation des souvenirs et messages à travers les générations.
        </div>
        """,
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Pilier notarial intégré</div>
            Possibilité d’associer les vidéos aux démarches successorales officielles.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.subheader("Témoignage lié à la transmission émotionnelle")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.markdown("---")

if st.button("Retour accueil"):
    st.switch_page("app.py")
