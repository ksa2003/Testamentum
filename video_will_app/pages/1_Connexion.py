import streamlit as st

st.set_page_config(page_title="Connexion • Testamentum", page_icon="🔒", layout="wide")

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
  padding:0.9rem 1rem!important;
}

.stButton button{
  background:linear-gradient(180deg,var(--accent),var(--accent2))!important;
  color:#0b0f14!important;
  border-radius:999px!important;
  font-weight:900!important;
  padding:0.9rem!important;
  width:100%;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<h1 style='color:#e7e9ea;'>Connexion</h1>", unsafe_allow_html=True)
st.markdown("<div style='color:#8b98a5;'>Accédez à votre coffre sécurisé.</div>", unsafe_allow_html=True)

st.write("")

email = st.text_input("Adresse e-mail")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter"):
    # ici vous mettrez votre auth Supabase
    st.success("Connexion validée (mock).")
    st.switch_page("pages/2_Tableau_de_bord.py")

st.write("")
if st.button("Retour à l’accueil"):
    st.switch_page("app.py")
