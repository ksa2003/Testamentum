import streamlit as st

# -----------------------------------------------------
# CONFIG PAGE
# -----------------------------------------------------

st.set_page_config(
    page_title="Kidan Vid",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------
# STYLE GLOBAL BLEU (THEME PRINCIPAL)
# -----------------------------------------------------

st.markdown("""
<style>

/* Fond global bleu */
.stApp {
    background: linear-gradient(180deg,#0A66C2 0%,#084C95 100%);
}

/* texte global */
html, body, [class*="css"] {
    color: white;
}

/* container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* cartes */
.card {
    background: rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.15);
}

/* hero */
.hero-box {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* boite juridique */
.legal-box {
    border-left: 5px solid #ffffff;
    background: rgba(255,255,255,0.08);
    padding: 14px 16px;
    border-radius: 10px;
    margin: 18px 0;
}

/* boutons */
.stButton>button {
    background:white;
    color:#0A66C2;
    border-radius:10px;
    border:none;
    font-weight:600;
}

.stButton>button:hover {
    background:#eaf4ff;
}

/* sidebar */
section[data-testid="stSidebar"] {
    background:#063970;
}

/* champs */
input, textarea {
    background:rgba(255,255,255,0.1) !important;
    color:white !important;
}

/* select */
div[data-baseweb="select"] {
    background:rgba(255,255,255,0.1);
}

/* tabs */
button[data-baseweb="tab"] {
    color:white;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background:#0A66C2;
}

/* footer streamlit */
footer {
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.image("assets/logo_kidan_vid.png", width=250)

st.markdown(
"""
<div class="hero-box">

<h2>Kidan Vid</h2>

Plateforme de transmission vidéo, audio et documentaire sécurisée.

Envoyez des messages personnels en toute confidentialité.
Vidéos, audios, documents et accès bénéficiaire sont organisés
dans une logique humaine, technique et juridique.

</div>
""",
unsafe_allow_html=True
)

# -----------------------------------------------------
# AVERTISSEMENT JURIDIQUE
# -----------------------------------------------------

st.markdown(
"""
<div class="legal-box">

<b>Point juridique important</b>

En France, une vidéo seule ne constitue pas un testament juridiquement valable.
Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.

</div>
""",
unsafe_allow_html=True
)

# -----------------------------------------------------
# BOUTONS
# -----------------------------------------------------

col1,col2 = st.columns(2)

with col1:
    if st.button("Découvrir comment ça marche"):
        st.switch_page("pages/Comment_ca_marche.py")

with col2:
    if st.button("Créer un envoi sécurisé"):
        st.switch_page("pages/Connexion.py")

# -----------------------------------------------------
# PILIERS
# -----------------------------------------------------

st.markdown("## Les 4 piliers Kidan Vid")

col1,col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">

    🎥 <b>Vidéo</b>

    Messages vidéo personnels programmés
    et délivrés au bon moment.

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">

    🎤 <b>Audio</b>

    Souvenirs vocaux, témoignages
    sonores et compléments de transmission.

    </div>
    """, unsafe_allow_html=True)

col3,col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">

    🛡️ <b>Sécurisation</b>

    Protection technique :
    chiffrement, double authentification
    et traçabilité.

    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">

    ⚖️ <b>Notaires</b>

    Le pilier juridique central
    pour articuler la transmission avec le droit.

    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------
# TEMOIGNAGES
# -----------------------------------------------------

st.markdown("## Témoignages")

st.video("https://www.youtube.com/watch?v=oRVvi5xWF1k")

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.markdown("---")

col1,col2,col3 = st.columns(3)

with col1:
    if st.button("Qui sommes-nous"):
        st.switch_page("pages/Pourquoi_Kidan_Vid.py")

with col2:
    if st.button("Sécurité technique"):
        st.switch_page("pages/Securite_technique.py")

with col3:
    if st.button("Mentions légales"):
        st.switch_page("pages/Mentions_legales.py")
