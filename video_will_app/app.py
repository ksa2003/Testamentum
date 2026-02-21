import streamlit as st

st.set_page_config(page_title="Testamentum", page_icon="🎬", layout="wide")

# ---------------------------------------------------
# CONFIG VISUELLE
# ---------------------------------------------------
HERO_BG = "https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?auto=format&fit=crop&w=2400&q=70"
LOGO_TEXT = "TESTAMENTUM"

# ---------------------------------------------------
# CSS + HERO (IMPORTANT: unsafe_allow_html=True)
# ---------------------------------------------------
st.markdown(
    f"""
    <style>
      /* Hide Streamlit UI to look like a real website */
      #MainMenu {{ visibility: hidden; }}
      footer {{ visibility: hidden; }}
      header {{ visibility: hidden; }}

      /* Kill Streamlit sidebar spacing */
      [data-testid="stSidebar"] {{ display:none; }}

      .stApp {{
        background: #000;
      }}

      section.main > div {{
        padding: 0 !important;
        max-width: 100% !important;
      }}

      .hero {{
        position: relative;
        min-height: 100vh;
        background-image:
          linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.88)),
          url("{HERO_BG}");
        background-size: cover;
        background-position: center;
        padding: 28px 18px;
      }}

      .nav {{
        display:flex;
        align-items:center;
        justify-content:space-between;
        max-width: 1120px;
        margin: 0 auto;
      }}

      .logo {{
        font-weight: 900;
        letter-spacing: 0.06em;
        color: #E50914;
        font-size: 1.35rem;
      }}

      .navright {{
        display:flex;
        gap: 10px;
        align-items:center;
      }}

      .pill {{
        border: 1px solid rgba(255,255,255,0.18);
        background: rgba(0,0,0,0.35);
        color: rgba(255,255,255,0.88);
        padding: 8px 12px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.92rem;
        backdrop-filter: blur(6px);
      }}

      .hero-inner {{
        max-width: 1120px;
        margin: 0 auto;
        padding-top: 70px;
        display:grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 24px;
      }}

      @media (max-width: 900px) {{
        .hero-inner {{
          grid-template-columns: 1fr;
          padding-top: 38px;
        }}
      }}

      .h1 {{
        color: #fff;
        font-weight: 900;
        font-size: clamp(2.1rem, 4vw, 3.2rem);
        line-height: 1.05;
        margin: 0 0 14px 0;
      }}

      .lead {{
        color: rgba(255,255,255,0.86);
        font-size: 1.08rem;
        line-height: 1.55;
        margin: 0 0 18px 0;
        max-width: 60ch;
      }}

      .bullets {{
        color: rgba(255,255,255,0.78);
        font-size: 1.02rem;
        line-height: 1.6;
        margin-top: 10px;
      }}

      .card {{
        background: rgba(0,0,0,0.58);
        border: 1px solid rgba(255,255,255,0.14);
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 18px 40px rgba(0,0,0,0.45);
        backdrop-filter: blur(10px);
      }}

      .card h3 {{
        color: #fff;
        margin: 0 0 8px 0;
        font-size: 1.1rem;
        font-weight: 900;
      }}

      .muted {{
        color: rgba(255,255,255,0.74);
        font-size: 0.98rem;
        margin: 0 0 12px 0;
        line-height: 1.55;
      }}

      /* Streamlit input overrides inside hero */
      .stTextInput input {{
        background: rgba(0,0,0,0.35) !important;
        border: 1px solid rgba(255,255,255,0.22) !important;
        color: #fff !important;
        border-radius: 12px !important;
        padding: 0.85rem 0.9rem !important;
      }}
      .stTextInput label {{
        color: rgba(255,255,255,0.80) !important;
        font-weight: 800 !important;
      }}

      .stButton button {{
        background: #E50914 !important;
        color: #fff !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.85rem 1.0rem !important;
        font-weight: 900 !important;
        width: 100%;
      }}
      .stButton button:hover {{
        background: #f6121d !important;
      }}

      .fineprint {{
        color: rgba(255,255,255,0.55);
        font-size: 0.86rem;
        margin-top: 10px;
        line-height: 1.4;
      }}
    </style>

    <div class="hero">
      <div class="nav">
        <div class="logo">{LOGO_TEXT}</div>
        <div class="navright">
          <div class="pill">Sécurité</div>
          <div class="pill">Confidentialité</div>
          <div class="pill">Traçabilité</div>
        </div>
      </div>

      <div class="hero-inner">
        <div>
          <div class="h1">Votre message vidéo, transmis au bon moment.</div>

          <div class="lead">
            Testamentum est un coffre sécurisé permettant d’enregistrer un testament émotionnel en vidéo,
            et de contrôler précisément l’accès des bénéficiaires lorsque le décès est déclaré.
          </div>

          <div class="bullets">
            • Accès par jeton temporaire pour les bénéficiaires<br/>
            • Validation possible par notaire (workflow métier)<br/>
            • Stockage cloud et journalisation des actions (MVP)
          </div>

          <div style="height:14px;"></div>

          <div class="card">
            <h3>Commencer</h3>
            <p class="muted">Saisissez votre adresse e-mail pour créer un compte ou vous connecter.</p>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# CTA (Streamlit widgets)
# ---------------------------------------------------
email = st.text_input("Adresse e-mail", placeholder="votre-email@exemple.com")

if st.button("Continuer"):
    st.session_state["prefill_email"] = email.strip()
    st.switch_page("pages/1_Connexion.py")

# ---------------------------------------------------
# Bloc droite + footer hero
# ---------------------------------------------------
st.markdown(
    """
            <div class="fineprint">
              En continuant, vous acceptez les conditions d’utilisation et la politique de confidentialité (MVP).
            </div>
          </div>
        </div>

        <div>
          <div class="card">
            <h3>Pourquoi ce service existe ?</h3>
            <p class="muted">
              Pour laisser un message clair, humain et structuré à vos proches, avec une transmission respectueuse,
              sécurisée et traçable.
            </p>

            <div class="bullets">
              • Interface simple, accessible mondialement<br/>
              • Séparation des rôles (propriétaire / bénéficiaire / notaire)<br/>
              • Architecture évolutive (EU/US/Asie) à venir
            </div>
          </div>
        </div>

      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
