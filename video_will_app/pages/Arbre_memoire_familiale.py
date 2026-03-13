import streamlit as st

st.set_page_config(page_title="Arbre de mémoire familiale", layout="centered")

if "family_tree" not in st.session_state:
    st.session_state.family_tree = []

st.title("Arbre de mémoire familiale")

st.write(
    """
Chaque famille peut créer un arbre familial et associer des messages pour chaque génération.
L’objectif est de construire une mémoire familiale numérique.
"""
)

with st.form("family_tree_page_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        nom = st.text_input("Nom")
        relation = st.text_input("Relation")
    with c2:
        generation = st.selectbox("Génération", ["Grand-parents", "Parents", "Enfants", "Petits-enfants", "Autre"])
        message = st.text_input("Message associé (optionnel)")

    submitted = st.form_submit_button("Ajouter")
    if submitted:
        if not nom:
            st.warning("Veuillez renseigner un nom.")
        else:
            st.session_state.family_tree.append(
                {
                    "Nom": nom.strip(),
                    "Relation": relation.strip(),
                    "Génération": generation,
                    "Message associé": message.strip(),
                }
            )
            st.success("Membre ajouté à l’arbre.")

st.markdown("---")
if st.session_state.family_tree:
    st.dataframe(st.session_state.family_tree, use_container_width=True, hide_index=True)
else:
    st.info("Aucun membre ajouté pour le moment.")

st.markdown("---")
if st.button("Retour accueil"):
    st.switch_page("app.py")
