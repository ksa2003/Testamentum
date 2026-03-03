# video_will_app/app.py
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import streamlit as st
from PIL import Image


# -----------------------------
# Config
# -----------------------------
st.set_page_config(
    page_title="Kidan Vid",
    page_icon="🎥",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# Chemin logo (ton fichier : assets/logo_kidan_vid.png)
LOGO_PATH = ASSETS_DIR / "logo_kidan_vid.png"


# -----------------------------
# Helpers
# -----------------------------
def st_image_compat(img, caption: Optional[str] = None, use_full_width: bool = True, width: Optional[int] = None):
    """
    Compat Streamlit:
    - versions récentes: use_container_width
    - versions anciennes: use_column_width
    """
    try:
        st.image(img, caption=caption, use_container_width=use_full_width, width=width)
    except TypeError:
        # fallback anciennes versions Streamlit
        st.image(img, caption=caption, use_column_width=use_full_width, width=width)


def show_image_if_exists(path: Path, caption: Optional[str] = None, use_full_width: bool = True, width: Optional[int] = None):
    if not path.exists():
        st.warning(f"Image introuvable : {path.as_posix()}")
        return

    try:
        img = Image.open(path)
        st_image_compat(img, caption=caption, use_full_width=use_full_width, width=width)
    except Exception as e:
        st.error(f"Erreur lecture image {path.name} : {e}")


def go_to(page_name: str):
    """
    Navigation multi-pages Streamlit Cloud.
    page_name doit correspondre au slug Streamlit:
    ex: 'Connexion' -> '/Connexion' si le fichier pages s'appelle Connexion.py
    """
    try:
        st.switch_page(f"pages/{page_name}.py")
    except Exception:
        # fallback: lien cliquable si switch_page indisponible
        st.markdown(f"[Ouvrir {page_name}](/{page_name})")


# -----------------------------
# UI
# -----------------------------
# Un peu de CSS pour une page d'accueil plus "site"
st.markdown(
    """
    <style>
      .block-container { padding-top: 1.2rem; }
      .kv-hero h1 { font-size: 2.1rem; margin-bottom: 0.4rem; }
      .kv-hero p { font-size: 1.05rem; margin-top: 0.2rem; color: #444; }
      .kv-bullets li { margin-bottom: 0.25rem; }
      .kv-card {
        border: 1px solid rgba(0,0,0,0.08);
        border-radius: 16px;
        padding: 18px;
        background: rgba(255,255,255,0.75);
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo grand en haut
show_image_if_exists(LOGO_PATH, use_full_width=True)

st.markdown(
    """
    <div class="kv-hero">
      <h1>Kidan Vid</h1>
      <p><b>Plateforme de transmission vidéo sécurisée.</b></p>
      <p>
        Envoyez des vidéos personnelles en toute confidentialité.
        La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne,
        accessible uniquement par elle, lorsque vous reposez en paix.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

colA, colB = st.columns([1.1, 0.9], gap="large")

with colA:
    st.markdown("<div class='kv-card'>", unsafe_allow_html=True)
    st.markdown("### Points clés")
    st.markdown(
        """
        <ul class="kv-bullets">
          <li>100% sécurisé</li>
          <li>Accès unique et contrôlé</li>
          <li>Programmation possible</li>
          <li>Accessible partout</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("Découvrir comment ça marche", use_container_width=True):
            # ton menu contient déjà "Comment ca marche"
            go_to("Comment_ca_marche")
    with b2:
        if st.button("Créer un envoi sécurisé", use_container_width=True):
            go_to("Creer_un_envoi_securise")
    with b3:
        if st.button("Se connecter", use_container_width=True):
            go_to("Connexion")

    st.markdown("</div>", unsafe_allow_html=True)

with colB:
    st.markdown("<div class='kv-card'>", unsafe_allow_html=True)
    st.markdown("### Comment ça marche ?")
    st.markdown(
        """
        **I. Vous téléchargez votre vidéo**  
        Format sécurisé, cryptage immédiat.

        **II. Vous identifiez le destinataire**  
        Email + téléphone + vérification d’identité.

        **III. Nous sécurisons l’accès**  
        Code unique + double authentification.

        **IV. Le destinataire reçoit la vidéo (timing)**  
        Accès personnel, protégé et traçable.
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# Footer simple
st.caption("© Kidan Vid — Prototype Streamlit")
