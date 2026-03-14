import streamlit as st

st.set_page_config(page_title="Accès bénéficiaire", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_SOFT = "#EAF4FF"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 760px;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
      }}
      a.anchor-link {{
        display: none !important;
      }}
      .box {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 18px;
        padding: 22px;
        background: linear-gradient(180deg, #ffffff 0%, {BLUE_SOFT} 100%);
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

st.title("Accès bénéficiaire")

st.markdown(
    """
    <div class="box">
        <h3 style="margin-top:0;">Accéder à un contenu qui vous est destiné</h3>
        <div>
            Saisissez les informations reçues pour consulter le contenu auquel vous avez été autorisé à accéder.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="legal-box">
        <strong>Information importante</strong><br>
        Certains contenus peuvent avoir une valeur émotionnelle forte, mais un testament vidéo seul n’a pas de valeur juridique en France.
        Lorsque nécessaire, Kidanmemoris prévoit l’intervention du notaire comme pilier central.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("benef_form"):
    lien_unique = st.text_input("Lien ou code d’accès")
    email = st.text_input("Votre email")
    otp = st.text_input("Code OTP", max_chars=6)
    submitted = st.form_submit_button("Accéder au contenu", use_container_width=True)

    if submitted:
        if not lien_unique or not email or not otp:
            st.warning("Veuillez compléter le lien/code, l’email et l’OTP.")
        else:
            st.success("Accès validé (prototype).")

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
