import random
import time
from datetime import date, datetime

import streamlit as st

st.set_page_config(page_title="Créer une transmission", layout="wide")

BLUE_MAIN = "#0A66C2"
BLUE_SOFT = "#EAF4FF"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 980px;
        padding-top: 1.6rem;
        padding-bottom: 3rem;
      }}
      a.anchor-link {{
        display: none !important;
      }}
      .section-box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 18px;
        padding: 18px;
        background: #ffffff;
        margin-bottom: 18px;
      }}
      .legal-box {{
        border-left: 5px solid {BLUE_MAIN};
        background: #f5faff;
        padding: 14px 16px;
        border-radius: 10px;
        margin: 18px 0;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Créer une transmission Kidanmemoris")

st.markdown(
    """
    <div class="legal-box">
        <strong>Point juridique important</strong><br>
        En France, une vidéo seule ne constitue pas un testament juridiquement valable.
        Kidanmemoris intègre le notaire comme pilier central pour sécuriser la transmission successorale.
    </div>
    """,
    unsafe_allow_html=True,
)

if "otp_code" not in st.session_state:
    st.session_state.otp_code = None
if "otp_expire" not in st.session_state:
    st.session_state.otp_expire = None

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("1) Enregistrer ou téléverser un contenu")
    contenu_type = st.selectbox(
        "Type de contenu",
        ["Message vidéo", "Souvenir familial", "Lettre numérique", "Document patrimonial"]
    )
    action_video = st.selectbox(
        "Action",
        ["Enregistrer maintenant", "Télécharger une vidéo", "Recommencer"]
    )

    if action_video == "Télécharger une vidéo":
        uploaded_file = st.file_uploader("Choisir un fichier", type=["mp4", "mov", "m4v", "avi", "mkv", "webm", "pdf", "png", "jpg", "jpeg", "doc", "docx"])
    else:
        uploaded_file = None

    st.info("Conseils : message pour un enfant, message pour un partenaire, message familial.")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("2) Choisir les destinataires")
    dest_nom = st.text_input("Nom")
    dest_email = st.text_input("Email")
    dest_phone = st.text_input("Téléphone")
    dest_mode = st.selectbox(
        "Type de destinataire",
        ["1 destinataire", "Plusieurs destinataires", "Destinataire collectif (famille)"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("3) Sécurisation de l’accès")
    st.write("Un code unique et une double authentification (2FA) peuvent être requis à l’ouverture.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Générer un code OTP", use_container_width=True):
            st.session_state.otp_code = f"{random.randint(100000, 999999)}"
            st.session_state.otp_expire = time.time() + 300
            st.info(f"Code OTP (démo) : {st.session_state.otp_code} (valide 5 minutes)")
    with col2:
        otp_input = st.text_input("Entrer l’OTP", max_chars=6, placeholder="6 chiffres")

    valid_otp = False
    if st.session_state.otp_code and st.session_state.otp_expire:
        if time.time() <= st.session_state.otp_expire and otp_input == st.session_state.otp_code:
            valid_otp = True
            st.success("OTP validé.")
        elif otp_input and otp_input != st.session_state.otp_code:
            st.error("OTP incorrect.")
        elif time.time() > st.session_state.otp_expire:
            st.error("OTP expiré. Regénérez un code.")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("4) Paramètres de transmission")
    transmission = st.selectbox(
        "Transmission",
        ["Après confirmation de décès", "Date programmée", "Événement spécifique"]
    )

    if transmission == "Date programmée":
        c1, c2 = st.columns(2)
        with c1:
            d = st.date_input("Date d’ouverture", value=date.today())
        with c2:
            t = st.time_input("Heure d’ouverture", value=datetime.now().time().replace(second=0, microsecond=0))
    else:
        d = None
        t = None

    evenement = st.text_input("Événement spécifique (optionnel)", placeholder="Mariage, naissance, 18 ans, anniversaire important...")
    visionnage = st.selectbox(
        "Visionnage",
        ["Visionnage unique", "Accès pendant 7 jours", "Accès permanent"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.subheader("5) Création")
    can_create = bool(dest_email) and valid_otp

    if st.button("Créer la transmission", use_container_width=True, disabled=not can_create):
        st.success("Transmission créée (prototype).")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("Voir le coffre", use_container_width=True):
        st.switch_page("pages/Espace_Memoire.py")
