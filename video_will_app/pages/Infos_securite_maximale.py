import streamlit as st

st.set_page_config(page_title="Informations à collecter pour une sécurité maximale", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 960px;
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
        margin-bottom: 14px;
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

st.title("Informations à collecter pour une sécurité maximale")

st.markdown(
    """
    <div class="hero-box">
        Objectif : protéger l’expéditeur, le destinataire et la plateforme.
        Les informations demandées renforcent la sécurité technique, la vérification d’identité
        et la bonne articulation avec les démarches notariales si nécessaire.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="sec-card">
        <div class="sec-title">Informations demandées à l’abonné (expéditeur)</div>
        <strong>Identité vérifiée (KYC simplifié)</strong><br><br>
        Obligatoire :
        <ul>
            <li>Nom complet</li>
            <li>Date de naissance</li>
            <li>Pièce d’identité (vérification automatique)</li>
            <li>Email vérifié</li>
            <li>Numéro de téléphone vérifié (SMS OTP)</li>
            <li>Pays de résidence</li>
            <li>Adresse IP enregistrée</li>
        </ul>
        Pour formule premium :
        <ul>
            <li>Pièce d’identité (vérification automatique)</li>
            <li>Selfie vidéo de validation</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="sec-card">
        <div class="sec-title">Sécurité compte</div>
        <ul>
            <li>Mot de passe fort obligatoire</li>
            <li>Double authentification (2FA)</li>
            <li>Question secrète</li>
            <li>Code de récupération</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="sec-card">
        <div class="sec-title">Informations demandées pour le destinataire</div>
        Minimum requis :
        <ul>
            <li>Nom complet</li>
            <li>Nom complet des parents</li>
            <li>Informations sur sa famille</li>
            <li>Email</li>
            <li>Numéro de téléphone</li>
            <li>Pays</li>
            <li>Adresse (localité)</li>
        </ul>
        Sécurité renforcée :
        <ul>
            <li>Histoire commune / élément d’authentification</li>
            <li>Question secrète personnalisée</li>
            <li>Code OTP envoyé par SMS</li>
            <li>Lien à usage unique</li>
            <li>Date limite d’accès</li>
            <li>Limitation du nombre de visionnages</li>
            <li>Option reconnaissance faciale (premium)</li>
            <li>Lien pour succession (actes notariés)</li>
        </ul>
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

st.markdown("---")
if st.button("Retour accueil", use_container_width=True):
    st.switch_page("app.py")
