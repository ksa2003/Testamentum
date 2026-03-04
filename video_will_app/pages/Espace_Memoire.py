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
# State init (prototype: session_state)
# -----------------------------
if "beneficiaires" not in st.session_state:
    st.session_state.beneficiaires = []  # liste de dict

if "uploads_videos" not in st.session_state:
    st.session_state.uploads_videos = []  # liste de dict

if "uploads_docs" not in st.session_state:
    st.session_state.uploads_docs = []  # liste de dict

if "abonnee_profile" not in st.session_state:
    # Profil abonné (expéditeur) : mêmes infos que bénéficiaire + identité
    st.session_state.abonnee_profile = {
        "Nom": "",
        "Prénom": "",
        "Date de naissance": "",
        "Email": st.session_state.get("user_email", ""),
        "Téléphone": "",
        "Pays": "",
        "Adresse": "",
        "Pièce (type)": "",
        "Pièce (numéro)": "",
        "Pièce (expiration)": "",
        "Notes": "",
        "Dernière mise à jour": "",
    }

# -----------------------------
# Styles
# -----------------------------
st.markdown(
    """
    <style>
      .block-container { max-width: 900px; padding-top: 1.25rem; }
      hr { margin: 1.6rem 0; }
      .kv-muted { color: rgba(0,0,0,0.6); font-size: 0.95rem; }
      .kv-card { border: 1px solid rgba(0,0,0,0.08); border-radius: 14px; padding: 14px 14px; background: #fff; }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# ============================================================
# TAB: VIDEOS (contenu réel)
# ============================================================
with tab_videos:
    st.subheader("Vidéos")
    st.markdown("<div class='kv-muted'>Déposez une vidéo, définissez le bénéficiaire, et programmez l’accès.</div>", unsafe_allow_html=True)
    st.markdown("---")

    # Choix bénéficiaire (si dispo)
    benef_labels = []
    benef_ids = []
    for b in st.session_state.beneficiaires:
        benef_ids.append(b.get("id"))
        benef_labels.append(f'{b.get("Nom","")} {b.get("Prénom","")} — {b.get("Email","")}')

    with st.form("form_upload_video", clear_on_submit=True):
        st.markdown("#### Déposer une vidéo")

        video_file = st.file_uploader(
            "Fichier vidéo",
            type=["mp4", "mov", "m4v", "avi", "mkv", "webm"],
            key="video_file_upl",
        )

        col1, col2 = st.columns(2)
        with col1:
            titre = st.text_input("Titre (optionnel)", placeholder="Ex : Message pour ma famille")
        with col2:
            categorie = st.selectbox(
                "Catégorie",
                ["Message personnel", "Dernières volontés", "Informations importantes", "Souvenir", "Autre"],
                index=0,
            )

        col3, col4 = st.columns(2)
        with col3:
            if benef_ids:
                idx = st.selectbox(
                    "Bénéficiaire destinataire",
                    list(range(len(benef_ids))),
                    format_func=lambda i: benef_labels[i],
                )
                benef_id = benef_ids[idx]
                benef_display = benef_labels[idx]
            else:
                benef_id = ""
                benef_display = ""
                st.info("Ajoutez d’abord un bénéficiaire dans l’onglet « Bénéficiaires ».")

        with col4:
            acces_mode = st.selectbox(
                "Mode d’accès",
                ["Accès immédiat", "Programmation (date/heure)", "Accès après validation (à implémenter)"],
                index=0,
            )

        schedule_dt = None
        if acces_mode == "Programmation (date/heure)":
            c5, c6 = st.columns(2)
            with c5:
                d = st.date_input("Date d’ouverture", value=date.today())
            with c6:
                t = st.time_input("Heure d’ouverture", value=datetime.now().time().replace(second=0, microsecond=0))
            schedule_dt = datetime.combine(d, t)

        st.markdown("#### Options de sécurité")
        o1, o2, o3 = st.columns(3)
        with o1:
            visionnage_unique = st.checkbox("Visionnage unique", value=False)
        with o2:
            limiter_nb = st.checkbox("Limiter nb de visionnages", value=False)
        with o3:
            nb_max = st.number_input("Nb max", min_value=1, max_value=50, value=3, disabled=not limiter_nb)

        col7, col8 = st.columns(2)
        with col7:
            expirer = st.checkbox("Date limite d’accès", value=False)
        with col8:
            date_limite = st.date_input("Date limite", value=date.today(), disabled=not expirer)

        notes = st.text_area("Notes (optionnel)", height=90, placeholder="Ex : à lire après la cérémonie, etc.")

        submitted = st.form_submit_button("Ajouter la vidéo")
        if submitted:
            if video_file is None:
                st.warning("Veuillez sélectionner un fichier vidéo.")
            elif not benef_id:
                st.warning("Veuillez choisir un bénéficiaire (ou en créer un).")
            else:
                st.session_state.uploads_videos.append(
                    {
                        "id": gen_id(),
                        "Titre": titre.strip() or video_file.name,
                        "Fichier": video_file.name,
                        "Catégorie": categorie,
                        "Bénéficiaire": benef_display,
                        "Mode d’accès": acces_mode,
                        "Programmation": schedule_dt.strftime("%Y-%m-%d %H:%M") if schedule_dt else "",
                        "Visionnage unique": "Oui" if visionnage_unique else "Non",
                        "Limite visionnages": str(int(nb_max)) if limiter_nb else "",
                        "Date limite": str(date_limite) if expirer else "",
                        "Notes": notes.strip(),
                        "Ajouté le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Vidéo ajoutée (prototype).")

    st.markdown("---")

    if st.session_state.uploads_videos:
        st.markdown("#### Vos vidéos")
        st.dataframe(
            [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.uploads_videos],
            use_container_width=True,
            hide_index=True,
        )

        with st.expander("Supprimer une vidéo", expanded=False):
            ids = [v["id"] for v in st.session_state.uploads_videos]
            labels = [f'{v["Titre"]} — {v["Bénéficiaire"]}' for v in st.session_state.uploads_videos]
            choice = st.selectbox("Choisir", list(range(len(ids))), format_func=lambda i: labels[i])
            if st.button("Supprimer la vidéo"):
                del st.session_state.uploads_videos[choice]
                st.success("Vidéo supprimée.")
                st.rerun()
    else:
        st.info("Aucune vidéo enregistrée pour le moment.")

# ============================================================
# TAB: DOCUMENTS (upload + liste)
# ============================================================
with tab_docs:
    st.subheader("Documents")
    st.markdown("<div class='kv-muted'>Déposez des documents utiles (actes, pièces d’identité, justificatifs…).</div>", unsafe_allow_html=True)
    st.markdown("---")

    with st.form("form_upload_doc", clear_on_submit=True):
        st.markdown("#### Déposer un document")
        doc_file = st.file_uploader(
            "Fichier document",
            type=["pdf", "png", "jpg", "jpeg", "doc", "docx"],
            key="doc_file_upl",
        )

        col1, col2 = st.columns(2)
        with col1:
            doc_type = st.selectbox(
                "Type de document",
                [
                    "Acte notarié / succession",
                    "Pièce d’identité",
                    "Justificatif de domicile",
                    "Livret de famille",
                    "Contrat / assurance",
                    "Autre",
                ],
                index=0,
            )
        with col2:
            doc_titre = st.text_input("Titre (optionnel)", placeholder="Ex : Carte d’identité, Acte de naissance…")

        doc_notes = st.text_area("Notes (optionnel)", height=90)

        submitted = st.form_submit_button("Ajouter le document")
        if submitted:
            if doc_file is None:
                st.warning("Veuillez sélectionner un document.")
            else:
                st.session_state.uploads_docs.append(
                    {
                        "id": gen_id(),
                        "Titre": doc_titre.strip() or doc_file.name,
                        "Fichier": doc_file.name,
                        "Type": doc_type,
                        "Notes": doc_notes.strip(),
                        "Ajouté le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Document ajouté (prototype).")

    st.markdown("---")

    if st.session_state.uploads_docs:
        st.markdown("#### Vos documents")
        st.dataframe(
            [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.uploads_docs],
            use_container_width=True,
            hide_index=True,
        )

        with st.expander("Supprimer un document", expanded=False):
            ids = [d["id"] for d in st.session_state.uploads_docs]
            labels = [f'{d["Titre"]} — {d["Type"]}' for d in st.session_state.uploads_docs]
            choice = st.selectbox("Choisir", list(range(len(ids))), format_func=lambda i: labels[i])
            if st.button("Supprimer le document"):
                del st.session_state.uploads_docs[choice]
                st.success("Document supprimé.")
                st.rerun()
    else:
        st.info("Aucun document enregistré pour le moment.")

# ============================================================
# TAB: BENEFICIAIRES
# ============================================================
with tab_benef:
    st.subheader("Bénéficiaires")
    st.markdown(
        """
Renseignez ici les informations de vos bénéficiaires.  
Ces informations servent à l’accès sécurisé et peuvent être utiles aux actes notariés.
""".strip()
    )
    st.markdown("---")

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
                st.warning("Veuillez renseigner au minimum : Nom, Prénom et Email.")
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
                st.rerun()

    st.markdown("---")

    if st.session_state.beneficiaires:
        st.markdown("#### Bénéficiaires enregistrés")
        display_rows = [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.beneficiaires]
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

# ============================================================
# TAB: PARAMETRES (infos inscription abonné)
# ============================================================
with tab_params:
    st.subheader("Paramètres")
    st.markdown("<div class='kv-muted'>Complétez les informations de l’abonné (expéditeur).</div>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### Informations de l’abonné (expéditeur)")
    st.markdown(
        """
Ces informations servent à l’inscription, à la sécurité, et peuvent être requises pour certains documents (succession / notaire).  
""".strip()
    )

    p = st.session_state.abonnee_profile

    with st.form("form_abonnee_profile"):
        col1, col2 = st.columns(2)
        with col1:
            p_nom = st.text_input("Nom", value=p.get("Nom", ""))
            p_dn = st.date_input(
                "Date de naissance",
                value=None if not p.get("Date de naissance") else date.fromisoformat(p["Date de naissance"]),
            )
            p_pays = st.text_input("Pays", value=p.get("Pays", ""))
            p_tel = st.text_input("Téléphone", value=p.get("Téléphone", ""))
        with col2:
            p_prenom = st.text_input("Prénom", value=p.get("Prénom", ""))
            # email connecté : on laisse visible mais non modifiable ici
            _ = st.text_input("Email", value=p.get("Email", st.session_state.get("user_email", "")), disabled=True)
            p_adresse = st.text_area(
                "Adresse complète",
                value=p.get("Adresse", ""),
                height=90,
                placeholder="Numéro + rue\nCode postal + ville\nPays",
            )

        st.markdown("**Pièce d’identité (optionnel / Premium)**")
        col3, col4, col5 = st.columns(3)
        with col3:
            options = ["", "Carte d'identité", "Passeport", "Titre de séjour", "Autre"]
            current = p.get("Pièce (type)", "")
            p_id_type = st.selectbox("Type de pièce", options, index=options.index(current) if current in options else 0)
        with col4:
            p_id_num = st.text_input("Numéro de pièce", value=p.get("Pièce (numéro)", ""))
        with col5:
            p_id_exp = st.date_input(
                "Date d’expiration",
                value=None if not p.get("Pièce (expiration)") else date.fromisoformat(p["Pièce (expiration)"]),
            )

        p_notes = st.text_area("Notes (optionnel)", value=p.get("Notes", ""), height=90)

        saved = st.form_submit_button("Enregistrer les informations")
        if saved:
            st.session_state.abonnee_profile = {
                "Nom": p_nom.strip(),
                "Prénom": p_prenom.strip(),
                "Date de naissance": str(p_dn) if p_dn else "",
                "Email": st.session_state.get("user_email", ""),
                "Téléphone": p_tel.strip(),
                "Pays": p_pays.strip(),
                "Adresse": p_adresse.strip(),
                "Pièce (type)": p_id_type,
                "Pièce (numéro)": p_id_num.strip(),
                "Pièce (expiration)": str(p_id_exp) if p_id_exp else "",
                "Notes": p_notes.strip(),
                "Dernière mise à jour": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
            st.success("Informations abonné enregistrées (prototype).")

# -----------------------------
# Footer navigation
# -----------------------------
st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
