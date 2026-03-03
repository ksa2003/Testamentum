import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Kidan Vid", layout="wide")

# ==============================
# PATHS
# ==============================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"

# ==============================
# STYLE
# ==============================
st.markdown("""
<style>
.block-container { padding-top: 0.6rem; padding-bottom: 2rem; max-width: 1100px; }
header { visibility: hidden; }

.kv-hero { display:flex; justify-content:center; margin: 0.2rem 0 1.2rem 0; }
.kv-hero img { width: 100%; max-width: 1000px; height: auto; }

.kv-title { text-align:center; font-size: 34px; font-weight: 700; margin-bottom: 0.5rem; }
.kv-sub { text-align:center; font-size: 18px; max-width: 850px; margin: auto; }

.kv-section { max-width: 850px; margin: 2rem auto; }
.kv-section h2 { margin-bottom: 0.5rem; }

.kv-login-box {
    margin-top: 2rem;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(0,0,0,0.08);
    background: rgba(255,255,255,0.98);
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOGO
# ==============================
if LOGO_PATH.exists():
    b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    st.markdown(f"""
        <div class="kv-hero">
            <img src="data:image/png;base64,{b64}" alt="Kidan Vid"/>
        </div>
    """, unsafe_allow_html=True)

# ==============================
# HEADLINE
# ==============================
st.markdown('<div class="kv-title">Envoyez des vidéos personnelles en toute confidentialité.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kv-sub">
La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne,
accessible uniquement par elle, lorsque vous reposez en paix.
</div>
""", unsafe_allow_html=True)

# ==============================
# AVANTAGES
# ==============================
st.markdown("""
<div class="kv-section">
<ul>
<li>100% sécurisé</li>
<li>Accès unique et contrôlé</li>
<li>Programmation possible</li>
<li>Accessible partout</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ==============================
# COMMENT CA MARCHE
# ==============================
st.markdown('<div class="kv-section">', unsafe_allow_html=True)
st.markdown("## Comment ça marche ?")

st.markdown("""
1️⃣ Vous téléchargez votre vidéo  
2️⃣ Vous identifiez le destinataire  
3️⃣ Nous sécurisons l’accès  
4️⃣ Le destinataire reçoit la vidéo au moment prévu
""")

# ==============================
# CONNEXION EN BAS DE LA SECTION
# ==============================
st.markdown('<div class="kv-login-box">', unsafe_allow_html=True)

st.subheader("Se connecter")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com")

if st.button("Continuer", use_container_width=True):
    if not email.strip():
        st.warning("Veuillez saisir votre e-mail.")
    else:
        st.session_state["prefill_email"] = email.strip()
        st.switch_page("pages/Connexion.py")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================
st.markdown("---")
st.caption("Kidan Vid – Transmission sécurisée et traçable.")
