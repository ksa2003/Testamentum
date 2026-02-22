import streamlit as st
from supabase import create_client, Client
from theme import apply_theme

st.set_page_config(page_title="Espace Mémoire — Testamentum", page_icon="⚖️", layout="centered")
apply_theme()

def sidebar_nav():
    st.sidebar.markdown("### Navigation")
    try:
        st.sidebar.page_link("app.py", label="Accueil")
        st.sidebar.page_link("pages/Connexion.py", label="Connexion")
        st.sidebar.page_link("pages/Tableau_de_bord.py", label="Espace Mémoire")
        st.sidebar.page_link("pages/Acces_beneficiaire.py", label="Accès bénéficiaire")
    except Exception:
        pass

sidebar_nav()

def get_supabase() -> Client:
    if "supabase_client" in st.session_state:
        return st.session_state["supabase_client"]

    if "supabase" not in st.secrets:
        st.error("Secrets manquants : ajoutez [supabase].url et [supabase].key dans les Secrets Streamlit.")
        st.stop()

    url = st.secrets["supabase"].get("url")
    key = st.secrets["supabase"].get("key")
    if not url or not key:
        st.error("Secrets incomplets : [supabase].url et [supabase].key sont requis.")
        st.stop()

    client = create_client(url, key)
    st.session_state["supabase_client"] = client
    return client

def require_auth():
    user = st.session_state.get("user")
    if not user:
        st.warning("Vous devez être connecté pour accéder à cet espace.")
        st.switch_page("pages/Connexion.py")
        st.stop()
    return user

supabase = get_supabase()
user = require_auth()

st.markdown(
    f"""
<div class="tm-card2">
  <h2 style="margin:0; font-size:34px; font-weight:800; color:rgba(255,255,255,0.93);">Espace Mémoire</h2>
  <div class="tm-p" style="margin-top:6px;">Votre espace personnel de messages et de transmission</div>
  <div class="tm-muted" style="margin-top:6px;">Connecté : {user.email}</div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ------------------ Upload vidéo (MVP sans stockage) ------------------
st.markdown('<div class="tm-videos-title">Créer un message vidéo</div>', unsafe_allow_html=True)

title = st.text_input("Titre du message", placeholder="Ex : Pour ma famille")

video = st.file_uploader(
    "Sélectionner une vidéo",
    type=["mp4", "mov", "webm", "mpeg4"],
    help="MVP : l’upload réel vers un stockage (Supabase Storage) sera ajouté ensuite.",
)

c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Téléverser", use_container_width=True):
        if not title:
            st.error("Veuillez renseigner un titre.")
        elif not video:
            st.error("Veuillez sélectionner une vidéo.")
        else:
            # MVP: on simule l'upload
            st.success("Vidéo reçue (MVP). Prochaine étape : stockage sécurisé + journalisation.")
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    if st.button("Gérer les bénéficiaires", use_container_width=True):
        st.session_state["scroll_to_beneficiaries"] = True
        st.rerun()

st.write("")

# ------------------ Bénéficiaires (CRUD) ------------------
st.markdown('<div class="tm-videos-title">Bénéficiaires</div>', unsafe_allow_html=True)
st.caption("Ajoutez les personnes autorisées à recevoir l’accès au moment prévu.")

# Lecture
try:
    beneficiaries = (
        supabase.table("beneficiaries")
        .select("*")
        .eq("owner_id", user.id)
        .order("created_at", desc=True)
        .execute()
        .data
    )
except Exception:
    beneficiaries = []
    st.error(
        "Impossible de lire la table beneficiaries. Vérifiez qu’elle existe (SQL) et que les policies RLS sont activées."
    )

with st.expander("Ajouter un bénéficiaire", expanded=True):
    bn = st.text_input("Nom complet", placeholder="Ex : Marie Dupont")
    be = st.text_input("Email (optionnel)", placeholder="Ex : marie@email.com")
    br = st.text_input("Lien (optionnel)", placeholder="Ex : sœur, ami, conjoint")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    if st.button("Ajouter", use_container_width=True):
        if not bn.strip():
            st.error("Le nom est obligatoire.")
        else:
            try:
                supabase.table("beneficiaries").insert(
                    {
                        "owner_id": user.id,
                        "full_name": bn.strip(),
                        "email": be.strip() if be.strip() else None,
                        "relationship": br.strip() if br.strip() else None,
                    }
                ).execute()
                st.success("Bénéficiaire ajouté.")
                st.rerun()
            except Exception:
                st.error("Insertion impossible. Vérifiez les policies RLS (owner_id = auth.uid()).")
    st.markdown("</div>", unsafe_allow_html=True)

if beneficiaries:
    st.markdown('<div class="tm-p" style="margin-top:6px;">Bénéficiaires enregistrés :</div>', unsafe_allow_html=True)

    for b in beneficiaries:
        cols = st.columns([6, 2], gap="medium")
        label = b.get("full_name", "—")
        rel = b.get("relationship") or ""
        em = b.get("email") or ""
        line = f"{label}"
        if rel:
            line += f" — {rel}"
        if em:
            line += f" ({em})"

        with cols[0]:
            st.write("• " + line)

        with cols[1]:
            if st.button("Supprimer", key=f"del_{b['id']}", use_container_width=True):
                try:
                    supabase.table("beneficiaries").delete().eq("id", b["id"]).eq("owner_id", user.id).execute()
                    st.success("Bénéficiaire supprimé.")
                    st.rerun()
                except Exception:
                    st.error("Suppression impossible. Vérifiez les policies RLS.")

    st.write("")
    st.info("Accès bénéficiaire : il sera disponible quand un système de jeton (token) sera activé et lié à ces bénéficiaires.")
else:
    st.info("Aucun bénéficiaire ajouté pour l’instant. Ajoutez-en au moins un pour préparer la transmission.")

# ------------------ Vos vidéos / Vos messages ------------------
st.markdown('<div class="tm-videos-title">Vos messages</div>', unsafe_allow_html=True)
st.caption("Aucun message pour l’instant (MVP).")

st.write("")
if st.button("Se déconnecter", use_container_width=True):
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    st.session_state.pop("auth_session", None)
    st.session_state.pop("user", None)
    st.success("Déconnecté.")
    st.switch_page("app.py")
