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


def _ensure_lists():
    if "uploaded_videos" not in st.session_state:
        st.session_state["uploaded_videos"] = []
    if "uploaded_docs" not in st.session_state:
        st.session_state["uploaded_docs"] = []
    if "uploaded_audios" not in st.session_state:
        st.session_state["uploaded_audios"] = []
    if "saved_texts" not in st.session_state:
        st.session_state["saved_texts"] = []
    if "beneficiaries" not in st.session_state:
        st.session_state["beneficiaries"] = []


_ensure_lists()


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

    st.info("Ajoutez vos vidéos ici (stockage local Streamlit pour l’instant).")

    uploaded_video = st.file_uploader(
        "Téléverser une vidéo",
        type=["mp4", "mov", "m4v", "webm"],
        accept_multiple_files=False,
        key="video_uploader",
    )

    if uploaded_video is not None:
        st.session_state["uploaded_videos"].append(
            {
                "name": uploaded_video.name,
                "bytes": uploaded_video.getvalue(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        )
        st.success("Vidéo ajoutée.")
        st.rerun()

    st.divider()

    if not st.session_state["uploaded_videos"]:
        st.write("Aucune vidéo pour l’instant.")
    else:
        for i, v in enumerate(reversed(st.session_state["uploaded_videos"])):
            with st.container(border=True):
                st.write(f"**{v['name']}**")
                st.caption(f"Ajouté le {v['created_at']}")
                st.video(v["bytes"])

                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button("Supprimer", key=f"del_video_{i}", use_container_width=True):
                        # supprimer l’élément correspondant dans la liste d’origine
                        idx_in_list = len(st.session_state["uploaded_videos"]) - 1 - i
                        st.session_state["uploaded_videos"].pop(idx_in_list)
                        st.rerun()
                with col2:
                    st.empty()


# =====================================================
# ONGLET DOCUMENTS (documents + audio + texte)
# =====================================================
with tab_docs:
    st.subheader("Documents, audio et texte")

    st.info("Ajoutez des fichiers (PDF, images, audio) ou écrivez un texte.")

    colA, colB = st.columns(2)

    with colA:
        uploaded_doc = st.file_uploader(
            "Téléverser un document (PDF / image / texte)",
            type=["pdf", "png", "jpg", "jpeg", "txt"],
            accept_multiple_files=False,
            key="doc_uploader",
        )
        if uploaded_doc is not None:
            item = {
                "name": uploaded_doc.name,
                "type": uploaded_doc.type or "",
                "bytes": uploaded_doc.getvalue(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            st.session_state["uploaded_docs"].append(item)
            st.success("Document ajouté.")
            st.rerun()

    with colB:
        uploaded_audio = st.file_uploader(
            "Téléverser un audio (MP3 / WAV / M4A)",
            type=["mp3", "wav", "m4a"],
            accept_multiple_files=False,
            key="audio_uploader",
        )
        if uploaded_audio is not None:
            item = {
                "name": uploaded_audio.name,
                "type": uploaded_audio.type or "",
                "bytes": uploaded_audio.getvalue(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            st.session_state["uploaded_audios"].append(item)
            st.success("Audio ajouté.")
            st.rerun()

    st.divider()

    st.markdown("### Écrire un texte")
    with st.form("text_form", clear_on_submit=True):
        title = st.text_input("Titre")
        body = st.text_area("Votre texte", height=160)
        ok = st.form_submit_button("Enregistrer le texte", use_container_width=True)
        if ok:
            if not title.strip() or not body.strip():
                st.error("Titre et texte obligatoires.")
            else:
                st.session_state["saved_texts"].append(
                    {
                        "title": title.strip(),
                        "body": body.strip(),
                        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Texte enregistré.")
                st.rerun()

    st.divider()

    # Affichage documents
    st.markdown("### Vos documents")
    if not st.session_state["uploaded_docs"]:
        st.write("Aucun document pour l’instant.")
    else:
        for i, d in enumerate(reversed(st.session_state["uploaded_docs"])):
            with st.container(border=True):
                st.write(f"**{d['name']}**")
                st.caption(f"Ajouté le {d['created_at']}")

                name_lower = d["name"].lower()
                if name_lower.endswith(".pdf"):
                    st.download_button(
                        "Télécharger",
                        data=d["bytes"],
                        file_name=d["name"],
                        mime="application/pdf",
                        use_container_width=True,
                        key=f"dl_pdf_{i}",
                    )
                elif name_lower.endswith((".png", ".jpg", ".jpeg")):
                    st.image(d["bytes"])
                elif name_lower.endswith(".txt"):
                    try:
                        st.code(d["bytes"].decode("utf-8", errors="replace"))
                    except Exception:
                        st.write("Impossible d’afficher ce fichier texte.")
                else:
                    st.download_button(
                        "Télécharger",
                        data=d["bytes"],
                        file_name=d["name"],
                        mime=d["type"] or "application/octet-stream",
                        use_container_width=True,
                        key=f"dl_doc_{i}",
                    )

                if st.button("Supprimer", key=f"del_doc_{i}", use_container_width=True):
                    idx_in_list = len(st.session_state["uploaded_docs"]) - 1 - i
                    st.session_state["uploaded_docs"].pop(idx_in_list)
                    st.rerun()

    st.divider()

    # Affichage audios
    st.markdown("### Vos audios")
    if not st.session_state["uploaded_audios"]:
        st.write("Aucun audio pour l’instant.")
    else:
        for i, a in enumerate(reversed(st.session_state["uploaded_audios"])):
            with st.container(border=True):
                st.write(f"**{a['name']}**")
                st.caption(f"Ajouté le {a['created_at']}")
                st.audio(a["bytes"])

                if st.button("Supprimer", key=f"del_audio_{i}", use_container_width=True):
                    idx_in_list = len(st.session_state["uploaded_audios"]) - 1 - i
                    st.session_state["uploaded_audios"].pop(idx_in_list)
                    st.rerun()

    st.divider()

    # Affichage textes
    st.markdown("### Vos textes")
    if not st.session_state["saved_texts"]:
        st.write("Aucun texte pour l’instant.")
    else:
        for i, t in enumerate(reversed(st.session_state["saved_texts"])):
            with st.container(border=True):
                st.write(f"**{t['title']}**")
                st.caption(f"Ajouté le {t['created_at']}")
                st.write(t["body"])

                if st.button("Supprimer", key=f"del_text_{i}", use_container_width=True):
                    idx_in_list = len(st.session_state["saved_texts"]) - 1 - i
                    st.session_state["saved_texts"].pop(idx_in_list)
                    st.rerun()


# =====================================================
# ONGLET BÉNÉFICIAIRES (sans expiration)
# =====================================================
with tab_benef:
    st.subheader("Bénéficiaires")

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

        notes = st.text_area("Notes (optionnel)")
        submitted = st.form_submit_button("Ajouter le bénéficiaire", use_container_width=True)

        if submitted:
            if not last_name.strip() or not first_name.strip():
                st.error("Nom et prénom obligatoires.")
            elif "@" not in ben_email:
                st.error("Email invalide.")
            else:
                code = secrets.token_urlsafe(8).replace("-", "").replace("_", "")[:10].upper()

                st.session_state["beneficiaries"].append({
                    "Nom": last_name.strip(),
                    "Prénom": first_name.strip(),
                    "Email": ben_email.strip(),
                    "Lien": relation,
                    "Accès": access_level,
                    "Code": code,
                    "Créé le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Notes": notes.strip(),
                })

                st.success("Bénéficiaire ajouté.")
                st.rerun()

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
Code : `{b['Code']}`  
Créé le : {b['Créé le']}
"""
                    )
                    if b.get("Notes"):
                        st.caption(f"Notes : {b['Notes']}")

                with colB:
                    if st.button("Supprimer", key=f"delete_benef_{idx}", use_container_width=True):
                        st.session_state["beneficiaries"].pop(idx)
                        st.rerun()


# =====================================================
# ONGLET PARAMÈTRES (sans "démo")
# =====================================================
with tab_params:
    st.subheader("Paramètres du compte")

    st.write("Informations du compte")
    st.code(email)

    st.divider()

    st.write("Sécurité")
    st.caption("Changement de mot de passe et paramètres avancés : à connecter ensuite à Supabase Auth.")

    st.divider()

    if st.button("Se déconnecter", use_container_width=True):
        logout()
