import streamlit as st

st.set_page_config(page_title="Accès bénéficiaire • Testamentum", page_icon="🔒", layout="wide")

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
  max-width:760px!important;
  padding-top:2rem!important;
}

.stTextInput input{
  background:var(--surface)!important;
  border:1px solid var(--border)!important;
  color:var(--text)!important;
  border-radius:14px!important;
}

.stButton button{
  background:linear-gradient(180deg,var(--accent),var(--accent2))!important;
  color:#0b0f14!important;
  border-radius:999px!important;
  font-weight:900!important;
  width:100%;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<h1 style='color:#e7e9ea;'>Accès bénéficiaire</h1>", unsafe_allow_html=True)
st.markdown("<div style='color:#8b98a5;'>Veuillez saisir votre jeton d’accès sécurisé.</div>", unsafe_allow_html=True)

st.write("")

token = st.text_input("Jeton d’accès")

if st.button("Accéder au message"):
    st.success("Jeton validé (mock).")
