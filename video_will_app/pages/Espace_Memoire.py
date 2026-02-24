import streamlit as st
from theme import apply_theme
from supabase import create_client, Client

apply_theme()

SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def main():
    user = st.session_state.get("user")
    if not user:
        st.switch_page("app.py")

    st.markdown(
        f"""
        <div class="tm-card">
          <div class="tm-h2">Espace Mémoire</div>
          <div class="tm-sub" style="margin-top:6px;">Votre espace personnel de messages et de transmission</div>
          <div class="tm-latin" style="margin-top:6px;">Connecté : {user.email}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown('<div class="tm-card2"><div class="tm-h3">Créer un message vidéo</div></div>', unsafe_allow_html=True)
    title = st.text_input("Titre du message", placeholder="Ex : Pour ma famille")
    video = st.file_uploader("Sélectionner une vidéo", type=["mp4", "mov", "webm", "mpeg4"])

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
        upload = st.button("Téléverser")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        manage = st.button("Gérer les bénéficiaires")

    st.write("")
    st.markdown('<div class="tm-card2"><div class="tm-h3">Bénéficiaires</div><div class="tm-muted" style="margin-top:6px;">Ajoutez les personnes autorisées à recevoir l’accès au message.</div></div>', unsafe_allow_html=True)

    name = st.text_input("Nom complet", placeholder="Ex : Marie Dupont")
    email = st.text_input("Email (optionnel)", placeholder="Ex : marie@email.com")
    relation = st.text_input("Lien (optionnel)", placeholder="Ex : sœur, ami, conjoint")

    st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
    add = st.button("Ajouter")
    st.markdown("</div>", unsafe_allow_html=True)

    st.info("Aucun bénéficiaire ajouté pour l’instant.")

    st.write("")
    st.markdown('<div class="tm-card2"><div class="tm-h3">Vos messages</div><div class="tm-muted" style="margin-top:6px;">Vous retrouverez ici vos messages enregistrés.</div></div>', unsafe_allow_html=True)
    st.info("Aucun message pour l’instant (MVP).")

    st.write("")
    logout = st.button("Se déconnecter")
    if logout:
        st.session_state.pop("user", None)
        st.switch_page("app.py")

    if upload:
        if not title.strip():
            st.error("Veuillez saisir un titre.")
        elif not video:
            st.error("Veuillez sélectionner une vidéo.")
        else:
            st.success("Vidéo prête à être téléversée (MVP).")

    if manage:
        st.info("Gestion des bénéficiaires (MVP).")

    if add:
        if not name.strip():
            st.error("Le nom du bénéficiaire est obligatoire.")
        else:
            st.success("Bénéficiaire ajouté (MVP).")


if __name__ == "__main__":
    main()
