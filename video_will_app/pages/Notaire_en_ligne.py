import streamlit as st
from datetime import date
from pathlib import Path

from utils_media import show_logo

# -----------------------------
# Config
# -----------------------------
st.set_page_config(page_title="Notaire en ligne", layout="centered")

# -----------------------------
# Styles
# -----------------------------
st.markdown(
    """
    <style>
      .block-container { max-width: 900px; padding-top: 1.25rem; }
      .kv-muted { color: rgba(0,0,0,0.6); font-size: 0.95rem; }
      .kv-card { border: 1px solid rgba(0,0,0,0.08); border-radius: 14px; padding: 16px 16px; background: #ffffff; }
      hr { margin: 1.8rem 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
show_logo()

st.title("Notaire en ligne")
st.markdown(
    "<div class='kv-muted'>Préparez les informations nécessaires aux actes notariés (succession, testament, partage, donation, etc.).</div>",
    unsafe_allow_html=True,
)

st.markdown("---")

st.header("Informations à collecter pour les actes notariés")
st.markdown(
    """
Objectif : **protéger l’expéditeur (abonné), le(s) bénéficiaire(s) et la plateforme**, et faciliter le travail du notaire.

Les champs ci-dessous sont organisés en deux parties :
- **Informations demandées à l’abonné (expéditeur)**
- **Informations demandées pour le(s) bénéficiaire(s)**
"""
)

st.markdown("---")

# -----------------------------
# Form: Abonné (expéditeur)
# -----------------------------
st.subheader("Informations demandées à l’abonné (expéditeur)")

with st.expander("Identité vérifiée (KYC simplifié) – Obligatoire", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        exp_nom = st.text_input("Nom (expéditeur)", key="exp_nom")
        exp_dn = st.date_input("Date de naissance", value=None, key="exp_dn")
        exp_pays = st.text_input("Pays de résidence", key="exp_pays")
    with col2:
        exp_prenom = st.text_input("Prénom", key="exp_prenom")
        exp_ln = st.text_input("Lieu de naissance (optionnel)", key="exp_ln")
        exp_natio = st.text_input("Nationalité (optionnel)", key="exp_natio")

    exp_email = st.text_input("Email vérifié", key="exp_email")
    exp_tel = st.text_input("Numéro de téléphone vérifié (SMS OTP)", key="exp_tel")

    exp_adresse = st.text_area(
        "Adresse de résidence complète",
        placeholder="Numéro + rue\nCode postal + ville\nPays",
        key="exp_adresse",
        height=90,
    )

with st.expander("Pièce d’identité – Recommandé (Premium)", expanded=False):
    col1, col2, col3 = st.columns(3)
    with col1:
        id_type = st.selectbox("Type de pièce", ["Carte d'identité", "Passeport", "Titre de séjour", "Autre"], key="exp_id_type")
    with col2:
        id_num = st.text_input("Numéro de pièce", key="exp_id_num")
    with col3:
        id_exp = st.date_input("Date d’expiration", value=None, key="exp_id_exp")

    st.caption("Pour Premium : possibilité de demander une **selfie vidéo de validation** (à intégrer plus tard).")

with st.expander("Sécurité du compte", expanded=False):
    st.markdown(
        """
- Mot de passe fort obligatoire  
- Double authentification (2FA)  
- Question secrète  
- Codes de récupération  
- Adresse IP enregistrée (trace anti-fraude)  
"""
    )

st.markdown("---")

# -----------------------------
# Beneficiaires list (local UI)
# -----------------------------
st.subheader("Informations demandées pour le(s) bénéficiaire(s)")

if "notaire_beneficiaires" not in st.session_state:
    st.session_state.notaire_beneficiaires = []

with st.form("form_benef_notaire", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        b_nom = st.text_input("Nom", key="b_nom")
        b_lien = st.selectbox(
            "Lien",
            ["Conjoint(e)", "Enfant", "Parent", "Frère/Sœur", "Cousin/Cousine", "Ami(e)", "Notaire", "Autre"],
            key="b_lien",
        )
        b_dn = st.date_input("Date de naissance (si connue)", value=None, key="b_dn")
        b_tel = st.text_input("Téléphone", key="b_tel")
    with col2:
        b_prenom = st.text_input("Prénom", key="b_prenom")
        b_email = st.text_input("Email", key="b_email")
        b_pays = st.text_input("Pays", key="b_pays")
        b_adresse = st.text_area("Adresse (localité)", key="b_adresse", height=90)

    st.markdown("**Optionnel (sécurité renforcée / succession)**")
    col3, col4 = st.columns(2)
    with col3:
        b_id_type = st.selectbox("Type de pièce (optionnel)", ["", "Carte d'identité", "Passeport", "Autre"], key="b_id_type")
        b_id_num = st.text_input("Numéro de pièce (optionnel)", key="b_id_num")
    with col4:
        b_question = st.text_input("Question secrète personnalisée (optionnel)", key="b_question")
        b_indice = st.text_input("Indice / réponse attendue (optionnel)", key="b_indice")

    b_notes = st.text_area("Notes (optionnel)", key="b_notes", height=90)

    submitted = st.form_submit_button("Ajouter le bénéficiaire")
    if submitted:
        if not (b_nom and b_prenom):
            st.warning("Veuillez renseigner au minimum **Nom** et **Prénom**.")
        else:
            st.session_state.notaire_beneficiaires.append(
                {
                    "Nom": b_nom.strip(),
                    "Prénom": b_prenom.strip(),
                    "Lien": b_lien,
                    "Date de naissance": str(b_dn) if b_dn else "",
                    "Email": b_email.strip(),
                    "Téléphone": b_tel.strip(),
                    "Pays": b_pays.strip(),
                    "Adresse": b_adresse.strip(),
                    "Pièce (type)": b_id_type,
                    "Pièce (numéro)": b_id_num.strip(),
                    "Question secrète": b_question.strip(),
                    "Notes": b_notes.strip(),
                }
            )
            st.success("Bénéficiaire ajouté.")

if st.session_state.notaire_beneficiaires:
    st.markdown("#### Bénéficiaires enregistrés (local)")
    st.dataframe(st.session_state.notaire_beneficiaires, use_container_width=True, hide_index=True)
else:
    st.info("Aucun bénéficiaire enregistré pour l’instant.")

st.markdown("---")

st.subheader("Sécurité renforcée recommandée")
st.markdown(
    """
- Raconter une **histoire commune** (authentifier l’auteur de la vidéo)  
- **Code OTP** envoyé par SMS  
- Lien à **usage unique**  
- **Date limite d’accès**  
- Limitation du **nombre de visionnages**  
- Option reconnaissance faciale (Premium)  
- Lien pour succession (**actes notariés**)  
"""
)

st.markdown("---")

# -----------------------------
# Navigation
# -----------------------------
colA, colB = st.columns(2)
with colA:
    if st.button("Retour accueil"):
        st.switch_page("app.py")
with colB:
    if st.button("Accéder à l’espace mémoire"):
        st.switch_page("pages/Espace_Memoire.py")

st.caption("© Kidan Vid")
