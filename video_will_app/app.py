# app.py — Landing page Kidan Vid avec bouton "Se connecter"
# Remplace entièrement le fichier app.py par ce contenu.

import streamlit as st
from pathlib import Path
import base64

# -----------------------
# Config page
# -----------------------
st.set_page_config(page_title="Kidan Vid", layout="wide")

# -----------------------
# Chemins
# -----------------------
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"  # attendu : video_will_app/assets/logo_kidan_vid.png

# -----------------------
# Styles
# -----------------------
st.markdown(
    """
<style>
.block-container { padding-top: 0.6rem; padding-bottom: 2rem; max-width: 1200px; }
header { visibility: hidden; }

.kv-hero { display:flex; justify-content:center; margin: 0.2rem 0 1.2rem 0; }
.kv-hero img { width: 100%; max-width: 1100px; height: auto; }

.kv-title { text-align:center; font-size: 34px; font-weight: 700; margin: 0.2rem 0 0.2rem 0; color: #111; }
.kv-sub { text-align:center; font-size: 18px; opacity: 0.95; max-width: 900px; margin: 0 auto; color: #222; }

.kv-points { max-width: 760px; margin: 1.0rem auto 0 auto; line-height: 1.85; font-size: 16px; color: #333; }
.kv-points li { margin-bottom: 0.2rem; }

.kv-section { max-width: 980px; margin: 1.2rem auto; }
.kv-card { border: 1px solid rgba(0,0,0,0.06); background: rgba(255,255,255,0.98); border-radius: 12px; padding: 16px; }
.kv-muted { opacity: 0.9; }

.kv-cta-row { max-width: 740px; margin: 1.2rem auto; display:flex; gap:12px; }
.kv-btn {
    width:100%;
    padding: 12px 16px;
    border-radius: 12px;
    font-weight: 700;
    border: 1px solid rgba(0,0,0,0.06);
}
.kv-btn-primary { background: #111; color: #fff; }
.kv-btn-ghost { background: transparent; color: #111; border: 1px solid rgba(0,0,0,0.06); }

.kv-login { max-width: 420px; margin: 1.2rem auto; display:flex; gap:8px; align-items:center; }
.kv-input { width: 100%; }
.kv-login .stButton button { height:48px; border-radius:10px; font-weight:700; }
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------
# Logo (affichage via base64 pour compatibilité)
# -----------------------
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

# -----------------------
# Headline & description
# -----------------------
st.markdown('<div class="kv-title">Envoyez des vidéos personnelles en toute confidentialité.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="kv-sub">La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, accessible uniquement par elle, lorsque vous reposez en paix.</div>',
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# Email + bouton Se connecter (visibilité principale demandée)
# - Si l'utilisateur remplit l'email puis clique "Se connecter", on préfillera la page Connexion.
# -----------------------
st.markdown('<div class="kv-section">', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; margin-bottom:8px;"><strong>Connectez-vous pour gérer vos envois sécurisés</strong></div>', unsafe_allow_html=True)
email_input = st.text_input("Adresse e-mail", placeholder="votre@email.com", key="landing_email")

col_a, col_b = st.columns([2,1])
with col_a:
    # Bouton principal "Se connecter" : redirection vers pages/Connexion.py
    if st.button("Se connecter", key="landing_login"):
        if not (email_input and email_input.strip()):
            st.warning("Veuillez saisir votre adresse e-mail avant de continuer.")
        else:
            st.session_state["prefill_email"] = email_input.strip()
            # nom exact : pages/Connexion.py
            st.switch_page("pages/Connexion.py")

with col_b:
    # Bouton secondaire pour créer un envoi (mène aussi à Connexion)
    if st.button("Créer un envoi sécurisé", key="landing_create"):
        if email_input and email_input.strip():
            st.session_state["prefill_email"] = email_input.strip()
        st.switch_page("pages/Connexion.py")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# Avantages clés (visuels)
# -----------------------
st.markdown(
    """
<div class="kv-points">
<ul>
  <li><strong>Sécurité</strong> — chiffrement et journalisation</li>
  <li><strong>Contrôle</strong> — accès unique et traçable pour vos bénéficiaires</li>
  <li><strong>Programmation</strong> — transmission conditionnelle (déclaration de décès)</li>
  <li><strong>International</strong> — architecture pensée pour multi-régions</li>
</ul>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# CTA sections rapides (nav)
# -----------------------
s1, s2, s3, s4 = st.columns(4)
with s1:
    if st.button("Découvrir comment ça marche", use_container_width=True):
        st.switch_page("pages/Comment_ca_marche.py")
with s2:
    if st.button("Pourquoi Kidan Vid", use_container_width=True):
        st.switch_page("pages/Pourquoi_Kidan_Vid.py")
with s3:
    if st.button("Nos offres", use_container_width=True):
        st.switch_page("pages/Nos_offres.py")
with s4:
    if st.button("Sécurité", use_container_width=True):
        st.switch_page("pages/Securite_technique.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------
# Sections explicatives courtes (accroches)
# -----------------------
st.markdown(
    """
<div class="kv-section">
  <div class="kv-card">
    <h3>Comment ça marche</h3>
    <p class="kv-muted">Téléchargez votre vidéo, indiquez vos bénéficiaires, choisissez la condition d'envoi — nous nous occupons du reste (sécurisé, traçable).</p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# Footer léger
# -----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Kidan Vid — service conçu pour une transmission respectueuse, sécurisée et traçable.")
