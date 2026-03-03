import streamlit as st

st.set_page_config(page_title="Sécurité technique", layout="wide")

st.title("Sécurité technique indispensable")

st.markdown(
    """
- Chiffrement AES-256 des vidéos  
- Chiffrement SSL/TLS  
- Hébergement européen (RGPD)  
- Logs d’accès horodatés  
- Suppression automatique après X jours dès le premier visionnage  
- Blocage capture écran (si possible techniquement)  
- Filigrane invisible personnalisé  
"""
)

st.warning(
    "Note produit : la « non-téléchargeabilité » et le « blocage capture écran » ne sont jamais garantis à 100% "
    "sur un appareil utilisateur. On peut fortement limiter (tokens courts, lecteur web, watermark, audit trail), "
    "mais pas empêcher totalement l’enregistrement écran."
)

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Informations sécurité maximale", use_container_width=True):
        st.switch_page("pages/Infos_securite_maximale.py")
with c2:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
