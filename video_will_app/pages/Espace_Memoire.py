import streamlit as st
from theme import apply_theme

apply_theme()

# ---------------- Helpers UI ----------------
def card_open(title: str, subtitle: str = "", extra: str = ""):
    st.markdown(
        f"""
<div class="tm-card">
  <h2 style="margin:0; font-size:30px; font-weight:750;">{title}</h2>
  {f'<div class="tm-sub">{subtitle}</div>' if subtitle else ''}
  {f'<div class="tm-latin">{extra}</div>' if extra else ''}
</div>
""",
        unsafe_allow_html=True,
    )

def section_title(txt: str):
    st.markdown(f"<div style='margin-top:18px; font-size:18px; font-weight:750; color:#FFFFFF;'>{txt}</div>", unsafe_allow_html=True)

# ---------------- Security: do NOT leak infra messages ----------------
# Ici on suppose que tu stockes la session user dans st.session_state["user_email"]
# Si pas connecté, on redirige vers Connexion sans afficher de détails techniques.
if "user_email" not in st.session_state or not st.session_state["user_email"]:
    st.warning("Veuillez vous connecter pour accéder à votre espace.")
    st.page_link("pages/Connexion.py", label="Aller à Connexion")
    st.stop()

user_email = st.session_state["user_email"]

# ---------------- Header ----------------
card_open(
    "Espace Mémoire",
    "Votre espace personnel de messages et de transmission",
    f"Connecté : {user_email}",
)

st.write("")

# ---------------- Create video message ----------------
section_title("Créer un message vidéo")

titre = st.text_input("Titre du message", placeholder="Ex : Pour ma famille")

video_file = st.file_uploader(
    "Sélectionner une vidéo",
    type=["mp4", "mov", "webm", "mpeg4"],
    help="Formats : MP4, MOV, WEBM. Taille max selon la configuration.",
)

c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    televerser = st.button("Téléverser", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    gerer = st.button("Gérer les bénéficiaires", use_container_width=True)

if televerser:
    # MVP : on vérifie que c'est cohérent, sans “message vert perdu dans la page”
    if not titre.strip():
        st.error("Veuillez renseigner un titre.")
    elif video_file is None:
        st.error("Veuillez sélectionner une vidéo.")
    else:
        st.success("Téléversement (MVP) : vidéo reçue côté interface. La sauvegarde serveur sera branchée ensuite.")

st.write("")

# ---------------- Beneficiaries ----------------
section_title("Bénéficiaires")
st.caption("Ajoutez les personnes autorisées à recevoir l’accès au message lorsque la transmission sera déclenchée.")

with st.expander("Ajouter un bénéficiaire", expanded=True):
    b_name = st.text_input("Nom complet", placeholder="Ex : Marie Dupont", key="b_name")
    b_email = st.text_input("Email (optionnel)", placeholder="Ex : marie@email.com", key="b_email")
    b_rel = st.text_input("Lien (optionnel)", placeholder="Ex : sœur, ami, conjoint", key="b_rel")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    add_b = st.button("Ajouter", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# stockage MVP local (à remplacer par Supabase ensuite)
if "beneficiaires" not in st.session_state:
    st.session_state["beneficiaires"] = []

if add_b:
    if not b_name.strip():
        st.error("Le nom complet est obligatoire.")
    else:
        st.session_state["beneficiaires"].append(
            {"nom": b_name.strip(), "email": b_email.strip(), "lien": b_rel.strip()}
        )
        st.success("Bénéficiaire ajouté.")
        st.session_state["b_name"] = ""
        st.session_state["b_email"] = ""
        st.session_state["b_rel"] = ""

# liste bénéficiaires (lisible)
if len(st.session_state["beneficiaires"]) == 0:
    st.info("Aucun bénéficiaire ajouté pour l’instant. Ajoutez-en au moins un pour préparer la transmission.")
else:
    for i, b in enumerate(st.session_state["beneficiaires"], start=1):
        st.markdown(
            f"""
<div class="tm-card" style="padding:16px; margin-top:10px;">
  <div style="font-weight:750; font-size:15px; color:#FFFFFF;">{i}. {b["nom"]}</div>
  <div class="tm-sub" style="margin-top:6px;">
    {("Email : " + b["email"]) if b["email"] else "Email : —"}<br/>
    {("Lien : " + b["lien"]) if b["lien"] else "Lien : —"}
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

st.write("")

# ---------------- Messages list ----------------
section_title("Vos messages")
st.caption("Vous retrouverez ici vos messages enregistrés.")

st.info("Aucun message pour l’instant (MVP).")

st.write("")
st.write("")

# ---------------- Logout ----------------
if st.button("Se déconnecter", use_container_width=True):
    st.session_state["user_email"] = None
    st.success("Vous êtes déconnecté.")
    st.page_link("pages/Connexion.py", label="Aller à Connexion")
