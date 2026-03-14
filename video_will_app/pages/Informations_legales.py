import streamlit as st

st.set_page_config(page_title="Informations légales", layout="centered")

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

st.title("Informations légales")

st.write(
    """
Cette page rassemble les éléments d’information juridique, réglementaire et fonctionnelle
du service Kidanmemoris.
"""
)

st.subheader("Nature du service")
st.markdown(
    """
Kidanmemoris est un service numérique de transmission sécurisée de contenus :
- vidéos
- audios
- documents
- paramètres d’accès bénéficiaire
"""
)

st.subheader("Cadre de responsabilité")
st.markdown(
    """
Le service a pour objet d’organiser une transmission sécurisée.
Il ne remplace ni un conseil juridique individualisé, ni les formes légales exigées pour les actes de succession.
"""
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Rappel essentiel</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Le recours au notaire reste central pour toute transmission à portée successorale.
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Données et sécurité")
st.markdown(
    """
- chiffrement des contenus  
- authentification renforcée  
- journalisation des accès  
- durée de conservation à définir selon le service  
- limitation de l’accès et du nombre de consultations  
"""
)

st.subheader("Bénéficiaires et accès")
st.markdown(
    """
L’accès d’un bénéficiaire peut dépendre :
- de son identité
- de sa relation avec l’abonné
- d’un OTP
- d’un lien unique
- d’une limite de durée ou de visionnage
"""
)

if st.button("Retour accueil"):
    st.switch_page("app.py")
