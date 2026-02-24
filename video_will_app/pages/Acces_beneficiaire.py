import streamlit as st
from theme import apply_theme

apply_theme()


def main():
    st.markdown(
        """
        <div class="tm-card">
          <div class="tm-title">Kidan Vid</div>
          <div class="tm-sub">Accès bénéficiaire</div>
          <div class="tm-latin">Consultez un message qui vous a été destiné (via lien ou jeton).</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    token = st.text_input("Jeton d’accès", placeholder="Ex : KIDAN-XXXX-XXXX")
    st.markdown('<div class="tm-muted" style="margin-top:-6px;">Le jeton est fourni par le déposant.</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div class="tm-primary">', unsafe_allow_html=True)
        go = st.button("Accéder")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        back = st.button("Retour")

    if go:
        if not token.strip():
            st.error("Veuillez saisir un jeton d’accès.")
        else:
            st.success("Jeton reçu. (MVP) Ici, vous chargerez la vidéo associée au jeton.")

    if back:
        st.switch_page("app.py")


if __name__ == "__main__":
    main()
