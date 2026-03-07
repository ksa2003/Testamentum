import streamlit as st

st.set_page_config(page_title="Pourquoi Kidan Vid", layout="centered")

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

st.title("Pourquoi Kidan Vid ?")

st.markdown(
    """
    <div class="hero-box">
        <div style="font-size:1.05rem;color:#12344D;">
            Kidan Vid unit mémoire humaine, sécurité technique et cadre juridique.
            La plateforme n’est pas pensée comme un simple dépôt vidéo, mais comme
            une solution de transmission structurée.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Rappel juridique</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Transmission humaine</div>
            Préserver un message, une voix, une intention ou un souvenir au-delà du simple écrit.
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Sécurité d’accès</div>
            Chiffrement, OTP, 2FA, limitation du nombre de visionnages et journalisation.
        </div>
        """,
        unsafe_allow_html=True,
    )

c3, c4 = st.columns(2)
with c3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Gestion des bénéficiaires</div>
            Association précise des contenus à une ou plusieurs personnes avec règles d’accès.
        </div>
        """,
        unsafe_allow_html=True,
    )
with c4:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">Pilier notarial</div>
            Quand la portée juridique l’exige, le notaire devient l’élément central de la transmission.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("Témoignage lié à la confiance")
st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
