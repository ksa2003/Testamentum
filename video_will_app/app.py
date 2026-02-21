import streamlit as st
from supabase import create_client
import uuid
from datetime import datetime, timedelta

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Testamentum",
    page_icon="⚖️",
    layout="centered",
)

# =========================================================
# THEME (X / LegalTech) – 2 MODES
# =========================================================
THEME_MODE = st.sidebar.selectbox(
    "Thème",
    ["card X (blur)", "flat (noir)"],
    index=0,
)

IS_CARD = THEME_MODE.startswith("card")

BG = "#000000" if not IS_CARD else "#000000"
CARD_BG = "rgba(15, 20, 25, 0.70)" if IS_CARD else "rgba(0,0,0,0)"
CARD_BORDER = "rgba(255,255,255,0.08)" if IS_CARD else "rgba(255,255,255,0.06)"
CARD_SHADOW = "0 18px 60px rgba(0,0,0,0.55)" if IS_CARD else "none"
CARD_BLUR = "blur(12px)" if IS_CARD else "none"

# Accent “deuil / légal” : gris argent froid (pas de bleu / pas de rouge)
ACCENT = "#C7CBD1"
ACCENT_2 = "#9AA4B2"
TEXT = "#E7E9EA"
MUTED = "#AAB2BD"
MUTED_2 = "#76808F"

st.markdown(
    f"""
<style>
/* ---- Global base ---- */
:root {{
  --bg: {BG};
  --card: {CARD_BG};
  --cardBorder: {CARD_BORDER};
  --cardShadow: {CARD_SHADOW};
  --accent: {ACCENT};
  --accent2: {ACCENT_2};
  --text: {TEXT};
  --muted: {MUTED};
  --muted2: {MUTED_2};
}}

html, body, [class*="css"] {{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}}

.stApp {{
  background: var(--bg) !important;
}}

/* Container */
section.main > div {{
  max-width: 980px;
  padding-top: 2rem;
}}

.block-container {{
  padding-top: 2rem;
}}

/* ---- Hero Card ---- */
.tm-hero {{
  background: var(--card);
  border: 1px solid var(--cardBorder);
  border-radius: 18px;
  padding: 22px 22px 18px 22px;
  box-shadow: var(--cardShadow);
  backdrop-filter: {CARD_BLUR};
  -webkit-backdrop-filter: {CARD_BLUR};
  animation: tmFadeIn 420ms ease-out;
}}

@keyframes tmFadeIn {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to   {{ opacity: 1; transform: translateY(0px); }}
}}

.tm-brand {{
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-bottom: 10px;
}}

.tm-title {{
  font-size: 44px;
  line-height: 1.05;
  margin: 0;
  letter-spacing: -0.02em;
  font-weight: 750;
  background: linear-gradient(90deg, #ffffff, var(--accent));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}

.tm-tagline {{
  margin: 4px 0 0 0;
  color: var(--muted2);
  font-size: 13px;
  font-style: italic;
}}

.tm-sub {{
  margin-top: 6px;
  color: var(--muted);
  font-size: 13px;
}}

.tm-h2 {{
  margin: 14px 0 6px 0;
  font-size: 26px;
  letter-spacing: -0.01em;
}}

.tm-p {{
  color: var(--muted);
  margin: 0 0 10px 0;
  line-height: 1.55;
}}

.tm-bullets {{
  margin: 10px 0 0 0;
  color: var(--muted);
  line-height: 1.7;
}}

.tm-chiprow {{
  display:flex;
  gap:8px;
  flex-wrap:wrap;
  margin-top:10px;
}}

.tm-chip {{
  border: 1px solid rgba(255,255,255,0.10);
  color: var(--muted);
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 12px;
  background: rgba(255,255,255,0.02);
}}

.tm-section {{
  margin-top: 20px;
  padding: 18px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  background: rgba(255,255,255,0.02);
  animation: tmFadeIn 420ms ease-out;
}}

/* ---- Streamlit widgets: remove red focus, keep theme ---- */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {{
  background: linear-gradient(180deg, rgba(15,20,25,0.98), rgba(11,15,20,0.98)) !important;
  border: 1px solid rgba(255,255,255,0.10) !important;
  color: var(--text) !important;
  caret-color: var(--text) !important;
  border-radius: 14px !important;
}}

.stTextInput input:focus,
.stTextArea textarea:focus {{
  outline: none !important;
  border: 1px solid rgba(199,203,209,0.85) !important;
  box-shadow: 0 0 0 2px rgba(199,203,209,0.15) !important;
}}

input:invalid {{
  box-shadow: none !important;
  border: 1px solid rgba(255,255,255,0.10) !important;
}}

.stTextInput div[data-baseweb="input"] {{
  border: none !important;
}}
.stTextInput div[data-baseweb="input"] > div {{
  border: none !important;
}}

/* Buttons */
.stButton button {{
  background: rgba(199,203,209,0.14) !important;
  color: var(--text) !important;
  border: 1px solid rgba(199,203,209,0.30) !important;
  border-radius: 999px !important;
  padding: 0.70rem 1.05rem !important;
  transition: all .15s ease !important;
}}

.stButton button:hover {{
  background: rgba(199,203,209,0.22) !important;
  border-color: rgba(199,203,209,0.45) !important;
}}

.tm-primary button {{
  width: 100%;
  background: rgba(199,203,209,0.18) !important;
  border: 1px solid rgba(199,203,209,0.40) !important;
}}

.tm-muted {{
  color: var(--muted2);
  font-size: 12px;
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
  gap: 8px;
}}
.stTabs [data-baseweb="tab"] {{
  border-radius: 999px;
  padding: 8px 12px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.07);
  color: var(--muted) !important;
}}
.stTabs [aria-selected="true"] {{
  background: rgba(199,203,209,0.10);
  border-color: rgba(199,203,209,0.30);
  color: var(--text) !important;
}}

/* Hide Streamlit default header */
header {{ visibility: hidden; }}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# SUPABASE
# =========================================================
sb = create_client(
    st.secrets["supabase"]["url"],
    st.secrets["supabase"]["key"],
)

# =========================================================
# HELPERS
# =========================================================
def now_utc():
    return datetime.utcnow()

def iso(dt: datetime):
    return dt.replace(microsecond=0).isoformat()

def get_user():
    return st.session_state.get("user")

def set_user(user):
    st.session_state["user"] = user

def logout():
    # Streamlit-only session logout (Supabase has no server-side session here)
    for k in ["user", "page"]:
        if k in st.session_state:
            del st.session_state[k]
    st.success("Vous avez été déconnecté.")
    st.rerun()

def nav_to(page_name: str):
    st.session_state["page"] = page_name
    st.rerun()

def current_page():
    return st.session_state.get("page", "Accueil")

def ensure_tables_ready_hint():
    st.info(
        "MVP : certaines fonctionnalités supposent que vos tables Supabase existent déjà "
        "(vaults, videos, beneficiaries, access_tokens)."
    )

# -----------------------------
# DB actions
# -----------------------------
def get_or_create_vault(owner_user_id: str):
    existing = sb.table("vaults").select("*").eq("owner_user_id", owner_user_id).execute()
    if existing.data:
        return existing.data[0]

    created = sb.table("vaults").insert({
        "owner_user_id": owner_user_id,
        "title": "Coffre principal",
    }).execute()
    return created.data[0]

def list_videos(vault_id: str):
    res = sb.table("videos").select("*").eq("vault_id", vault_id).order("created_at", desc=True).execute()
    return res.data or []

def create_access_token(vault_id: str, beneficiary_email: str, days_valid: int = 7):
    token = str(uuid.uuid4())
    expires_at = iso(now_utc() + timedelta(days=days_valid))
    sb.table("access_tokens").insert({
        "vault_id": vault_id,
        "token": token,
        "beneficiary_email": beneficiary_email,
        "expires_at": expires_at
    }).execute()
    return token, expires_at

def verify_token(token: str):
    res = sb.table("access_tokens").select("*").eq("token", token).execute()
    if not res.data:
        return None
    row = res.data[0]
    # Expiration check
    if row.get("expires_at"):
        try:
            exp = datetime.fromisoformat(row["expires_at"].replace("Z", "+00:00")).replace(tzinfo=None)
        except Exception:
            exp = datetime.fromisoformat(row["expires_at"].split("+")[0])
        if now_utc() > exp:
            return "expired"
    return row

# =========================================================
# UI – HERO
# =========================================================
def render_hero():
    st.markdown(
        """
<div class="tm-hero">
  <div class="tm-brand">
    <h1 class="tm-title">Testamentum</h1>
  </div>
  <div class="tm-sub">Coffre numérique sécurisé pour transmission vidéo posthume</div>
  <div class="tm-tagline">Verba manent. Memoria custoditur.</div>

  <div class="tm-chiprow">
    <span class="tm-chip">LegalTech</span>
    <span class="tm-chip">Confidentialité</span>
    <span class="tm-chip">Traçabilité</span>
    <span class="tm-chip">Accès contrôlé</span>
  </div>

  <h2 class="tm-h2">Un message vidéo, transmis au bon moment.</h2>
  <p class="tm-p">
    Enregistrez un message destiné à vos proches, puis contrôlez précisément l’accès des bénéficiaires
    lorsque le décès est déclaré. Le service est conçu pour une transmission respectueuse, avec des règles strictes
    (jeton, expiration, journalisation).
  </p>

  <div class="tm-bullets">
    • Accès bénéficiaires par jeton temporaire sécurisé<br/>
    • Validation notariale (workflow métier, selon juridiction)<br/>
    • Journalisation des actions pour la traçabilité (MVP)
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

# =========================================================
# PAGES
# =========================================================
def page_home():
    render_hero()

    st.markdown('<div class="tm-section">', unsafe_allow_html=True)
    st.subheader("Commencer")
    st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")
    email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
        if st.button("Continuer"):
            # On pré-remplit l'email sur la page Connexion
            st.session_state["prefill_email"] = (email or "").strip()
            nav_to("Connexion")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        if st.button("Accès bénéficiaire"):
            nav_to("Accès bénéficiaire")

    st.markdown(
        '<div class="tm-muted">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def page_auth():
    st.subheader("Connexion")
    st.caption("Veuillez vous identifier pour accéder à votre coffre.")

    tabs = st.tabs(["Se connecter", "Créer un compte"])

    prefill = st.session_state.get("prefill_email", "")

    with tabs[0]:
        email = st.text_input("Adresse e-mail", value=prefill, key="login_email")
        password = st.text_input("Mot de passe", type="password", key="login_pass")

        if st.button("Se connecter"):
            try:
                res = sb.auth.sign_in_with_password({"email": email.strip(), "password": password})
                if res.user:
                    set_user({"id": res.user.id, "email": res.user.email})
                    st.success("Connecté.")
                    nav_to("Tableau de bord")
                else:
                    st.error("Connexion impossible. Vérifiez vos identifiants.")
            except Exception:
                st.error("Connexion impossible. Vérifiez vos identifiants et la configuration Supabase.")

        if st.button("Retour à l’accueil"):
            nav_to("Accueil")

    with tabs[1]:
        email = st.text_input("Adresse e-mail", value=prefill, key="reg_email")
        password = st.text_input("Mot de passe", type="password", key="reg_pass")

        st.caption("Conseil : utilisez un mot de passe unique et robuste.")

        if st.button("Créer mon compte"):
            try:
                res = sb.auth.sign_up({"email": email.strip(), "password": password})
                if res.user:
                    st.success("Compte créé. Vous pouvez maintenant vous connecter.")
                else:
                    st.error("Création impossible. Réessayez.")
            except Exception:
                st.error("Création impossible. Vérifiez l’e-mail ou essayez un autre mot de passe.")


def page_dashboard():
    u = get_user()
    if not u:
        nav_to("Connexion")
        return

    st.subheader("Tableau de bord")
    st.caption(f"Connecté : {u['email']}")

    c1, c2 = st.columns([1, 2])
    with c1:
        if st.button("Se déconnecter"):
            logout()
    with c2:
        st.write("")

    ensure_tables_ready_hint()

    vault = get_or_create_vault(u["id"])

    tab1, tab2 = st.tabs(["Téléverser", "Bénéficiaires & jetons"])

    with tab1:
        st.markdown('<div class="tm-section">', unsafe_allow_html=True)
        st.markdown("### Téléverser une vidéo")
        title = st.text_input("Titre", value="Mon message")

        file = st.file_uploader(
            "Sélectionner un fichier",
            type=["mp4", "mov", "m4v", "webm"],
            help="MVP : le stockage final dépend de votre configuration (Storage / presigned URL).",
        )

        # MVP (simple) : on enregistre juste un "placeholder" en DB
        if st.button("Téléverser"):
            if not file:
                st.error("Veuillez sélectionner un fichier.")
            else:
                try:
                    # Ici, on simule un stockage en mettant un nom de fichier
                    sb.table("videos").insert({
                        "vault_id": vault["id"],
                        "title": title.strip() if title else "Sans titre",
                        "storage_path": f"mvp/{u['id']}/{uuid.uuid4()}_{file.name}",
                        "created_at": iso(now_utc())
                    }).execute()
                    st.success("Vidéo enregistrée (MVP).")
                except Exception:
                    st.error("Erreur d’enregistrement. Vérifiez vos tables et vos politiques RLS.")

        st.markdown("### Vos vidéos")
        vids = list_videos(vault["id"])
        if not vids:
            st.info("Aucune vidéo pour l’instant.")
        else:
            for v in vids[:20]:
                st.write(f"• **{v.get('title','Sans titre')}** — {v.get('created_at','')}")

        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="tm-section">', unsafe_allow_html=True)
        st.markdown("### Créer un accès bénéficiaire (jeton temporaire)")
        ben_email = st.text_input("E-mail du bénéficiaire", placeholder="beneficiaire@exemple.com")
        days = st.selectbox("Durée de validité", [1, 3, 7, 14, 30], index=2)

        if st.button("Générer un jeton"):
            if not ben_email.strip():
                st.error("Veuillez saisir un e-mail bénéficiaire.")
            else:
                try:
                    token, expires_at = create_access_token(vault["id"], ben_email.strip(), int(days))
                    st.success("Jeton créé.")
                    st.code(token)
                    st.caption(f"Expiration : {expires_at} (UTC)")
                except Exception:
                    st.error("Impossible de créer le jeton. Vérifiez vos tables et vos politiques RLS.")
        st.markdown("</div>", unsafe_allow_html=True)


def page_beneficiary_access():
    st.subheader("Accès bénéficiaire")
    st.caption("Collez le jeton reçu pour accéder au coffre (selon les règles d’expiration).")

    token = st.text_input("Jeton", placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

    if st.button("Accéder"):
        if not token.strip():
            st.error("Veuillez coller un jeton.")
            return

        try:
            res = verify_token(token.strip())
            if res == "expired":
                st.error("Jeton expiré.")
                return
            if not res:
                st.error("Jeton invalide.")
                return

            vault_id = res["vault_id"]
            vids = sb.table("videos").select("*").eq("vault_id", vault_id).order("created_at", desc=True).execute().data or []

            st.success("Accès autorisé (MVP).")
            st.markdown("### Contenu disponible")
            if not vids:
                st.info("Aucune vidéo disponible.")
            else:
                for v in vids[:20]:
                    st.write(f"• **{v.get('title','Sans titre')}** — {v.get('created_at','')}")
                    st.caption(f"Chemin stockage (MVP) : {v.get('storage_path','')}")

        except Exception:
            st.error("Erreur d’accès. Consultez les logs Streamlit Cloud.")

    if st.button("Retour à l’accueil"):
        nav_to("Accueil")


# =========================================================
# SIMPLE ROUTER
# =========================================================
PAGES = ["Accueil", "Connexion", "Tableau de bord", "Accès bénéficiaire"]

if "page" not in st.session_state:
    st.session_state["page"] = "Accueil"

# Sidebar nav
st.sidebar.markdown("### Navigation")
choice = st.sidebar.radio("Aller à", PAGES, index=PAGES.index(current_page()))
if choice != current_page():
    nav_to(choice)

# Render page
page = current_page()
if page == "Accueil":
    page_home()
elif page == "Connexion":
    page_auth()
elif page == "Tableau de bord":
    page_dashboard()
elif page == "Accès bénéficiaire":
    page_beneficiary_access()
else:
    page_home()
