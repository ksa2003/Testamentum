# pages/Espace_Memoire.py
import streamlit as st
from datetime import datetime
import secrets


# -----------------------------
# Helpers
# -----------------------------
def _safe_apply_theme():
    """
    Essaie d'appliquer ton thème si tu as un theme.py avec apply_theme().
    Ne casse jamais la page si le fichier n'existe pas.
    """
    try:
        from theme import apply_theme  # type: ignore
        apply_theme()
    except Exception:
        pass


def require_login():
    """
    Page protégée. On considère l'utilisateur connecté si st.session_state["user_email"] existe.
    Si absent -> redirection vers Connexion.
    """
    if not st.session_state.get("user_email"):
        st.warning("Vous devez vous connecter pour accéder à cet espace.")
        # Redirection Streamlit (nouvelle API)
        try:
            st.switch_page("pages/Connexion.py")
        except Exception:
            st.stop()


def logout_button():
    if st.button("Se déconnecter", use_container_width=True):
        for k in ["user_email", "is_authenticated"]:
            if k in st.session_state:
                del st.session_state[k]
        # Redirection vers Connexion
        try:
            st.switch_page("pages/Connexion.py")
        except Exception:
            st.stop()


def mask_email(email: str) -> str:
    if "@" not in email:
        return email
    name, domain = email.split("@", 1)
    if len(name) <= 2:
        masked = name[0] + "*" * 6
    else:
        masked = name[0] + "*" * max(6, len(name) - 2) + name[-1]
    return f"{masked}@{domain}"


# -----------------------------
# Page
# -----------------------------
_safe_apply_theme()
st.set_page_config(page_title="Espace Mémoire", layout="centered")

require_login()

email = st.session_state.get("user_email", "")
st.title("Espace Mémoire")
st.caption(f"Connecté en tant que : {mask_email(email)}")

st.divider()

tab_videos, tab_docs, tab_benef, tab_params = st.tabs(
    ["Vidéos", "Documents", "Bénéficiaires", "Paramètres"]
)

# -----------------------------
# Onglet Vidéos
# -----------------------------
with tab_videos:
    st.subheader("Vidéos")
    st.info("Zone privée à connecter ensuite à Supabase : upload, stockage, lecture, journalisation.")

    st.caption("Démo : pas encore branché à Supabase.")
    st.text_input("Rechercher une vidéo", placeholder="Titre, tag, bénéficiaire...")

    st.write("Aucune vidéo pour l’instant.")


# -----------------------------
# Onglet Documents
# -----------------------------
with tab_docs:
    st.subheader("Documents")
    st.info("Zone privée à connecter ensuite à Supabase : PDF, pièces, coffre-fort, versions.")

    st.caption("Démo : pas encore branché à Supabase.")
    st.text_input("Rechercher un document", placeholder="Nom, catégorie...")

    st.write("Aucun document pour l’instant.")


# -----------------------------
# Onglet Bénéficiaires
# -----------------------------
with tab_benef:
    st.subheader("Bénéficiaires")

    # Init stockage session
    if "beneficiaries" not in st.session_state:
        st.session_state["beneficiaries"] = []  # list[dict]

    st.caption("Démo locale (session). Prochaine étape : Supabase (table + RLS + journalisation).")

    with st.form("add_beneficiary", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            last_name = st.text_input("Nom", placeholder="Ex: Dupont")
            relation = st.selectbox(
                "Lien avec le testateur",
                ["Conjoint", "Enfant", "Parent", "Frère/Sœur", "Ami", "Notaire", "Autre"],
                index=1,
            )
            access_level = st.selectbox(
                "Niveau d'accès",
                ["Lecture seule", "Accès complet", "Accès conditionnel (post-décès)"],
                index=2,
            )
        with c2:
            first_name = st.text_input("Prénom", placeholder="Ex: Marie")
            ben_email = st.text_input("Email", placeholder="ex: marie.dupont@email.com")
            expiry_days = st.number_input(
                "Expiration du lien (jours)",
                min_value=1,
                max_value=3650,
                value=365,
                step=1,
            )

        notes = st.text_area(
            "Notes (optionnel)",
            placeholder="Ex: à prévenir en priorité, instructions, etc.",
            height=90,
        )

        submitted = st.form_submit_button("Ajouter le bénéficiaire", use_container_width=True)

        if submitted:
            if not last_name.strip() or not first_name.strip():
                st.error("Nom et prénom sont obligatoires.")
            elif "@" not in ben_email or "." not in ben_email:
                st.error("Email invalide.")
            else:
                # Code unique lisible (démo)
                code = secrets.token_urlsafe(8).replace("-", "").replace("_", "")[:10].upper()

                st.session_state["beneficiaries"].append(
                    {
                        "Nom": last_name.strip(),
                        "Prénom": first_name.strip(),
                        "Email": ben_email.strip(),
                        "Lien": relation,
                        "Accès": access_level,
                        "Expiration (jours)": int(expiry_days),
                        "Code": code,
                        "Notes": notes.strip(),
                        "Créé le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Bénéficiaire ajouté.")

    st.divider()

    if not st.session_state["beneficiaries"]:
        st.info("Aucun bénéficiaire enregistré pour l’instant.")
    else:
        st.write("Liste des bénéficiaires :")

        for idx, b in enumerate(st.session_state["beneficiaries"]):
            with st.container(border=True):
                colA, colB = st.columns([3, 1])

                with colA:
                    st.markdown(
                        f"**{b['Prénom']} {b['Nom']}**  \n"
                        f"Email : `{b['Email']}`  \n"
                        f"Lien : {b['Lien']}  \n"
                        f"Accès : {b['Accès']}  \n"
                        f"Expiration : {b['Expiration (jours)']} jours  \n"
                        f"Code d’accès : `{b['Code']}`  \n"
                        f"Créé le : {b['Créé le']}"
                    )
                    if b.get("Notes"):
                        st.caption(f"Notes : {b['Notes']}")

                with colB:
                    if st.button("Supprimer", key=f"del_benef_{idx}", use_container_width=True):
                        st.session_state["beneficiaries"].pop(idx)
                        st.rerun()

        st.divider()
        st.subheader("Partager un code d’accès (démo)")
        st.caption("En production : envoi email/SMS + journalisation + double validation.")
        st.info("Chaque bénéficiaire reçoit un code unique à utiliser dans « Accès bénéficiaire ».")


# -----------------------------
# Onglet Paramètres
# -----------------------------
with tab_params:
    st.subheader("Paramètres")
    st.info("Paramètres du compte (démo).")

    st.caption("Ici tu pourras ajouter : MFA, clés, préférences, sécurité, journal d’accès…")
    logout_button()    )

with tab_benef:
    st.subheader("Bénéficiaires")
    st.info("Section à connecter : codes d’accès, expirations, journalisation, double validation.")
    st.write("Prochaine étape : gérer les bénéficiaires via Supabase (table + RLS).")

with tab_settings:
    st.subheader("Paramètres")
    st.write("Sécurité et session")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Retour accueil", use_container_width=True):
            st.switch_page("app.py")
    with col2:
        if st.button("Se déconnecter", use_container_width=True):
            st.session_state["auth"] = False
            st.session_state["user_email"] = ""
            st.switch_page("pages/Connexion.py")
