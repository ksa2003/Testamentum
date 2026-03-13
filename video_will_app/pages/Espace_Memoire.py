import streamlit as st
from datetime import datetime, date
import secrets

st.set_page_config(page_title="Coffre Kidanmemoris", layout="centered")

BLUE_MAIN = "#0A66C2"

if "user_email" not in st.session_state:
    st.warning("Vous devez être connecté pour accéder à cet espace.")
    st.switch_page("pages/Connexion.py")
    st.stop()

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

if "beneficiaires" not in st.session_state:
    st.session_state.beneficiaires = []

if "uploads_videos" not in st.session_state:
    st.session_state.uploads_videos = []

if "uploads_docs" not in st.session_state:
    st.session_state.uploads_docs = []

if "family_tree" not in st.session_state:
    st.session_state.family_tree = []

if "abonnee_profile" not in st.session_state:
    st.session_state.abonnee_profile = {
        "Nom": st.session_state.get("user_name", ""),
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

st.markdown(
    f"""
    <style>
      .block-container {{ max-width: 980px; padding-top: 1.25rem; }}
      hr {{ margin: 1.6rem 0; }}
      a.anchor-link {{ display:none !important; }}
      .kv-muted {{ color: rgba(0,0,0,0.68); font-size: 0.95rem; }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Coffre Kidanmemoris")
st.caption(f"Connecté en tant que : {mask_email(st.session_state.get('user_email', ''))}")

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

tab_videos, tab_docs, tab_benef, tab_tree, tab_params, tab_succession = st.tabs(
    ["Mes vidéos", "Souvenirs & lettres", "Destinataires", "Arbre familial", "Paramètres", "Préparer ma succession"]
)

with tab_videos:
    st.subheader("Mes vidéos")
    st.markdown("<div class='kv-muted'>Messages vidéo, programmés pour des moments de vie ou après confirmation.</div>", unsafe_allow_html=True)

    with st.form("form_upload_video", clear_on_submit=True):
        video_file = st.file_uploader("Vidéo", type=["mp4", "mov", "m4v", "avi", "mkv", "webm"], key="video_file_upl")
        col1, col2 = st.columns(2)
        with col1:
            titre = st.text_input("Titre", placeholder="Ex : Pour mes enfants")
        with col2:
            moment = st.selectbox(
                "Moment de vie",
                ["Après décès", "Mariage", "Naissance", "Baptême", "18 ans", "Anniversaire important", "Réussite scolaire", "Message familial", "Autre"]
            )

        transmission = st.selectbox("Transmission", ["Après confirmation de décès", "Date programmée", "Événement spécifique"])
        visionnage = st.selectbox("Visionnage", ["Visionnage unique", "Accès pendant 7 jours", "Accès permanent"])
        notes = st.text_area("Notes")
        submitted = st.form_submit_button("Ajouter la vidéo")

        if submitted:
            if video_file is None:
                st.warning("Veuillez sélectionner une vidéo.")
            else:
                st.session_state.uploads_videos.append(
                    {
                        "id": gen_id(),
                        "Titre": titre.strip() or video_file.name,
                        "Fichier": video_file.name,
                        "Moment de vie": moment,
                        "Transmission": transmission,
                        "Visionnage": visionnage,
                        "Notes": notes.strip(),
                        "Ajouté le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Vidéo ajoutée.")

    st.markdown("---")
    if st.session_state.uploads_videos:
        st.dataframe(
            [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.uploads_videos],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Aucune vidéo enregistrée pour le moment.")

with tab_docs:
    st.subheader("Souvenirs & lettres numériques")
    st.markdown("<div class='kv-muted'>Le coffre du patrimoine émotionnel ne contient pas seulement des vidéos.</div>", unsafe_allow_html=True)

    with st.form("form_upload_doc", clear_on_submit=True):
        doc_file = st.file_uploader("Document", type=["pdf", "png", "jpg", "jpeg", "doc", "docx"], key="doc_file_upl")
        col1, col2 = st.columns(2)
        with col1:
            doc_type = st.selectbox(
                "Type",
                ["Lettre numérique", "Souvenir familial", "Document patrimonial", "Pièce d’identité", "Acte / succession", "Autre"]
            )
        with col2:
            doc_titre = st.text_input("Titre", placeholder="Ex : Lettre pour plus tard")

        doc_notes = st.text_area("Notes")
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
                st.success("Document ajouté.")

    st.markdown("---")
    if st.session_state.uploads_docs:
        st.dataframe(
            [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.uploads_docs],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Aucun souvenir ou document enregistré.")

with tab_benef:
    st.subheader("Destinataires")
    st.markdown("<div class='kv-muted'>1 destinataire, plusieurs destinataires ou destinataire collectif (famille).</div>", unsafe_allow_html=True)

    with st.form("form_add_benef", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nom = st.text_input("Nom")
            tel = st.text_input("Téléphone")
            mode = st.selectbox("Type", ["1 destinataire", "Plusieurs destinataires", "Destinataire collectif (famille)"])
        with c2:
            prenom = st.text_input("Prénom")
            email = st.text_input("Email")
            lien = st.selectbox("Lien", ["Enfant", "Partenaire", "Parent", "Famille", "Ami", "Autre"])

        submitted = st.form_submit_button("Ajouter le destinataire")
        if submitted:
            if not nom or not email:
                st.warning("Veuillez renseigner au minimum le nom et l’email.")
            else:
                st.session_state.beneficiaires.append(
                    {
                        "id": gen_id(),
                        "Nom": nom.strip(),
                        "Prénom": prenom.strip(),
                        "Email": email.strip(),
                        "Téléphone": tel.strip(),
                        "Lien": lien,
                        "Type": mode,
                        "Créé le": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    }
                )
                st.success("Destinataire ajouté.")

    st.markdown("---")
    if st.session_state.beneficiaires:
        st.dataframe(
            [{k: v for k, v in row.items() if k != "id"} for row in st.session_state.beneficiaires],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Aucun destinataire enregistré.")

with tab_tree:
    st.subheader("Arbre de mémoire familiale")
    st.markdown("<div class='kv-muted'>Chaque famille peut créer un arbre familial et des messages pour chaque génération.</div>", unsafe_allow_html=True)

    with st.form("family_tree_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            membre = st.text_input("Nom du membre")
            relation = st.text_input("Relation")
        with c2:
            generation = st.selectbox("Génération", ["Grand-parents", "Parents", "Enfants", "Petits-enfants", "Autre"])
            note = st.text_input("Note courte")

        submitted = st.form_submit_button("Ajouter à l’arbre")
        if submitted:
            if not membre:
                st.warning("Veuillez renseigner un nom.")
            else:
                st.session_state.family_tree.append(
                    {
                        "Nom": membre.strip(),
                        "Relation": relation.strip(),
                        "Génération": generation,
                        "Note": note.strip(),
                    }
                )
                st.success("Membre ajouté à l’arbre familial.")

    st.markdown("---")
    if st.session_state.family_tree:
        st.dataframe(st.session_state.family_tree, use_container_width=True, hide_index=True)
    else:
        st.info("Aucun membre ajouté pour le moment.")

with tab_params:
    st.subheader("Paramètres")
    st.write("Identité, sécurité du coffre, contact de confiance et règles de transmission.")

with tab_succession:
    st.subheader("Préparer ma succession")
    st.markdown(
        """
- contacter un notaire partenaire  
- associer une vidéo à un testament  
- créer un dossier patrimonial  
"""
    )
    st.info("Concept : patrimoine numérique émotionnel et juridique.")

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
