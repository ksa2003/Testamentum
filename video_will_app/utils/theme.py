import streamlit as st

BG_IMAGE_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme(bg_url: str = BG_IMAGE_URL) -> None:
    st.markdown(
        f"""
<style>

/* =========================================================
   BACKGROUND
========================================================= */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.82)),
    url("{bg_url}");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}}

/* =========================================================
   VARIABLES
========================================================= */
:root{{
  --card: rgba(15,18,22,0.82);
  --card2: rgba(15,18,22,0.76);
  --border: rgba(255,255,255,0.14);
  --text: #FFFFFF;
  --muted: #E6E9EE;
  --muted2: #C4CBD6;
  --accent: #EDEFF2;
  --accentHover: #FFFFFF;
  --focus: rgba(237,239,242,0.22);
  --chipBg: rgba(255,255,255,0.06);
  --inputBg: rgba(0,0,0,0.42);
  --inputBorder: rgba(255,255,255,0.26);
  --inputBorderFocus: rgba(237,239,242,0.60);
}}

/* =========================================================
   BASE
========================================================= */
html, body, [class*="css"]{{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}}

section.main > div{{
  max-width: 920px;
  padding-top: 2rem;
}}

header, footer {{visibility: hidden;}}
#MainMenu {{visibility: hidden;}}

/* =========================================================
   CARDS
========================================================= */
.tm-card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.70);
}}

.tm-card2 {{
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px 26px 26px;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.60);
}}

/* =========================================================
   TYPOGRAPHY
========================================================= */
.tm-title {{
  font-size: 46px;
  font-weight: 750;
  letter-spacing: -0.03em;
  margin: 0;
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
  margin-top: 18px;
  font-size: 24px;
  font-weight: 700;
}}

.tm-p {{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.6;
  font-size: 15px;
}}

.tm-muted {{
  margin-top: 10px;
  font-size: 12px;
  color: rgba(255,255,255,0.70);
}}

/* =========================================================
   CHIPS
========================================================= */
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
  background: var(--chipBg);
}}

/* =========================================================
   INPUTS
========================================================= */
.stTextInput label,
.stPasswordInput label {{
  color: var(--muted) !important;
}}

.stTextInput input,
.stPasswordInput input {{
  background: var(--inputBg) !important;
  border: 1px solid var(--inputBorder) !important;
  color: var(--text) !important;
  border-radius: 12px !important;
  padding: 0.8rem 1rem !important;
  caret-color: var(--text) !important;
}}

.stTextInput input::placeholder,
.stPasswordInput input::placeholder {{
  color: rgba(255,255,255,0.50) !important;
}}

.stTextInput input:focus,
.stPasswordInput input:focus {{
  border: 1px solid var(--inputBorderFocus) !important;
  box-shadow: 0 0 0 3px var(--focus) !important;
  outline: none !important;
}}

input:invalid {{
  border: 1px solid var(--inputBorder) !important;
  box-shadow: none !important;
  outline: none !important;
}}

/* =========================================================
   BUTTONS
========================================================= */
.stButton button,
div[data-testid="stFormSubmitButton"] button {{
  width: 100% !important;
  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,0.20) !important;
  background: rgba(255,255,255,0.08) !important;
  color: var(--text) !important;
  font-weight: 650 !important;
  height: 50px !important;
}}

.stButton button:hover,
div[data-testid="stFormSubmitButton"] button:hover {{
  background: rgba(255,255,255,0.14) !important;
}}

.stButton button:active,
div[data-testid="stFormSubmitButton"] button:active {{
  transform: translateY(1px);
}}

.stButton button:focus-visible,
div[data-testid="stFormSubmitButton"] button:focus-visible {{
  box-shadow: 0 0 0 3px var(--focus) !important;
  outline: none !important;
}}

button[kind="primary"] {{
  background: var(--accent) !important;
  color: #0b0f16 !important;
  border: none !important;
}}

button[kind="primary"]:hover {{
  background: var(--accentHover) !important;
}}

/* =========================================================
   ALIGNMENT FIX
========================================================= */
div[data-testid="stHorizontalBlock"] {{
  align-items: stretch !important;
}}

div[data-testid="column"] {{
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-end !important;
}}

div[data-testid="stFormSubmitButton"] {{
  margin: 0 !important;
  padding: 0 !important;
}}

/* =========================================================
   ALERTS (neutral style)
========================================================= */
div[data-testid="stAlert"] {{
  border-radius: 14px !important;
  border: 1px solid rgba(255,255,255,0.16) !important;
  background: rgba(15,18,22,0.70) !important;
}}

div[data-testid="stAlert"] * {{
  color: rgba(255,255,255,0.92) !important;
}}

/* =========================================================
   REMOVE BLACK BAR UNDER TABS
========================================================= */
div[data-baseweb="tab-border"] {{
  display: none !important;
}}

div[data-baseweb="tab-highlight"] {{
  background: rgba(255,255,255,0.15) !important;
  height: 2px !important;
}}

div[data-baseweb="tab"] {{
  background: transparent !important;
  border: none !important;
}}

@media (max-width: 520px) {{
  .tm-title {{ font-size: 38px; }}
}}

</style>
""",
        unsafe_allow_html=True,
)
