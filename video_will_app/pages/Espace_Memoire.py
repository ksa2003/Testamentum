import streamlit as st
from datetime import date

st.set_page_config(page_title="Espace Mémoire", layout="wide")

# -----------------------------
# (Optionnel) : si tu as déjà un email en session
# Sinon on met un fallback
# -----------------------------
if "user_email" not in st.session_state:
    st.session_state["user_email"] = "said-ahmed2003@hotmail.com"

# -----------------------------
# Styles : enlève le petit symbole lien à côté des titres
# -----------------------------
st.markdown(
    """
    <style>
      a.anchor-link { display: none !important; }
      .block-container { max-width: 1100px; padding-top: 1.4rem; padding-bottom: 2.5rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Espace Mémoire")
st.caption(f"Connecté en tant que : {st.session_state['user_email']}")

st.markdown("---")

tabs = st.tabs(["Vidéos", "Documents", "Bénéficiaires", "Paramètres"])

# -----------------------------
# Onglet VIDÉOS
# -----------------------------
with tabs[0]:
    st.header("Vidéos")
    st.info("Fonctionnalité à compléter : dépôt / chiffrement / programmation / accès bénéficiaire.")
    if st.button("Retour accueil", key="retour_videos"):
        st.switch_page("app.py")

# -----------------------------
# Onglet DOCUMENTS
# -----------------------------
with tabs[1]:
    st.header("Documents")
    st.info("Fonctionnalité à compléter : dépôt de documents (actes, pièces, justificatifs, etc.).")
    if st.button("Retour accueil", key="retour_docs"):
        st.switch_page("app.py")

# -----------------------------
# Onglet BÉNÉFICIAIRES (placeholder)
# -----------------------------
with tabs[2]:
    st.header("Bénéficiaires")
    st.info("Ici tu gères la liste des bénéficiaires (formulaire + liste).")
    if st.button("Retour accueil", key="retour_benef"):
        st.switch_page("app.py")

# -----------------------------
# Onglet PARAMÈTRES (CORRIGÉ)
# -----------------------------
with tabs[3]:
    st.header("Paramètres")

    st.subheader("Informations de l’abonné (expéditeur)")
    st.write(
        "Ces informations servent à l’inscription, à la sécurité, et peuvent être requises pour certains documents (succession / notaire)."
    )

    # --- Valeurs par défaut (session_state) ---
    # Important : on ne met pas "" en dur dans l’aperçu.
    # On lit/écrit dans st.session_state via des keys stables.
    defaults = {
        "sub_nom": "",
        "sub_prenom": "",
        "sub_naissance": None,   # date_input gère None
        "sub_email": st.session_state["user_email"],
        "sub_pays": "",
        "sub_tel": "",
        "sub_adresse": "",
        "sub_piece_type": "",
        "sub_piece_num": "",
        "sub_piece_exp": None,
        "sub_notes": "",
        "sub_last_update": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # --- Formulaire : tout est lié à session_state via key= ---
    with st.form("abonnee_form", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Nom", key="sub_nom")
        with c2:
            st.text_input("Prénom", key="sub_prenom")

        c3, c4 = st.columns(2)
        with c3:
            st.date_input("Date de naissance", key="sub_naissance", value=st.session_state["sub_naissance"])
        with c4:
            # Email affiché, tu peux le bloquer si tu veux
            st.text_input("Email", key="sub_email")

        c5, c6 = st.columns(2)
        with c5:
            st.text_input("Pays", key="sub_pays")
            st.text_input("Téléphone", key="sub_tel")
        with c6:
            st.text_area(
                "Adresse complète",
                key="sub_adresse",
                height=96,
                placeholder="Numéro + rue\nCode postal + ville\nPays",
            )

        st.markdown("**Pièce d’identité (optionnel / Premium)**")
        p1, p2, p3 = st.columns(3)
        with p1:
            st.selectbox(
                "Type de pièce",
                ["", "Carte d'identité", "Passeport", "Titre de séjour", "Permis de conduire"],
                key="sub_piece_type",
            )
        with p2:
            st.text_input("Numéro de pièce", key="sub_piece_num")
        with p3:
            st.date_input("Date d’expiration", key="sub_piece_exp", value=st.session_state["sub_piece_exp"])

        st.text_area("Notes (optionnel)", key="sub_notes", height=90)

        submitted = st.form_submit_button("Enregistrer les informations")

    # --- Quand on clique "Enregistrer", on met à jour la date et on force l’aperçu à refléter l’entrée ---
    if submitted:
        st.session_state["sub_last_update"] = date.today().isoformat()
        st.success("Informations enregistrées (aperçu mis à jour).")
        st.rerun()

    st.markdown("---")

    # --- APERÇU : lit directement session_state (donc affiche ce que tu as saisi) ---
    st.subheader("Aperçu (abonné)")

    preview = {
        "Nom": st.session_state.get("sub_nom", ""),
        "Prénom": st.session_state.get("sub_prenom", ""),
        "Date de naissance": (
            st.session_state["sub_naissance"].isoformat()
            if isinstance(st.session_state.get("sub_naissance"), date)
            else ""
        ),
        "Email": st.session_state.get("sub_email", ""),
        "Téléphone": st.session_state.get("sub_tel", ""),
        "Pays": st.session_state.get("sub_pays", ""),
        "Adresse": st.session_state.get("sub_adresse", ""),
        "Pièce (type)": st.session_state.get("sub_piece_type", ""),
        "Pièce (numéro)": st.session_state.get("sub_piece_num", ""),
        "Pièce (expiration)": (
            st.session_state["sub_piece_exp"].isoformat()
            if isinstance(st.session_state.get("sub_piece_exp"), date)
            else ""
        ),
        "Dernière mise à jour": st.session_state.get("sub_last_update", ""),
    }

    st.json(preview, expanded=True)

    st.markdown("---")
    if st.button("Retour accueil", key="retour_params"):
        st.switch_page("app.py")

    st.caption("© Kidan Vid")
