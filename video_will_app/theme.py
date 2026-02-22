import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme():
    st.set_page_config(page_title="Testamentum", page_icon="⚖️", layout="centered")

    st.markdown(
        f"""
<style>

/* ---------------- Background ---------------- */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,0.70), rgba(0,0,0,0.80)),
    url("{BG_URL}");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}}

/* ---------------- Variables ---------------- */
:root{{
  --card: rgba(15,18,22,0.82);
  --border: rgba(255,255,255,0.14);
  --text: #FFFFFF;

  /* Plus clair qu'avant */
  --muted: rgba(255,255,255,0.82);
  --muted2: rgba(255,255,255,0.70);

  --inputBg: rgba(0,0,0,0.45);
  --inputBorder: rgba(255,255,255,0.26);

  --accent: #E5E7EB;
  --accentHover: #F3F4F6;
  --focus: rgba(255,255,255,0.22);
}}

/* ---------------- Base typography ---------------- */
html, body, [class*="css"] {{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}}

section.main > div {{
  max-width: 920px;
  padding-top: 2.2rem;
}}

/* ---------------- Cards ---------------- */
.tm-card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.70);
}}

.tm-title {{
  font-size: 46px;
  margin: 0;
  font-weight: 750;
  letter-spacing: -0.03em;
  background: linear-gradient(90deg, #FFFFFF 0%, #E5E7EB 50%, #FFFFFF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.tm-sub {{
  margin-top: 10px;
  font-size: 14px;
  color: var(--muted);
}}

.tm-latin {{
  margin-top: 6px;
  font-size: 13px;
  font-style: italic;
  color: var(--muted2);
}}

.tm-h2 {{
  margin-top: 22px;
  font-size: 24px;
  font-weight: 700;
}}

.tm-p {{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.65;
  font-size: 15px;
}}

.tm-bullets {{
  margin-top: 14px;
  color: var(--muted);
  line-height: 1.85;
  font-size: 14px;
}}

.tm-muted {{
  margin-top: 12px;
  font-size: 12px;
  color: var(--muted2);
}}

/* ---------------- Chips ---------------- */
.tm-chiprow {{
  margin-top: 14px;
  display:flex;
  gap:8px;
  flex-wrap:wrap;
}}

.tm-chip {{
  border: 1px solid var(--border);
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 12px;
  color: var(--muted);
  background: rgba(255,255,255,0.06);
}}

/* ---------------- Labels / captions (plus lisibles) ---------------- */
label, .stMarkdown, .stCaption, .stText {{
  color: var(--muted) !important;
}}

/* ---------------- Inputs ---------------- */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {{
  background: var(--inputBg) !important;
  border: 1px solid var(--inputBorder) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
}}

/* Placeholders plus visibles */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {{
  color: rgba(255,255,255,0.55) !important;
}}

/* Focus : enlever rouge/bleu, mettre blanc doux */
.stTextInput input:focus,
.stTextArea textarea:focus {{
  border: 1px solid rgba(255,255,255,0.70) !important;
  box-shadow: 0 0 0 3px var(--focus) !important;
  outline: none !important;
}}

/* Désactiver bordures rouges "invalid" */
input:invalid {{
  border: 1px solid var(--inputBorder) !important;
  box-shadow: none !important;
}}

/* ---------------- Buttons : même hauteur partout ---------------- */
.stButton button {{
  width: 100%;
  border-radius: 999px !important;

  /* clé pour l’alignement */
  min-height: 46px !important;
  height: 46px !important;
  line-height: 46px !important;
  padding: 0 18px !important;

  border: 1px solid rgba(255,255,255,0.22) !important;
  background: rgba(255,255,255,0.10) !important;
  color: var(--text) !important;
  font-weight: 650 !important;
}}

.stButton button:hover {{
  background: rgba(255,255,255,0.18) !important;
}}

.stButton button:active {{
  transform: translateY(1px);
}}

/* Bouton "primary" */
.tm-primary .stButton button {{
  background: var(--accent) !important;
  color: #111827 !important;
  border: none !important;
}}

.tm-primary .stButton button:hover {{
  background: var(--accentHover) !important;
}}

/* ---------------- Streamlit alert boxes : rendre lisible ---------------- */
div[data-testid="stAlert"] {{
  border-radius: 14px !important;
  border: 1px solid rgba(255,255,255,0.14) !important;
}}

/* ---------------- Remove weird extra spacing under headings ---------------- */
h1, h2, h3 {{
  letter-spacing: -0.02em;
}}

/* ---------------- Mobile ---------------- */
@media (max-width: 520px){{
  .tm-title{{ font-size: 38px; }}
  .tm-card{{ padding: 22px; }}
}}

</style>
        """,
        unsafe_allow_html=True,
)
