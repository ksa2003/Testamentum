import streamlit as st

BG_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme():
    st.markdown(
        f"""
<style>

/* ---------------- GLOBAL BACKGROUND ---------------- */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.80)),
    url("{BG_URL}");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}}

html, body, [class*="css"] {{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: #FFFFFF;
}}

section.main > div {{
  max-width: 920px;
  padding-top: 2.2rem;
}}

/* ---------------- CARDS ---------------- */
.tm-card {{
  background: rgba(15,18,22,0.82);
  border: 1px solid rgba(255,255,255,0.14);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.70);
}}

.tm-title {{
  font-size: 46px;
  font-weight: 750;
  letter-spacing: -0.02em;
  background: linear-gradient(90deg, #FFFFFF 0%, #E5E7EB 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.tm-sub {{
  font-size: 14px;
  color: rgba(255,255,255,0.85);
}}

.tm-latin {{
  font-size: 13px;
  font-style: italic;
  color: rgba(255,255,255,0.70);
}}

/* ---------------- FIX ALIGNEMENT COLONNES ---------------- */
div[data-testid="column"] {{
    display: flex !important;
    align-items: stretch !important;
}}

div[data-testid="column"] > div {{
    width: 100% !important;
}}

/* ---------------- INPUTS ---------------- */
.stTextInput label,
.stTextArea label {{
    color: rgba(255,255,255,0.85) !important;
}}

.stTextInput input,
.stTextArea textarea {{
  background: rgba(0,0,0,0.45) !important;
  border: 1px solid rgba(255,255,255,0.28) !important;
  color: #FFFFFF !important;
  border-radius: 12px !important;
}}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {{
  color: rgba(255,255,255,0.55) !important;
}}

.stTextInput input:focus,
.stTextArea textarea:focus {{
  border: 1px solid rgba(255,255,255,0.70) !important;
  box-shadow: 0 0 0 3px rgba(255,255,255,0.15) !important;
  outline: none !important;
}}

input:invalid {{
  border: 1px solid rgba(255,255,255,0.28) !important;
  box-shadow: none !important;
}}

/* ---------------- BOUTONS (ALIGNEMENT PARFAIT) ---------------- */
.stButton button {{
  width: 100% !important;
  height: 50px !important;
  min-height: 50px !important;
  line-height: 50px !important;
  padding: 0 18px !important;

  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,0.22) !important;
  background: rgba(255,255,255,0.10) !important;
  color: #FFFFFF !important;
  font-weight: 650 !important;
}}

.stButton button:hover {{
  background: rgba(255,255,255,0.18) !important;
}}

.stButton button:active {{
  transform: translateY(1px);
}}

.tm-primary .stButton button {{
  background: #E5E7EB !important;
  color: #111827 !important;
  border: none !important;
}}

.tm-primary .stButton button:hover {{
  background: #F3F4F6 !important;
}}

/* ---------------- MOBILE ---------------- */
@media (max-width: 520px) {{
  .tm-title {{
    font-size: 38px;
  }}
  .tm-card {{
    padding: 22px;
  }}
}}

</style>
""",
        unsafe_allow_html=True,
)
