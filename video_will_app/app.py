import streamlit as st
from theme import apply_theme

# DOIT être le premier appel Streamlit
st.set_page_config(
    page_title="Testamentum",
    page_icon="⚖️",
    layout="centered"
)

apply_theme()

# ---------------- HEADER ----------------

st.markdown("""
<div class="tm-card">
    <div class="tm-title">Testamentum</div>
    <div class="tm-sub">
        Coffre numérique sécurisé pour transmission vidéo posthume
    </div>
    <div class="tm-latin">
        Verba manent. Memoria custoditur.
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- SECTION COMMENCER ----------------

st.markdown('<div class="tm-card">', unsafe_allow_html=True)

st.markdown("## Commencer")

email = st.text_input(
    "Adresse e-mail",
    placeholder="votre-email@exemple.com"
)

st.write("")

# 🔹 Colonnes plus larges et moins espacées
col_left, col_right = st.columns([1, 1], gap="small")

with col_left:
    st.markdown('<div class="tm-btnwrap tm-primary">', unsafe_allow_html=True)
    btn_continue = st.button(
        "Continuer",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="tm-btnwrap">', unsafe_allow_html=True)
    btn_benef = st.button(
        "Accès bénéficiaire",
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------

if btn_continue:
    st.session_state["prefill_email"] = email.strip()
    st.switch_page("pages/Connexion.py")

if btn_benef:
    st.switch_page("pages/Acces_beneficiaire.py")
