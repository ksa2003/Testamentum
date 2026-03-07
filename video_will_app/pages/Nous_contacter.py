import streamlit as st

st.set_page_config(page_title="Nous contacter", layout="centered")

st.markdown(
    """
    <style>
      .block-container { max-width: 860px; padding-top: 1.5rem; }
      a.anchor-link { display:none !important; }
      .box {
        border: 1px solid rgba(10,102,194,0.16);
        border-radius: 16px;
        padding: 18px;
        background: #ffffff;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Nous contacter")

st.write(
    """
Vous pouvez utiliser ce formulaire pour toute demande liée :
- au fonctionnement du site
- à la sécurité des accès
- à l’espace mémoire
- à la gestion des bénéficiaires
- à la partie notariale et documentaire
"""
)

with st.form("contact_form"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    sujet = st.selectbox(
        "Sujet",
        [
            "Support technique",
            "Question juridique / notaire",
            "Sécurité / accès",
            "Compte abonné",
            "Autre",
        ],
    )
    message = st.text_area("Message", height=160)
    submitted = st.form_submit_button("Envoyer la demande")

    if submitted:
        if not nom or not email or not message:
            st.warning("Veuillez compléter au minimum le nom, l’email et le message.")
        else:
            st.success("Votre demande a été enregistrée (prototype).")

st.markdown("---")
st.subheader("Informations de contact")
st.markdown(
    """
- Support général : via ce formulaire  
- Sujets juridiques : via l’espace notarial ou les partenaires notaires  
- Sécurité : via l’espace abonné et les parcours d’accès protégés  
"""
)

if st.button("Retour accueil"):
    st.switch_page("app.py")
