import streamlit as st
from supabase import create_client
import uuid
import hashlib
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------
st.set_page_config(page_title="Testamentum", page_icon="🔐", layout="centered")

# ---------------------------------------------------
# THEME sombre lisible (style X, mais avec contraste fort)
# ---------------------------------------------------
st.markdown(
    """
    <style>
      :root{
        --bg: #000000;
        --surface: #0b0f14;     /* légèrement plus clair que le fond */
        --border: #2f3336;
        --text: #ffffff;
        --muted: #b6bcc2;       /* gris clair (lisible) */
        --muted2:#8b98a5;
        --accent:#1d9bf0;
        --input:#0f1419;        /* fond champs */
      }

      /* Fond global */
      .stApp{ background: var(--bg) !important; }

      /* Texte par défaut */
      html, body, [class*="css"]{
        color: var(--text) !important;
        font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Noto Sans", "Liberation Sans", sans-serif;
      }

      /* Container */
      section.main > div{
        max-width: 760px;
        padding-top: 1.0rem;
      }

      /* Enlever la carte blanche Streamlit */
      .block-container{
        background: transparent !important;
        padding: 12px 14px 18px 14px !important;
      }

      /* Panels */
      .panel{
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 14px;
        margin-bottom: 12px;
      }

      /* Titres */
      h1, h2, h3{
        color: var(--text) !important;
        letter-spacing: -0.01em;
      }

      /* Muted text */
      .muted{ color: var(--muted) !important; font-size: 0.98rem; }
      .muted2{ color: var(--muted2) !important; font-size: 0.92rem; }

      /* Labels des inputs (Streamlit) */
      label, .stTextInput label, .stTextArea label, .stFileUploader label{
        color: var(--muted) !important;
        font-weight: 600 !important;
      }

      /* Inputs */
      .stTextInput input, .stTextArea textarea{
        background: var(--input) !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        border-radius: 14px !important;
        padding: 0.65rem 0.85rem !important;
      }
      .stTextInput input:focus, .stTextArea textarea:focus{
        border: 1px solid var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(29,155,240,0.20) !important;
        outline: none !important;
      }

      /* File uploader */
      [data-testid="stFileUploader"]{
        background: var(--input) !important;
        border: 1px dashed var(--border) !important;
        border-radius: 14px !important;
        padding: 10px !important;
      }
      [data-testid="stFileUploader"] *{
        color: var(--muted) !important;
      }

      /* Tabs */
      button[role="tab"]{
        border-radius: 999px !important;
        border: 1px solid var(--border) !important;
        background: transparent !important;
        color: var(--muted) !important;
        padding: 6px 12px !important;
        margin-right: 6px !important;
        font-weight: 700 !important;
      }
      button[role="tab"][aria-selected="true"]{
        color: var(--text) !important;
        border: 1px solid var(--accent) !important;
        box-shadow: 0 0 0 3px rgba(29,155,240,0.15) !important;
      }

      /* Buttons */
      .stButton button{
        border-radius: 999px !important;
        padding: 0.60rem 1.10rem !important;
        border: 1px solid var(--border) !important;
        background: var(--text) !important;
        color: #0f1419 !important;
        font-weight: 800 !important;
      }
      .stButton button:hover{
        background: #e6e6e6 !important;
      }

      /* Secondary buttons (class wrapper) */
      .btn-secondary .stButton button{
        background: transparent !important;
        color: var(--text) !important;
        border: 1px solid var(--border) !important;
        font-weight: 700 !important;
      }
      .btn-secondary .stButton button:hover{
        background: rgba(255,255,255,0.06) !important;
      }

      /* Alerts */
      .stAlert{
        border-radius: 14px !important;
        border: 1px solid var(--border) !important;
        background: rgba(255,255,255,0.04) !important;
        color: var(--text) !important;
      }
      .stAlert *{ color: var(--text) !important; }

      /* Sidebar */
      section[data-testid="stSidebar"] > div{
        background: var(--bg) !important;
        border-right: 1px solid var(--border);
      }
      section[data-testid="stSidebar"] *{
        color: var(--text) !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# Supabase client
# ---------------------------------------------------
sb = create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])

# ---------------------------------------------------
# Helpers
# ---------------------------------------------------
def now_utc():
    return datetime.now(timezone.utc)

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ---------------------------------------------------
# DB functions
# ---------------------------------------------------
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

def verify_access_token(raw_token: str):
    token_hash = sha256(raw_token.strip())
    rows = sb.table("access_tokens").select("*").eq("token_hash", token_hash).execute().data
    if not rows:
        return None, "invalid"

    t = rows[0]
    exp = datetime.fromisoformat(t["expires_at"].replace("Z", "+00:00"))
    if now_utc() > exp:
        return None, "expired"

    v_rows = sb.table("videos").select("*").eq("id", t["video_id"]).execute().data
    if not v_rows:
        return None, "video_not_found"

    return v_rows[0], "ok"

# ---------------------------------------------------
# Header (lisible)
# ---------------------------------------------------
st.markdown(
    """
    <div class="panel">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:12px;">
        <div>
          <div style="font-size:1.25rem; font-weight:900; line-height:1.2;">Testamentum</div>
          <div class="muted">Coffre vidéo sécurisé — accès contrôlé pour les bénéficiaires</div>
        </div>
        <div class="muted2" style="font-weight:800;">MVP</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# Auth
# ---------------------------------------------------
if "user_id" not in st.session_state:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.header("Accès")
    st.markdown('<div class="muted">Veuillez créer un compte ou vous connecter.</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Créer un compte")
        email_reg = st.text_input("Adresse email", key="reg_email")
        password_reg = st.text_input("Mot de passe", type="password", key="reg_pass")
        if st.button("Créer mon compte"):
            try:
                sb.auth.sign_up({"email": email_reg, "password": password_reg})
                st.success("Compte créé avec succès. Vous pouvez maintenant vous connecter.")
            except Exception as e:
                st.error("Impossible de créer le compte.")
                st.caption(str(e)[:200])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("Connexion")
        email = st.text_input("Adresse email", key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")
        if st.button("Se connecter"):
            try:
                auth = sb.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state["user_id"] = auth.user.id
                st.session_state["user_email"] = auth.user.email
                st.rerun()
            except Exception as e:
                st.error("Identifiants invalides ou compte non confirmé.")
                st.caption(str(e)[:200])
        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# ---------------------------------------------------
# Connected + Logout
# ---------------------------------------------------
st.markdown(
    f"""
    <div class="panel">
      <div style="display:flex; align-items:center; justify-content:space-between;">
        <div>
          <div style="font-weight:900; font-size:1.05rem;">Tableau de bord</div>
          <div class="muted2">Connecté : {st.session_state['user_email']}</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
if st.button("Se déconnecter"):
    try:
        sb.auth.sign_out()
    except Exception:
        pass
    st.session_state.clear()
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

user_id = st.session_state["user_id"]
vault = get_or_create_vault(user_id)

tabs = st.tabs(["Téléversement", "Bénéficiaires", "Accès par jeton"])
tab1, tab2, tab3 = tabs

# ---------------------------------------------------
# Tab 1 - Upload
# ---------------------------------------------------
with tab1:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Téléverser une vidéo")
    st.markdown('<div class="muted2">Ajoutez un message vidéo à votre coffre.</div>', unsafe_allow_html=True)
    st.write("")

    title = st.text_input("Titre", value="Mon message", key="vid_title")
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
            st.write(f"- {v.get('title','(sans titre)')}  •  libérée : {v.get('released')}")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Tab 2 - Beneficiaries + Token generation (MVP)
# ---------------------------------------------------
with tab2:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Bénéficiaires")
    st.markdown('<div class="muted2">Ajoutez vos proches puis générez un jeton d’accès.</div>', unsafe_allow_html=True)
    st.write("")

    ben_email = st.text_input("Adresse email du bénéficiaire", key="ben_email")

    st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
    if st.button("Ajouter un bénéficiaire", disabled=(not ben_email)):
        try:
            sb.table("beneficiaries").insert({"vault_id": vault["id"], "email": ben_email}).execute()
            st.success("Bénéficiaire ajouté.")
        except Exception as e:
            st.error("Impossible d’ajouter ce bénéficiaire (déjà présent ou erreur).")
            st.caption(str(e)[:200])
    st.markdown("</div>", unsafe_allow_html=True)

    bens = sb.table("beneficiaries").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if bens:
        st.markdown("### Liste")
        for b in bens:
            st.write(f"- {b['email']}")
    else:
        st.info("Aucun bénéficiaire pour l’instant.")

    st.markdown("---")
    st.subheader("Jeton d’accès")
    st.markdown('<div class="muted2">Ce jeton est valable 7 jours (MVP).</div>', unsafe_allow_html=True)
    st.write("")

    vids = sb.table("videos").select("*").eq("vault_id", vault["id"]).order("created_at", desc=True).execute().data
    if not vids or not bens:
        st.info("Veuillez d’abord ajouter au moins une vidéo et un bénéficiaire.")
    else:
        video_choice = st.selectbox("Sélectionner une vidéo", vids, format_func=lambda x: x.get("title", "(sans titre)"))
        ben_choice = st.selectbox("Sélectionner un bénéficiaire", bens, format_func=lambda x: x["email"])

        if st.button("Générer le jeton"):
            try:
                sb.table("videos").update({"released": True, "released_at": now_utc().isoformat()}).eq("id", video_choice["id"]).execute()
                token = create_access_token(video_choice["id"], ben_choice["email"], days_valid=7)
                st.success("Jeton généré. Veuillez le transmettre au bénéficiaire :")
                st.code(token)
            except Exception as e:
                st.error("Impossible de générer le jeton.")
                st.caption(str(e)[:200])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Tab 3 - Token access
# ---------------------------------------------------
with tab3:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.subheader("Accès bénéficiaire")
    st.markdown('<div class="muted2">Collez le jeton reçu pour accéder au contenu.</div>', unsafe_allow_html=True)
    st.write("")

    raw_token = st.text_input("Jeton d’accès", key="access_token")

    if st.button("Accéder", disabled=(not raw_token)):
        try:
            video, status = verify_access_token(raw_token)

            if status == "invalid":
                st.error("Jeton invalide.")
            elif status == "expired":
                st.error("Jeton expiré.")
            elif status != "ok":
                st.error("Impossible de retrouver la vidéo.")
            else:
                if not video.get("released"):
                    st.error("Contenu non libéré.")
                else:
                    bucket = sb.storage.from_("video-wills")
                    signed = bucket.create_signed_url(video["storage_path"], 3600)
                    st.success("Accès autorisé. Lecture en cours.")
                    st.video(signed["signedURL"])
        except Exception as e:
            st.error("Erreur lors de l’accès.")
            st.caption(str(e)[:200])

    st.markdown("</div>", unsafe_allow_html=True)
