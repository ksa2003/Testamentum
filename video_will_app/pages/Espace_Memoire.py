import streamlit as st
from datetime import datetime
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
        masked = name[0] + "******"
    else:
        masked = name[0] + "*" * max(6, len(name) - 2) + name[-1]
    return f"{masked}@{domain}"


def logout():
    for key in ["user_email", "is_authenticated"]:
        if key in st.session_state:
            del st.session_state[key]
    st.switch_page("pages/Connexion.py")


# -----------------------------
# Interface principale
# -----------------------------
email = st.session_state["user_email"]

st.title("Espace Mémoire")
st.caption(f"Connecté en tant que : {mask_email(email)}")

st.divider()

tab_videos, tab_docs, tab_benef, tab_params = st.tabs(
    ["Vidéos", "Documents", "Bénéficiaires", "Paramètres"]
)

# =====================================================
# ONGLET VIDÉOS
# =====================================================
with tab_videos:
    st.subheader("Vidéos")
    st.info("Zone privée à connecter ensuite à Supabase : upload, stockage, lecture, journalisation.")
    st.write("Aucune vidéo pour l’instant.")


# =====================================================
# ONGLET DOCUMENTS
# =====================================================
with tab_docs:
    st.subheader("Documents")
    st.info("Zone privée à connecter ensuite à Supabase : coffre-fort numérique sécurisé.")
    st.write("Aucun document pour l’instant.")


# =====================================================
# ONGLET BÉNÉFICIAIRES
# =====================================================
with tab_benef:
    st.subheader("Bénéficiaires")

    if "beneficiaries" not in st.session_state:
        st.session_state["beneficiaries"] = []

    with st.form("add_beneficiary", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            last_name = st.text_input("Nom")
            relation = st.selectbox(
                "Lien",
                ["Conjoint", "Enfant", "Parent", "Frère/Sœur", "Ami", "Notaire", "Autre"]
            )
            access_level = st.selectbox(
                "Niveau d'accès",
                ["Lecture seule", "Accès complet", "Accès conditionnel (post-décès)"]
            )

        with col2:
            first_name = st.text_input("Prénom")
            ben_email = st.text_input("Email")
            expiry_days = st.number_input(
                "Expiration (jours)",
                min_value=1,
                max_value=3650,
                value=365
            )

        notes = st.text_area("Notes (optionnel)")
        submitted = st.form_submit_button("Ajouter le bénéficiaire", use_container_width=True)

        if submitted:
            if not last_name or not first_name:
                st.error("Nom et prénom obligatoires.")
            elif "@" not in ben_email:
                st.error("Email invalide.")
            else:
                code = secrets.token_urlsafe(8).replace("-", "").replace("_", "")[:10].upper()

                st.session_state["beneficiaries"].append({
                    "Nom": last_name,
                    "Prénom": first_name,
                    "Email": ben_email,
                    "Lien": relation,
                    "Accès": access_level,
                    "Expiration": expiry_days,
                    "Code": code,
                    "Créé le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Notes": notes
                })

                st.success("Bénéficiaire ajouté.")

    st.divider()

    if not st.session_state["beneficiaries"]:
        st.info("Aucun bénéficiaire enregistré.")
    else:
        for idx, b in enumerate(st.session_state["beneficiaries"]):
            with st.container(border=True):
                colA, colB = st.columns([3, 1])

                with colA:
                    st.markdown(
                        f"""
**{b['Prénom']} {b['Nom']}**  
Email : `{b['Email']}`  
Lien : {b['Lien']}  
Accès : {b['Accès']}  
Expiration : {b['Expiration']} jours  
Code : `{b['Code']}`  
Créé le : {b['Créé le']}
"""
                    )
                    if b["Notes"]:
                        st.caption(f"Notes : {b['Notes']}")

                with colB:
                    if st.button("Supprimer", key=f"delete_{idx}", use_container_width=True):
                        st.session_state["beneficiaries"].pop(idx)
                        st.rerun()


# =====================================================
# ONGLET PARAMÈTRES
# =====================================================
with tab_params:
    st.subheader("Paramètres")
    st.info("Paramètres du compte (démo).")

    if st.button("Se déconnecter", use_container_width=True):
        logout()
