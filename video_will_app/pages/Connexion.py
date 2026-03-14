import re
import streamlit as st

st.set_page_config(page_title="Créer mon coffre Kidanmemorris", layout="centered")

BLUE_MAIN = "#0A66C2"
BLUE_DARK = "#084C95"
BLUE_SOFT = "#EAF4FF"


def email_valide(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email.strip()))


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

      .section-title {{
        margin-top: 0;
        color: {BLUE_DARK};
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Créer mon coffre Kidanmemorris")

st.markdown(
    """
    <div class="login-wrap">
        <h3 class="section-title">Le coffre du patrimoine émotionnel</h3>
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
        Kidanmemorris intègre le notaire comme pilier central pour sécuriser la transmission successorale.
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2 = st.tabs(["Créer mon coffre", "Se connecter"])

with tab1:
    with st.form("coffre_form"):
        nom = st.text_input("Nom complet")
        email = st.text_input("Email", placeholder="votre@email.com")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        confirmer_mot_de_passe = st.text_input("Confirmer le mot de passe", type="password")

        verification = st.selectbox(
            "Vérification identité",
            ["À compléter", "Pièce d’identité", "Passeport", "Autre"]
        )

        contact_confiance = st.text_input("Contact de confiance (confirmation du décès)")

        submitted_create = st.form_submit_button("Activer le coffre", use_container_width=True)

        if submitted_create:
            erreurs = []

            if not nom.strip():
                erreurs.append("Veuillez renseigner votre nom complet.")

            if not email.strip():
                erreurs.append("Veuillez renseigner votre email.")
            elif not email_valide(email):
                erreurs.append("Veuillez saisir une adresse email valide.")

            if not mot_de_passe:
                erreurs.append("Veuillez saisir un mot de passe.")
            elif len(mot_de_passe) < 8:
                erreurs.append("Le mot de passe doit contenir au moins 8 caractères.")

            if mot_de_passe != confirmer_mot_de_passe:
                erreurs.append("Les mots de passe ne correspondent pas.")

            if erreurs:
                for err in erreurs:
                    st.warning(err)
            else:
                st.session_state["user_name"] = nom.strip()
                st.session_state["user_email"] = email.strip()
                st.session_state["user_password"] = mot_de_passe
                st.session_state["verification_identite"] = verification
                st.session_state["contact_confiance"] = contact_confiance.strip()
                st.session_state["is_authenticated"] = True

                st.success("Votre coffre Kidanmemorris a bien été créé.")
                st.switch_page("pages/Espace_Memoire.py")

with tab2:
    with st.form("login_form"):
        email_connexion = st.text_input("Email de connexion", placeholder="votre@email.com")
        mot_de_passe_connexion = st.text_input("Mot de passe", type="password")

        submitted_login = st.form_submit_button("Se connecter", use_container_width=True)

        if submitted_login:
            if not email_connexion.strip() or not mot_de_passe_connexion:
                st.warning("Veuillez renseigner votre email et votre mot de passe.")
            else:
                saved_email = st.session_state.get("user_email", "")
                saved_password = st.session_state.get("user_password", "")

                if saved_email and saved_password:
                    if (
                        email_connexion.strip() == saved_email
                        and mot_de_passe_connexion == saved_password
                    ):
                        st.session_state["is_authenticated"] = True
                        st.success("Connexion réussie.")
                        st.switch_page("pages/Espace_Memoire.py")
                    else:
                        st.error("Email ou mot de passe incorrect.")
                else:
                    st.info(
                        "Aucun compte local n’a encore été créé dans cette session. "
                        "Créez d’abord votre coffre dans l’onglet « Créer mon coffre »."
                    )

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("Retour accueil", use_container_width=True):
        st.switch_page("app.py")
with c2:
    if st.button("Accès bénéficiaire", use_container_width=True):
        st.switch_page("pages/Acces_beneficiaire.py")
