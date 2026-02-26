import streamlit as st
from theme import apply_theme

apply_theme("Espace Mémoire")

# -------------------------------------------------------------------
# Guard: accès réservé aux utilisateurs connectés
# -------------------------------------------------------------------
if not st.session_state.get("auth", False):
    st.warning("Vous devez être connecté pour accéder à l’Espace Mémoire.")
    st.switch_page("pages/Connexion.py")

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def mask_email(email: str) -> str:
    """Masque l'email pour éviter l'affichage public + évite la mise en lien auto."""
    if not email or "@" not in email:
        return ""
    local, domain = email.split("@", 1)
    if len(local) <= 2:
        local_masked = local[0] + "*"
    else:
        local_masked = local[0] + "*" * (len(local) - 2) + local[-1]
    return f"{local_masked}@{domain}"

email = st.session_state.get("user_email", "")
masked = mask_email(email)

# -------------------------------------------------------------------
# UI
# -------------------------------------------------------------------
st.title("Espace Mémoire")

# Affichage email en "code" pour empêcher Streamlit de le rendre cliquable
if masked:
    st.markdown(f"Connecté en tant que : `{masked}`")
else:
    st.caption("Connecté")

st.divider()

# Init stockage démo en session (en attendant Supabase)
if "vault_videos" not in st.session_state:
    st.session_state["vault_videos"] = []  # list[dict{name, bytes}]
if "vault_docs" not in st.session_state:
    st.session_state["vault_docs"] = []    # list[dict{name, bytes}]
if "vault_notes" not in st.session_state:
    st.session_state["vault_notes"] = ""

tab_videos, tab_docs, tab_benef, tab_settings = st.tabs(
    ["Vidéos", "Documents", "Bénéficiaires", "Paramètres"]
)

with tab_videos:
    st.subheader("Vidéos")
    st.caption("Démo locale (session). Prochaine étape : stockage sécurisé Supabase.")
    up = st.file_uploader("Ajouter une vidéo", type=["mp4", "mov", "m4v"], accept_multiple_files=False)
    if up is not None:
        st.session_state["vault_videos"].append({"name": up.name, "data": up.getvalue()})
        st.success("Vidéo ajoutée à la session.")

    if st.session_state["vault_videos"]:
        st.write("Vos vidéos (session) :")
        for i, v in enumerate(st.session_state["vault_videos"], start=1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{i}. {v['name']}")
            with col2:
                st.download_button(
                    "Télécharger",
                    data=v["data"],
                    file_name=v["name"],
                    mime="video/mp4",
                    use_container_width=True,
                    key=f"dl_video_{i}",
                )
    else:
        st.info("Aucune vidéo pour l’instant.")

with tab_docs:
    st.subheader("Documents")
    st.caption("Démo locale (session). Prochaine étape : coffre-fort Supabase + droits d’accès.")
    doc = st.file_uploader("Ajouter un document", type=["pdf", "jpg", "jpeg", "png"], accept_multiple_files=False)
    if doc is not None:
        st.session_state["vault_docs"].append({"name": doc.name, "data": doc.getvalue()})
        st.success("Document ajouté à la session.")

    if st.session_state["vault_docs"]:
        st.write("Vos documents (session) :")
        for i, d in enumerate(st.session_state["vault_docs"], start=1):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"{i}. {d['name']}")
            with col2:
                st.download_button(
                    "Télécharger",
                    data=d["data"],
                    file_name=d["name"],
                    use_container_width=True,
                    key=f"dl_doc_{i}",
                )
    else:
        st.info("Aucun document pour l’instant.")

    st.divider()
    st.subheader("Notes privées")
    st.session_state["vault_notes"] = st.text_area(
        "Notes",
        value=st.session_state["vault_notes"],
        height=160,
        placeholder="Écrivez ici des informations privées (démo session).",
    )

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
