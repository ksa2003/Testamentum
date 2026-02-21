import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Testamentum", page_icon="🔒", layout="wide")

# ------------------------------------------------------------
# THEME X NOIR PROPRE
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
        padding-top: 1.5rem !important;
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
# HERO SECTION AVEC MARQUE FORTE
# ------------------------------------------------------------
hero = """
<div style="
  border:1px solid #2f3336;
  background:#000000;
  border-radius:18px;
  padding:32px;
">

  <!-- NOM DU SITE -->
  <div style="
      font-size:clamp(3rem, 6vw, 4.2rem);
      font-weight:1000;
      letter-spacing:0.02em;
      color:#ffffff;
      line-height:1;
  ">
      Testamentum
  </div>

  <!-- Sous-titre institutionnel -->
  <div style="
      margin-top:8px;
      font-size:1.1rem;
      color:#8b98a5;
      font-weight:600;
  ">
      Coffre numérique sécurisé pour transmission vidéo posthume
  </div>

  <div style="height:28px;"></div>

  <!-- Phrase forte -->
  <div style="
      color:#e7e9ea;
      font-weight:900;
      font-size:clamp(1.6rem, 3.8vw, 2.4rem);
      line-height:1.2;
  ">
      Un message vidéo, transmis au bon moment.
  </div>

  <div style="
      margin-top:14px;
      color:#e7e9ea;
      opacity:.9;
      line-height:1.65;
      font-size:1.05rem;
      max-width:70ch;
  ">
      Enregistrez un message destiné à vos proches, puis contrôlez précisément
      l’accès des bénéficiaires lorsque le décès est déclaré.
      Le tout avec des règles strictes (jeton, expiration, journalisation).
  </div>

  <div style="
      margin-top:16px;
      color:#e7e9ea;
      opacity:.85;
      line-height:1.7;
  ">
      • Accès bénéficiaires par jeton temporaire sécurisé<br/>
      • Option de validation notariale (workflow métier)<br/>
      • Historique des actions pour la traçabilité (MVP)
  </div>

</div>
"""

components.html(hero, height=420, scrolling=False)

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
