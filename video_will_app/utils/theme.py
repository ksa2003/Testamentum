import streamlit as st

BG_IMAGE_URL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?q=80&w=1920&auto=format&fit=crop"

def apply_theme(background_url: str = BG_IMAGE_URL) -> None:
    st.markdown(
        f"""
<style>
/* --------- Background --------- */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,0.68), rgba(0,0,0,0.78)),
    url("{background_url}");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}}

/* --------- Variables --------- */
:root {{
  --card: rgba(15,18,22,0.78);
  --card2: rgba(15,18,22,0.62);
  --border: rgba(255,255,255,0.14);
  --text: rgba(255,255,255,0.94);
  --muted: rgba(255,255,255,0.78);
  --muted2: rgba(255,255,255,0.62);
  --chipbg: rgba(255,255,255,0.06);

  --btn: rgba(255,255,255,0.12);
  --btnHover: rgba(255,255,255,0.18);
  --btnPrimaryBg: rgba(255,255,255,0.92);
  --btnPrimaryText: rgba(0,0,0,0.92);

  --focus: rgba(255,255,255,0.22);
}}

/* --------- Base --------- */
html, body, [class*="css"] {{
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial;
  color: var(--text);
}}

section.main > div {{
  max-width: 920px;
  padding-top: 2.2rem;
}}

/* --------- Card --------- */
.tm-card {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 26px;
  backdrop-filter: blur(20px);
  box-shadow: 0 22px 100px rgba(0,0,0,0.7);
  animation: fadeIn 0.55s ease-out;
}}

.tm-card2 {{
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 22px;
  backdrop-filter: blur(16px);
}}

@keyframes fadeIn {{
  from {{opacity:0; transform: translateY(10px);}}
  to {{opacity:1; transform: translateY(0);}}
}}

/* --------- Typography --------- */
.tm-title {{
  font-size: 46px;
  margin: 0;
  font-weight: 750;
  letter-spacing: -0.03em;
  background: linear-gradient(90deg, rgba(255,255,255,0.98) 0%, rgba(229,231,235,0.95) 50%, rgba(255,255,255,0.98) 100%);
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
  font-size: 22px;
  font-weight: 700;
  color: rgba(255,255,255,0.93);
}}

.tm-p {{
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.7;
  font-size: 15px;
}}

.tm-bullets {{
  margin-top: 14px;
  color: var(--muted);
  line-height: 1.95;
  font-size: 14px;
}}

.tm-videos-title {{
  font-size: 20px;
  font-weight: 750;
  color: rgba(255,255,255,0.94);
  margin-top: 18px;
  margin-bottom: 10px;
  text-shadow: 0 2px 16px rgba(0,0,0,0.55);
}}

/* --------- Chips --------- */
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
  background: var(--chipbg);
}}

/* --------- Inputs --------- */
.stTextInput label, .stTextArea label, .stFileUploader label {{
  color: var(--muted) !important;
}}

.stTextInput input, .stTextArea textarea {{
  background: rgba(0,0,0,0.42) !important;
  border: 1px solid rgba(255,255,255,0.26) !important;
  color: rgba(255,255,255,0.94) !important;
  border-radius: 12px !important;
  padding: 0.80rem 1rem !important;
  caret-color: rgba(255,255,255,0.92) !important;
  outline: none !important;
  box-shadow: none !important;
}}

.stTextInput input::placeholder, .stTextArea textarea::placeholder {{
  color: rgba(255,255,255,0.45) !important;
}}

.stTextInput input:focus, .stTextArea textarea:focus {{
  border: 1px solid rgba(255,255,255,0.45) !important;
  box-shadow: 0 0 0 3px var(--focus) !important;
  outline: none !important;
}}

/* Supprime le rouge "invalid" (mobile/Chrome) */
input:invalid {{
  box-shadow: none !important;
  outline: none !important;
  border: 1px solid rgba(255,255,255,0.26) !important;
}}

/* --------- Buttons: ALIGNMENT + NO BLUE/RED --------- */
/* Fix Streamlit extra paddings inside columns for consistent baseline */
div[data-testid="stHorizontalBlock"] > div {{
  align-items: stretch !important;
}}

/* Uniform button style */
.stButton > button {{
  width: 100%;
  border-radius: 999px !important;
  padding: 0.95rem 1.2rem !important;
  border: 1px solid rgba(255,255,255,0.22) !important;
  background: var(--btn) !important;
  color: rgba(255,255,255,0.92) !important;
  font-weight: 650 !important;
  height: 52px !important;            /* IMPORTANT: same height */
  line-height: 52px !important;       /* IMPORTANT: same baseline */
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  outline: none !important;
  box-shadow: none !important;
}}

.stButton > button:hover {{
  background: var(--btnHover) !important;
  border-color: rgba(255,255,255,0.26) !important;
}}

.stButton > button:focus,
.stButton > button:active,
.stButton > button:focus-visible {{
  outline: none !important;
  box-shadow: 0 0 0 3px var(--focus) !important;
  border-color: rgba(255,255,255,0.36) !important;
}}

/* Primary button wrapper */
.tm-primary .stButton > button {{
  background: var(--btnPrimaryBg) !important;
  color: var(--btnPrimaryText) !important;
  border: none !important;
}}

.tm-primary .stButton > button:hover {{
  background: rgba(255,255,255,0.98) !important;
}}

/* Streamlit success/info/warn colors toned down for theme */
.stAlert {{
  border-radius: 14px !important;
  backdrop-filter: blur(10px);
}}

.tm-muted {{
  margin-top: 12px;
  font-size: 12px;
  color: rgba(255,255,255,0.70);
}}

@media (max-width: 520px) {{
  .tm-title{{ font-size: 38px; }}
  .tm-card{{ padding: 22px; }}
}}
</style>
""",
        unsafe_allow_html=True,
)
