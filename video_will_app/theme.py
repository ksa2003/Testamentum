import streamlit as st


def apply_theme() -> None:
    """
    IMPORTANT :
    - Ne pas appeler st.set_page_config ici (sinon erreur si appelé depuis plusieurs pages).
    - Ce fichier ne fait qu'injecter du CSS global.
    """

    st.markdown(
        """
<style>
/* =============== Base =============== */
:root{
  --bg1: rgba(10, 10, 12, 0.86);
  --bg2: rgba(18, 18, 22, 0.78);
  --border: rgba(255,255,255,0.16);
  --border2: rgba(255,255,255,0.10);
  --text: rgba(255,255,255,0.92);
  --muted: rgba(255,255,255,0.72);
  --muted2: rgba(255,255,255,0.60);
  --shadow: 0 10px 30px rgba(0,0,0,0.45);
  --radius: 18px;
}

/* Fond global (tu peux garder ton image via st.image ailleurs si tu préfères) */
.stApp{
  color: var(--text);
}

/* =============== Conteneur principal =============== */
/* Réduit la transparence qui "mange" le texte, et renforce la lisibilité */
.block-container{
  padding-top: 2rem;
  padding-bottom: 3rem;
  max-width: 980px;
}

/* =============== Cartes / typographies (classes utilisées dans app.py) =============== */
.tm-card{
  background: linear-gradient(180deg, var(--bg1), var(--bg2));
  border: 1px solid var(--border2);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 22px 22px;
  backdrop-filter: blur(10px);
}

.tm-title{
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -0.6px;
  margin: 0 0 8px 0;
  color: rgba(255,255,255,0.98);
  text-shadow: 0 2px 18px rgba(0,0,0,0.55);
}

.tm-sub{
  font-size: 15px;
  color: var(--muted);
  margin-bottom: 8px;
}

.tm-latin{
  font-size: 12px;
  color: rgba(255,255,255,0.62);
  font-style: italic;
  margin-bottom: 14px;
}

.tm-h2{
  font-size: 18px;
  font-weight: 700;
  margin: 14px 0 8px 0;
  color: rgba(255,255,255,0.96);
}

.tm-h1{
  font-size: 20px;
  font-weight: 800;
  margin: 0 0 6px 0;
  color: rgba(255,255,255,0.97);
}

.tm-text{
  font-size: 14px;
  line-height: 1.55;
  color: rgba(255,255,255,0.86);
}

.tm-list{
  margin: 10px 0 0 18px;
  color: rgba(255,255,255,0.86);
}
.tm-list li{
  margin: 6px 0;
}

/* =============== Pastilles =============== */
.tm-chiprow{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 10px 0 12px 0;
}

.tm-chip{
  display: inline-flex;
  align-items: center;
  padding: 7px 12px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.22);
  background: rgba(255,255,255,0.10);
  font-size: 12px;
  color: rgba(255,255,255,0.92);
}

/* =============== Notes =============== */
.tm-footnote{
  margin-top: 10px;
  font-size: 12px;
  color: rgba(255,255,255,0.62);
}

/* =============== Inputs Streamlit =============== */
div[data-baseweb="input"] > div{
  background: rgba(10,10,14,0.55) !important;
  border: 1px solid rgba(255,255,255,0.20) !important;
  border-radius: 12px !important;
}

div[data-baseweb="input"] input{
  color: rgba(255,255,255,0.92) !important;
}

div[data-baseweb="input"] input::placeholder{
  color: rgba(255,255,255,0.45) !important;
}

/* Focus (enlève le rouge/bleu agressif) */
div[data-baseweb="input"] > div:focus-within{
  border: 1px solid rgba(255,255,255,0.34) !important;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.08) !important;
}

/* =============== Boutons =============== */
/* on rend les boutons bien visibles, et plus "solides" */
.tm-btnwrap .stButton button{
  height: 48px !important;
  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,0.20) !important;
  background: rgba(255,255,255,0.10) !important;
  color: rgba(255,255,255,0.94) !important;
  font-weight: 650 !important;
  box-shadow: 0 10px 22px rgba(0,0,0,0.25) !important;
}

.tm-btnwrap .stButton button:hover{
  background: rgba(255,255,255,0.14) !important;
  border-color: rgba(255,255,255,0.26) !important;
}

/* Variante primaire (bouton principal) */
.tm-btnwrap.tm-primary .stButton button{
  background: rgba(255,255,255,0.18) !important;
  border-color: rgba(255,255,255,0.30) !important;
}

.tm-btnwrap.tm-primary .stButton button:hover{
  background: rgba(255,255,255,0.22) !important;
}

/* Désactivé */
.tm-btnwrap .stButton button:disabled{
  opacity: 0.55 !important;
}

/* =============== Sidebar (optionnel, mais aide la lisibilité) =============== */
section[data-testid="stSidebar"]{
  background: rgba(18,18,22,0.92) !important;
  border-right: 1px solid rgba(255,255,255,0.06) !important;
}
section[data-testid="stSidebar"] *{
  color: rgba(255,255,255,0.88) !important;
}

/* =============== Mobile =============== */
@media (max-width: 480px){
  .block-container{ padding-left: 1rem; padding-right: 1rem; }
  .tm-title{ font-size: 34px; }
  .tm-card{ padding: 18px 16px; }
}
</style>
        """,
        unsafe_allow_html=True,
    )
