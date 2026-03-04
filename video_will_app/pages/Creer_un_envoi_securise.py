import streamlit as st
import random
import time

st.set_page_config(page_title="Créer un envoi sécurisé", layout="wide")

st.title("Créer un envoi sécurisé")

st.subheader("1) Téléversement de la vidéo")
video = st.file_uploader("Choisir une vidéo (MP4)", type=["mp4", "mov", "m4v"])

st.subheader("2) Destinataire")
dest_email = st.text_input("Email du destinataire")
dest_phone = st.text_input("Téléphone du destinataire (format international recommandé)")

st.subheader("3) Sécurisation de l’accès")
st.write("Un code unique et une double authentification (2FA) seront requis à l’ouverture.")

# --- MVP 2FA (démo) ---
st.markdown("### Démonstration 2FA (MVP)")
st.write(
    "Cette étape simule un OTP. En production : envoi réel par SMS/Email + stockage en base + expiration."
)

if "otp_code" not in st.session_state:
    st.session_state.otp_code = None
if "otp_expire" not in st.session_state:
    st.session_state.otp_expire = None

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Générer un code**")
    if st.button("Générer un code OTP", use_container_width=True):
        st.session_state.otp_code = f"{random.randint(100000, 999999)}"
        st.session_state.otp_expire = time.time() + 300  # 5 minutes
        st.info(f"Code OTP (démo) : {st.session_state.otp_code} (valide 5 minutes)")

with col2:
    st.markdown("**Entrer l’OTP**")
    otp_input = st.text_input(
        "",
        max_chars=6,
        placeholder="6 chiffres",
        label_visibility="collapsed",
    )

valid_otp = False
if st.session_state.otp_code and st.session_state.otp_expire:
    if time.time() <= st.session_state.otp_expire and otp_input == st.session_state.otp_code:
        valid_otp = True
        st.success("OTP validé.")
    elif otp_input and otp_input != st.session_state.otp_code:
        st.error("OTP incorrect.")
    elif st.session_state.otp_expire and time.time() > st.session_state.otp_expire:
        st.error("OTP expiré. Regénérez un code.")

st.subheader("4) Planification")
access_deadline = st.date_input("Date limite d’accès (optionnel)")

st.subheader("5) Création")
can_create = bool(video) and bool(dest_email) and valid_otp

if st.button("Créer l’envoi sécurisé", use_container_width=True, disabled=not can_create):
    st.success(
        "Envoi créé (MVP). Prochaine étape : stockage chiffré + règles d’accès + traçabilité + notification destinataire."
    )
