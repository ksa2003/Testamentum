import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Kidan Vid", layout="wide")

# -------- Paths
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"  # mettez votre logo ici

# -------- CSS
st.markdown(
    """
<style>
.block-container { padding-top: 0.6rem; padding-bottom: 2rem; max-width: 1200px; }
header { visibility: hidden; }

.kv-hero { display:flex; justify-content:center; margin: 0.2rem 0 1.2rem 0; }
.kv-hero img { width: 100%; max-width: 1100px; height: auto; }

.kv-title { text-align:center; font-size: 34px; font-weight: 750; margin: 0.2rem 0 0.2rem 0; }
.kv-sub { text-align:center; font-size: 18px; opacity: 0.92; max-width: 900px; margin: 0 auto; }

.kv-points { max-width: 760px; margin: 1.0rem auto 0 auto; line-height: 1.9; font-size: 16px; }
.kv-points li { margin-bottom: 0.2rem; }

.kv-section { max-width: 980px; margin: 1.2rem auto; }
.kv-card { border: 1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.03); border-radius: 14px; padding: 16px; }
.kv-muted { opacity: 0.85; }
</style>
""",
    unsafe_allow_html=True,
)

# -------- Logo banner (sans use_container_width pour compatibilité)
if LOGO_PATH.exists():
    b64 = base64.b64encode(LOGO_PATH.read_bytes()).decode("utf-8")
    st.markdown(
        f"""
        <div class="kv-hero">
            <img src="data:image/png;base64,{b64}" alt="Kidan Vid"/>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning(f"Logo introuvable : {LOGO_PATH} (attendu : assets/logo_kidan_vid.png)")

# -------- Headline (DOC)
st.markdown('<div class="kv-title">Envoyez des vidéos personnelles en toute confidentialité.</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="kv-sub">
La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, accessible uniquement par elle,
lorsque vous reposez en paix.
</div>
""",
    unsafe_allow_html=True,
)

# -------- Key points (DOC)
st.markdown(
    """
<div class="kv-points">
<ul>
  <li>100% sécurisé</li>
  <li>Accès unique et contrôlé</li>
  <li>Programmation possible</li>
  <li>Accessible partout</li>
</ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# -------- Buttons (DOC)
c1, c2 = st.columns(2)
with c1:
    if st.button("Découvrir comment ça marche", use_container_width=True):
        st.switch_page("pages/Comment_ca_marche.py")
with c2:
    if st.button("Créer un envoi sécurisé", use_container_width=True):
        st.switch_page("pages/Connexion.py")

# -------- Sections (DOC) as quick access
st.markdown("<div class='kv-section'></div>", unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
with s1:
    if st.button("Pourquoi Kidan Vid", use_container_width=True):
        st.switch_page("pages/Pourquoi_Kidan_Vid.py")
with s2:
    if st.button("Cas d’usage", use_container_width=True):
        st.switch_page("pages/Cas_d_usage.py")
with s3:
    if st.button("Nos offres", use_container_width=True):
        st.switch_page("pages/Nos_offres.py")
with s4:
    if st.button("Sécurité", use_container_width=True):
        st.switch_page("pages/Securite_technique.py")

st.markdown("<br>", unsafe_allow_html=True)

# -------- Footer note
st.caption("Kidan Vid est conçu pour une transmission respectueuse, sécurisée et traçable.")
