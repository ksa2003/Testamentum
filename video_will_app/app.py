import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ------------------------------------------------------------
# THEME GLOBAL X (noir)
# ------------------------------------------------------------
st.markdown(
    """
    <style>
      #MainMenu {visibility:hidden;}
      footer {visibility:hidden;}
      header {visibility:hidden;}
      [data-testid="stSidebar"] {display:none;}

      :root{
        --bg:#000000;
        --surface:#0f1419;
        --border:#2f3336;
        --text:#e7e9ea;
        --muted:#8b98a5;
        --accent:#1d9bf0;
      }

      .stApp{ background: var(--bg) !important; }
      section.main > div{
        max-width: 980px !important;
        padding-top: 1rem !important;
      }

      .stTextInput input{
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        color: var(--text) !important;
        caret-color: var(--text) !important;
        border-radius: 14px !important;
        padding: 0.95rem 1rem !important;
      }

      .stTextInput input::placeholder{
        color: var(--muted) !important;
      }

      .stTextInput label{
        color: var(--muted) !important;
        font-weight: 800 !important;
      }

      .stButton button{
        background: var(--accent) !important;
        color: #001018 !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.9rem 1rem !important;
        font-weight: 900 !important;
        width: 100%;
      }

      .fine{
        color: var(--muted);
        font-size: 0.86rem;
        margin-top: 10px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Sélecteur de mode
# ------------------------------------------------------------
mode = st.radio(
    "Mode d'affichage",
    ["Flat (100% noir)", "Card X (effet carte floutée)"],
    horizontal=True
)

# ------------------------------------------------------------
# HERO - VERSION FLAT
# ------------------------------------------------------------
if mode == "Flat (100% noir)":

    hero = """
    <div style="
      border:1px solid #2f3336;
      background:#000000;
      border-radius:18px;
      padding:18px;
    ">
      <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px;">
        <div style="color:#e7e9ea; font-weight:900; font-size:1.05rem;">Testamentum</div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5;">Sécurité</span>
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5;">Confidentialité</span>
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5;">Traçabilité</span>
        </div>
      </div>

      <div style="margin-top:14px; color:#e7e9ea; font-weight:950; font-size:2.3rem; line-height:1.1;">
        Un message vidéo, transmis au bon moment.
      </div>

      <div style="margin-top:10px; color:#e7e9ea; opacity:.9; line-height:1.6;">
        Enregistrez un message vidéo destiné à vos proches, puis contrôlez l’accès des bénéficiaires
        lorsque le décès est déclaré. Le tout avec des règles strictes.
      </div>
    </div>
    """

# ------------------------------------------------------------
# HERO - VERSION CARD X
# ------------------------------------------------------------
else:

    hero = """
    <div style="
      border:1px solid #2f3336;
      background: rgba(15,20,25,0.72);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border-radius:18px;
      padding:18px;
    ">
      <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px;">
        <div style="color:#e7e9ea; font-weight:900; font-size:1.05rem;">Testamentum</div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5; background:rgba(255,255,255,0.02);">Sécurité</span>
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5; background:rgba(255,255,255,0.02);">Confidentialité</span>
          <span style="border:1px solid #2f3336; padding:6px 12px; border-radius:999px; color:#8b98a5; background:rgba(255,255,255,0.02);">Traçabilité</span>
        </div>
      </div>

      <div style="margin-top:14px; color:#e7e9ea; font-weight:950; font-size:2.3rem; line-height:1.1;">
        Un message vidéo, transmis au bon moment.
      </div>

      <div style="margin-top:10px; color:#e7e9ea; opacity:.9; line-height:1.6;">
        Enregistrez un message vidéo destiné à vos proches, puis contrôlez l’accès des bénéficiaires
        lorsque le décès est déclaré. Le tout avec des règles strictes.
      </div>
    </div>
    """

# Render HERO
components.html(hero, height=260, scrolling=False)

st.write("")

# ------------------------------------------------------------
# SECTION COMMENCER
# ------------------------------------------------------------
st.subheader("Commencer")
st.caption("Saisissez votre adresse e-mail pour créer un compte ou vous connecter.")

email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

if st.button("Continuer"):
    st.session_state["prefill_email"] = email.strip()
    st.switch_page("pages/1_Connexion.py")

st.markdown(
    '<div class="fine">En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).</div>',
    unsafe_allow_html=True,
)
