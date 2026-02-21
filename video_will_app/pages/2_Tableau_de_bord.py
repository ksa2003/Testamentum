import streamlit as st
from supabase import create_client
import uuid
import hashlib
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="Testamentum — Tableau de bord", page_icon="🎬", layout="centered")

st.markdown(
    """
    <style>
      .stApp { background:#000; }
      section.main > div { max-width: 820px; padding-top: 1.2rem; }
      .panel{ background:#0b0f14; border:1px solid #2f3336; border-radius:16px; padding:16px; margin-bottom:12px; }
      h1,h2,h3,p,div,span,label { color:#fff !important; }
      .muted{ color:#b6bcc2 !important; }
      .stTextInput input, .stTextArea textarea{
        background:#0f1419 !important; border:1px solid #2f3336 !important;
        color:#fff !important; border-radius:12px !important; padding:0.75rem 0.9rem !important;
      }
      [data-testid="stFileUploader"]{ background:#0f1419; border:1px dashed #2f3336; border-radius:12px; padding:10px; }
      .stButton button{
        background:#E50914 !important; color:#fff !important; border:none !important;
        border-radius:12px !important; font-weight:900 !important; padding:0.75rem 1.0rem !important;
      }
      .btn-secondary .stButton button{
        background:transparent !important; border:1px solid #2f3336 !important; color:#fff !important;
      }
      #MainMenu {visibility:hidden;} footer{visibility:hidden;} header{visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

def now_utc():
    return datetime.now(timezone.utc)

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def require_auth():
    if "user_id" not in st.session_state:
        st.switch_page("pages/1_Connexion.py")

def get_or_create_vault(owner_user_id: str):
    res = sb.table("vaults").select("*").eq("owner_user_id", owner_user_id).execute()
    if res.data:
        return res.data[0]
    created = sb.table("vaults").insert({"owner_user_id": owner_user_id, "title": "Coffre principal"}).execute()
    return created.data[0]

def create_access_token(video_id: str, beneficiary_email: str, days_valid: int = 7) -> str:
    raw = uuid.uuid4().hex + uuid.uuid4().hex
    token_hash = sha256(raw)
    expires = now_utc() + timedelta(days=days_valid)
    sb.table("access_tokens").insert({
        "video_id": video_id,
        "beneficiary_email": beneficiary_email,
        "token_hash": token_hash,
        "expires_at": expires.isoformat()
    }).execute()
    return raw

require_auth()
user_id = st.session_state["user_id"]
user_email = st.session_state.get("user_email", "")
vault = get_or_create_vault(user_id)

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.title("Tableau de bord")
st.markdown(f'<div class="muted">Connecté : {user_email}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
if st.button("Se déconnecter"):
    try:
        sb.auth.sign_out()
    except Exception:
        pass
    st.session_state.clear()
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Téléverser", "Bénéficiaires & jetons"])

with tab1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Téléverser une vidéo")
    title = st.text_input("Titre", value="Mon message")
    file = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "m4v", "webm"])

    if st.button("Téléverser", disabled=(file is None)):
        try:
            object_key = f"{vault['id']}/{uuid.uuid4().hex}_{file.name}"
            bucket = sb.storage.from_("video-wills")
            bucket.upload(object_key, file.getvalue(), {"content-type": file.type or "video/mp4"})

            sb.table("videos").insert({
                "vault_id": vault["id"],
                "title": title,
                "storage_path": object_key,
                "released": False
            }).execute()
            st.success("Vidéo téléversée avec succès.")
        except Exception as e:
            st.error("Impossible de téléverser la vidéo.")
            st.caption(str(e)[:200])

    st.markdown("### Vos vidéos")
    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if not vids:
        st.info("Aucune vidéo pour l’instant.")
    else:
        for v in vids:
            st.write(f"- {v.get('title','(sans titre)')} • libérée : {v.get('released')}")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Bénéficiaires")
    ben_email = st.text_input("Adresse e-mail du bénéficiaire")

    if st.button("Ajouter un bénéficiaire", disabled=(not ben_email)):
        try:
            sb.table("beneficiaries").insert({"vault_id": vault["id"], "email": ben_email}).execute()
            st.success("Bénéficiaire ajouté.")
        except Exception as e:
            st.error("Impossible d’ajouter ce bénéficiaire (déjà présent ou erreur).")
            st.caption(str(e)[:200])

    bens = sb.table("beneficiaries").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if bens:
        st.markdown("### Liste")
        for b in bens:
            st.write(f"- {b['email']}")
    else:
        st.info("Aucun bénéficiaire pour l’instant.")

    st.markdown("---")
    st.subheader("Générer un jeton (MVP)")
    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data

    if vids and bens:
        video_choice = st.selectbox("Sélectionner une vidéo", vids, format_func=lambda x: x.get("title", "(sans titre)"))
        ben_choice = st.selectbox("Sélectionner un bénéficiaire", bens, format_func=lambda x: x["email"])

        if st.button("Générer le jeton (7 jours)"):
            try:
                sb.table("videos").update({"released": True, "released_at": now_utc().isoformat()}).eq("id", video_choice["id"]).execute()
                token = create_access_token(video_choice["id"], ben_choice["email"], 7)
                st.success("Jeton généré :")
                st.code(token)
                st.markdown('<div class="muted">Transmettez ce jeton au bénéficiaire.</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("Impossible de générer le jeton.")
                st.caption(str(e)[:200])
    else:
        st.info("Ajoutez au moins une vidéo et un bénéficiaire.")
    st.markdown("</div>", unsafe_allow_html=True)
