import streamlit as st
from supabase import create_client
import hashlib
from datetime import datetime, timezone

st.set_page_config(page_title="Testamentum — Accès bénéficiaire", page_icon="🎟️", layout="centered")

st.markdown(
    """
    <style>
      .stApp { background:#000; }
      section.main > div { max-width: 720px; padding-top: 1.2rem; }
      .panel{ background:#0b0f14; border:1px solid #2f3336; border-radius:16px; padding:16px; margin-bottom:12px; }
      h1,h2,h3,p,div,span,label { color:#fff !important; }
      .muted{ color:#b6bcc2 !important; }
      .stTextInput input{
        background:#0f1419 !important; border:1px solid #2f3336 !important;
        color:#fff !important; border-radius:12px !important; padding:0.75rem 0.9rem !important;
      }
      .stButton button{
        background:#E50914 !important; color:#fff !important; border:none !important;
        border-radius:12px !important; font-weight:900 !important; padding:0.75rem 1.0rem !important; width:100%;
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

def sha256(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def now_utc():
    return datetime.now(timezone.utc)

def verify_token(raw_token: str):
    token_hash = sha256(raw_token.strip())
    rows = sb.table("access_tokens").select("*").eq("token_hash", token_hash).execute().data
    if not rows:
        return None, "invalid"

    t = rows[0]
    exp = datetime.fromisoformat(t["expires_at"].replace("Z", "+00:00"))
    if now_utc() > exp:
        return None, "expired"

    video = sb.table("videos").select("*").eq("id", t["video_id"]).execute().data
    if not video:
        return None, "video_not_found"

    return video[0], "ok"

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.title("Accès bénéficiaire")
st.markdown('<div class="muted">Veuillez coller le jeton reçu pour accéder au contenu.</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

raw = st.text_input("Jeton d’accès")

if st.button("Accéder", disabled=(not raw)):
    try:
        video, status = verify_token(raw)

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
                st.success("Accès autorisé.")
                st.video(signed["signedURL"])
    except Exception as e:
        st.error("Erreur lors de l’accès.")
        st.caption(str(e)[:200])

st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
if st.button("Retour à l’accueil"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)
