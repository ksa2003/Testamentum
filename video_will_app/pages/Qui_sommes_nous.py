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
Kidanmemoris est une capsule temporelle familiale numérique.
La plateforme permet de transmettre des messages vidéo, des souvenirs familiaux,
des lettres numériques et des contenus destinés à des moments de vie futurs.
"""
)

st.subheader("Notre fonctionnement")
st.markdown(
    """
- Création d’un coffre numérique sécurisé  
- Vérification d’identité et contact de confiance  
- Enregistrement ou téléversement de vidéos  
- Désignation de destinataires individuels ou familiaux  
- Transmission après décès, date programmée ou événement spécifique  
- Construction d’un arbre de mémoire familiale  
- Articulation avec un notaire partenaire pour les sujets successoraux  
"""
)

st.subheader("Notre vision")
st.markdown(
    """
Kidanmemoris repose sur quatre piliers :
- les **messages vidéo**
- les **moments de vie**
- la **mémoire familiale**
- le **cadre émotionnel, sécurisé et notarial**
"""
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Information juridique centrale</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris ne remplace pas le droit : la plateforme intègre le notaire pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Pourquoi ce positionnement ?")
st.write(
    """
Parce qu’un message important ne concerne pas uniquement l’après-décès.
Il peut aussi être destiné à un mariage, une naissance, un anniversaire,
ou une étape essentielle d’une vie familiale.
Kidanmemoris unit émotion, mémoire, famille, sécurité et patrimoine.
"""
)

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
