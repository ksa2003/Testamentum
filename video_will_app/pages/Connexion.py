import streamlit as st

st.set_page_config(page_title="Créer mon coffre Kidanmemoris", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"

st.markdown(
    f"""
    <style>
      .block-container {{
        max-width: 760px;
        padding-top: 2rem;
        padding-bottom: 3rem;
      }}
      a.anchor-link {{
        display: none !important;
      }}
      .login-wrap {{
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 20px;
        padding: 24px;
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

st.title("Créer mon coffre Kidanmemoris")

st.markdown(
    """
    <div class="login-wrap">
        <h3 style="margin-top:0;color:#084C95;">Le coffre du patrimoine émotionnel</h3>
        <div style="color:#23476a;">
            Créez votre coffre sécurisé pour transmettre des messages, souvenirs familiaux,
            lettres numériques et contenus programmés pour des moments de vie futurs.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

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

with st.form("coffre_form"):
    nom = st.text_input("Nom")
    email = st.text_input("Email", placeholder="votre@email.com")
    verification = st.selectbox("Vérification identité", ["À compléter", "Pièce d’identité", "Passeport", "Autre"])
    contact_confiance = st.text_input("Contact de confiance (confirmation du décès)")
    submitted = st.form_submit_button("Activer le coffre", use_container_width=True)

    if submitted:
        if not nom or not email:
            st.warning("Veuillez compléter au minimum le nom et l’email.")
        else:
            st.session_state["user_name"] = nom.strip()
            st.session_state["user_email"] = email.strip()
            st.session_state["verification_identite"] = verification
            st.session_state["contact_confiance"] = contact_confiance.strip()
            st.success("Votre coffre Kidanmemoris est activé.")
            st.switch_page("pages/Espace_Memoire.py")

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")
