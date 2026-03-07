import streamlit as st

st.set_page_config(page_title="Connexion", layout="centered")

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

st.title("Connexion")

st.markdown(
    """
    <div class="login-wrap">
        <h3 style="margin-top:0;color:#084C95;">Bienvenue dans votre espace Kidan Vid</h3>
        <div style="color:#23476a;">
            Connectez-vous pour accéder à vos vidéos, documents, bénéficiaires et paramètres de sécurité.
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
        Kidan Vid intègre le notaire comme pilier central pour sécuriser la transmission.
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("login_form"):
    email = st.text_input("Adresse e-mail", placeholder="votre@email.com")
    password = st.text_input("Mot de passe", type="password", placeholder="Votre mot de passe")
    submitted = st.form_submit_button("Se connecter", use_container_width=True)

    if submitted:
        if not email or not password:
            st.warning("Veuillez compléter l’adresse e-mail et le mot de passe.")
        else:
            st.session_state["user_email"] = email.strip()
            st.success("Connexion réussie.")
            st.switch_page("pages/Espace_Memoire.py")

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")
