import streamlit as st

st.set_page_config(page_title="Notaire en ligne", layout="centered")

BLUE_MAIN = "#0A66C2"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 960px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
      }}
      a.anchor-link {{
        display:none !important;
      }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
      .card {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 16px;
        padding: 18px;
        background: white;
        margin-bottom: 16px;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Notaire en ligne")

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique central</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Pourquoi le notaire est central")
st.markdown(
    """
- Encadrement juridique de la transmission  
- Vérification de la cohérence successorale  
- Sécurisation des actes et documents  
- Meilleure articulation entre mémoire personnelle et droit  
"""
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Ce que gère la partie notariale")
st.markdown(
    """
- Analyse des documents utiles  
- Préparation des actes et pièces  
- Coordination avec les bénéficiaires  
- Formalisation quand la situation l’exige  
"""
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Témoignage lié au cadre notarial")
st.video("https://www.youtube.com/watch?v=bkOKj_hWCj4")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
