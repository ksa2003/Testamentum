import streamlit as st

st.set_page_config(page_title="Tableau de bord • Testamentum", page_icon="🔒", layout="wide")

# ---------------- THEME ----------------
st.markdown("""
<style>
:root{
  --bg:#000000;
  --surface:#0f1419;
  --border:#2f3336;
  --text:#e7e9ea;
  --muted:#8b98a5;
  --accent:#c7cbd1;
  --accent2:#9aa3ad;
}

.stApp{background:var(--bg)!important;}
[data-testid="stSidebar"]{display:none;}
header, footer, #MainMenu{visibility:hidden;}

section.main > div{
  max-width:1000px!important;
  padding-top:2rem!important;
}

.card{
  border:1px solid var(--border);
  background:rgba(15,20,25,0.7);
  backdrop-filter:blur(10px);
  padding:22px;
  border-radius:16px;
  margin-bottom:20px;
}

.stButton button{
  background:linear-gradient(180deg,var(--accent),var(--accent2))!important;
  color:#0b0f14!important;
  border-radius:999px!important;
  font-weight:900!important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='color:#e7e9ea;'>Tableau de bord</h1>", unsafe_allow_html=True)
st.markdown("<div style='color:#8b98a5;'>Gestion de vos messages vidéo et bénéficiaires.</div>", unsafe_allow_html=True)

st.write("")

# ---------------- UPLOAD SECTION ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Téléverser une vidéo")
title = st.text_input("Titre du message")
video = st.file_uploader("Sélectionner une vidéo", type=["mp4","mov","webm"])
if st.button("Téléverser"):
    st.success("Vidéo enregistrée (mock).")
st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIST ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Vos vidéos")
st.markdown("<div style='color:#8b98a5;'>Aucune vidéo pour l’instant.</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
if st.button("Se déconnecter"):
    st.switch_page("app.py")
