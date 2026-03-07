import streamlit as st

st.set_page_config(page_title="Qui sommes-nous", layout="centered")

st.markdown(
    """
    <style>
      .block-container { max-width: 980px; padding-top: 1.5rem; }
      a.anchor-link { display:none !important; }
      .legal-box {
        border-left: 5px solid #0A66C2;
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Qui sommes-nous ?")

st.write(
    """
Kidan Vid est une plateforme pensée pour la transmission humaine, technique et juridique
de messages personnels, souvenirs audio/vidéo et documents sensibles.
Notre ambition est de permettre une transmission plus claire, plus protégée et mieux encadrée.
"""
)

st.subheader("Notre fonctionnement")
st.markdown(
    """
- Création d’un espace abonné sécurisé  
- Dépôt de vidéos, audios et documents  
- Désignation de bénéficiaires  
- Mise en place d’un accès contrôlé  
- Double authentification et journalisation  
- Articulation avec le notaire pour les sujets juridiques  
"""
)

st.subheader("Notre approche")
st.markdown(
    """
Kidan Vid repose sur quatre piliers :
- la **vidéo**
- l’**audio**
- la **sécurisation des données**
- le **notaire comme pilier central**
"""
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Information juridique centrale</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidan Vid ne remplace pas le droit : la plateforme intègre le notaire pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Pourquoi ce positionnement ?")
st.write(
    """
Parce que la valeur émotionnelle d’un message transmis peut être immense,
mais sa valeur juridique ne peut pas être improvisée.
La plateforme cherche donc à unir mémoire, sécurité et encadrement notarial.
"""
)

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
