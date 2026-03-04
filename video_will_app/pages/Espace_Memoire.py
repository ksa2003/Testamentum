import streamlit as st
from datetime import datetime, date
import secrets

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(page_title="Espace Mémoire", layout="centered")

# -----------------------------
# Sécurité : accès protégé
# -----------------------------
if "user_email" not in st.session_state:
    st.warning("Vous devez être connecté pour accéder à cet espace.")
    st.switch_page("pages/Connexion.py")
    st.stop()

# -----------------------------
# Helpers
# -----------------------------
def mask_email(email: str) -> str:
    if "@" not in email:
        return email
    name, domain = email.split("@", 1)
    if len(name) <= 2:
        masked = "*" * len(name)
    else:
        masked = name[0] + "*" * (len(name) - 2) + name[-1]
    return f"{masked}@{domain}"

def gen_id() -> str:
    return secrets.token_hex(8)

# -----------------------------
# State init
# -----------------------------
if "beneficiaires" not in st.session_state:
    st.session_state.beneficiaires = []  # local list (UI only)

# -----------------------------
# Header
# -----------------------------
st.title("Espace Mémoire")
st.caption(f"Connecté en tant que : {mask_email(st.session_state.get('user_email', ''))}")

st.markdown("---")

# -----------------------------
# Tabs
# -----------------------------
tab_videos, tab_docs, tab_benef, tab_params = st.tabs(["Vidéos", "Documents", "Bénéficiaires", "Paramètres"])

with tab_videos:
    st.subheader("Vidéos")
    st.info("Fonctionnalité à compléter : dépôt / chiffrement / programmation / accès bénéficiaire.")

with tab_docs:
    st.subheader("Documents")
    st.info("Fonctionnalité à compléter : dépôt de documents (actes, pièces, justificatifs, etc.).")

with tab_benef:
    st.subheader("Bénéficiaires")

    st.markdown(
        """
Renseignez ici les informations de vos bénéficiaires.  
Ces informations sont utiles pour **l’accès sécurisé** et, si besoin, pour **les actes notariés**.

Les données ci-dessous sont stockées **uniquement en mémoire côté app** (prototype).  
"""
    )

    with st.form("form_add_benef", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom", key="b_nom")
            lien = st.selectbox(
                "Lien",
                ["Conjoint(e)", "Enfant", "Parent", "Frère/Sœur", "Cousin/Cousine", "Ami(e)", "Notaire", "Autre"],
                key="b_lien",
            )
            niveau = st.selectbox("Niveau d’accès", ["Lecture seule", "Lecture + téléchargement", "Accès total"], key="b_niveau")
            tel = st.text_input("Téléphone", key="b_tel")
            pays = st.text_input("Pays", key="b_pays")
        with col2:
            prenom = st.text_input("Prénom", key="b_prenom")
            email = st.text_input("Email", key="b_email")
            dn = st.date_input("Date de naissance (si connue)", value=None, key="b_dn")
            adresse = st.text_area(
                "Adresse (localité)",
                placeholder="Ville / Code postal / Pays (ou adresse complète si nécessaire)",
                key="b_adresse",
                height=90,
            )

        st.markdown("**Vérification d’identité (optionnel / Premium)**")
        col3, col4 = st.columns(2)
        with col3:
            id_type = st.selectbox("Type de pièce (optionnel)", ["", "Carte d'identité", "Passeport", "Autre"], key="b_id_type")
        with col4:
            id_num = st.text_input("Numéro de pièce (optionnel)", key="b_id_num")

        notes = st.text_area("Notes (optionnel)", key="b_notes", height=90)

        submitted = st.form_submit_button("Ajouter le bénéficiaire")
        if submitted:
            if not (nom and prenom and email):
                st.warning("Veuillez renseigner au minimum : **Nom**, **Prénom** et **Email**.")
            else:
                st.session_state.beneficiaires.append(
                    {
                        "id": gen_id(),
                        "Nom": nom.strip(),
                        "Prénom": prenom.strip(),
                        "Lien": lien,
                        "Email": email.strip(),
                        "Téléphone": tel.strip(),
                        "Pays": pays.strip(),
                        "Adresse": adresse.strip(),
                        "Date de naissance": str(dn) if dn else "",
                        "Pièce (type)": id_type,
                        "Pièce (numéro)": id_num.strip(),
                        "Niveau d’accès": niveau,
                        "Notes": notes.strip(),
                        "Créé le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Bénéficiaire ajouté.")

    st.markdown("---")

    if st.session_state.beneficiaires:
        st.markdown("#### Bénéficiaires enregistrés (local)")
        display_rows = [
            {k: v for k, v in row.items() if k != "id"} for row in st.session_state.beneficiaires
        ]
        st.dataframe(display_rows, use_container_width=True, hide_index=True)

        with st.expander("Supprimer un bénéficiaire", expanded=False):
            ids = [b["id"] for b in st.session_state.beneficiaires]
            labels = [f'{b["Nom"]} {b["Prénom"]} — {b["Email"]}' for b in st.session_state.beneficiaires]
            choice = st.selectbox("Choisir", list(range(len(ids))), format_func=lambda i: labels[i])
            if st.button("Supprimer"):
                del st.session_state.beneficiaires[choice]
                st.success("Bénéficiaire supprimé.")
                st.rerun()
    else:
        st.info("Aucun bénéficiaire enregistré.")

with tab_params:
    st.subheader("Paramètres")
    st.info("À compléter : gestion du compte, sécurité, 2FA, récupération, etc.")

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
