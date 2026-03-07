import streamlit as st

st.set_page_config(page_title="Mentions légales", layout="centered")

st.markdown(
    """
    <style>
      .block-container { max-width: 980px; padding-top: 1.5rem; }
      a.anchor-link { display:none !important; }
      .section {
        border-bottom: 1px solid rgba(0,0,0,0.08);
        padding-bottom: 14px;
        margin-bottom: 18px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Mentions légales")

st.markdown("### Éditeur du site")
st.write(
    """
Kidan Vid  
Projet / service numérique de transmission sécurisée  
Les coordonnées exactes de l’éditeur, du responsable de publication et de l’hébergeur doivent être complétées avant mise en production publique.
"""
)

st.markdown("### Hébergement")
st.write(
    """
Le service peut être hébergé sur une infrastructure cloud compatible avec les exigences
de sécurité, de confidentialité et de conformité applicables au projet.
Les références exactes de l’hébergeur doivent être renseignées avant diffusion publique.
"""
)

st.markdown("### Propriété intellectuelle")
st.write(
    """
Le contenu du site, sa structure, ses textes, ses éléments graphiques, ses logos et sa charte visuelle
sont protégés. Toute reproduction non autorisée est interdite.
"""
)

st.markdown("### Responsabilité")
st.write(
    """
Le site présente un service de transmission sécurisée.
Les contenus juridiques ont une valeur informative générale et ne remplacent pas un conseil individualisé.
"""
)

st.markdown("### Point successoral")
st.write(
    """
En France, une vidéo seule ne constitue pas un testament juridiquement valable.
Le site doit être utilisé en articulation avec les formes juridiques reconnues et, si nécessaire, avec un notaire.
"""
)

st.markdown("### Contact")
st.write(
    """
Pour toute demande relative au site, à la sécurité ou aux accès :
utilisez la page “Nous contacter”.
"""
)

if st.button("Retour accueil"):
    st.switch_page("app.py")
