# app.py
# Page d’accueil Kidan Vid (Streamlit)
# - Logo grand (pleine largeur)
# - Pitch + bullets + 2 boutons
# - Sections complètes (Comment ça marche, Pourquoi, Cas d’usage, Offres, Sécurité, Notaire en ligne, FAQ)
# - Bloc Connexion placé tout en bas de "Comment ça marche"
# - Sidebar moins large (mobile-friendly)
# - Chargement d’images robuste (évite le TypeError st.image)

from __future__ import annotations

from pathlib import Path
from typing import Optional

import streamlit as st
from PIL import Image


# =========================
# Configuration
# =========================
st.set_page_config(page_title="Kidan Vid", layout="wide")

# CSS: limiter la sidebar (évite qu’elle prenne toute la place sur mobile)
st.markdown(
    """
<style>
/* Sidebar plus étroite */
section[data-testid="stSidebar"]{
  width: 280px !important;
  min-width: 280px !important;
}

/* Un peu d’air */
.block-container { padding-top: 1.2rem; }

/* Boutons un peu plus visibles */
div.stButton > button {
  padding: 0.6rem 1rem;
  border-radius: 10px;
}
</style>
""",
    unsafe_allow_html=True,
)

APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"

LOGO_PATHS = [
    ASSETS_DIR / "logo_kidan_vid.png",         # recommandé (vu dans ton repo)
    ASSETS_DIR / "logo_kidan_vid.jpg",
    ASSETS_DIR / "logo_kidan_vid.webp",
]


# =========================
# Helpers
# =========================
def find_first_existing(paths: list[Path]) -> Optional[Path]:
    for p in paths:
        if p.exists() and p.is_file():
            return p
    return None


def show_image_if_exists(
    path: Path | str,
    *,
    caption: Optional[str] = None,
    use_container_width: bool = True,
    width: Optional[int] = None,
) -> bool:
    """
    Affiche une image si elle existe.
    Evite l’erreur TypeError en n’envoyant PAS width + use_container_width ensemble.
    Utilise PIL pour être robuste avec les formats.
    """
    p = Path(path)
    if not p.exists():
        return False

    img = Image.open(p)
    if use_container_width:
        st.image(img, caption=caption, use_container_width=True)
    else:
        if width is None:
            st.image(img, caption=caption)
        else:
            st.image(img, caption=caption, width=width)
    return True


def switch_page_safe(page_label: str, page_file: str) -> None:
    """
    Essaie de naviguer vers une page multipage Streamlit.
    - page_file: ex "pages/Connexion.py"
    - page_label: texte utilisateur
    """
    try:
        st.switch_page(page_file)  # Streamlit multipage
    except Exception:
        st.info(
            f"Navigation vers « {page_label} » indisponible ici. "
            f"Assure-toi que le fichier existe: {page_file}"
        )


# =========================
# Sidebar (raccourcis)
# =========================
with st.sidebar:
    st.markdown("### Kidan Vid")
    st.caption("Plateforme de transmission vidéo sécurisée.")

    if st.button("Accueil"):
        st.session_state["_scroll"] = "top"
    if st.button("Comment ça marche"):
        st.session_state["_scroll"] = "how"
    if st.button("Créer un envoi sécurisé"):
        switch_page_safe("Créer un envoi sécurisé", "pages/Creer_un_envoi_securise.py")
    if st.button("Connexion"):
        switch_page_safe("Connexion", "pages/Connexion.py")
    if st.button("Notaire en ligne"):
        switch_page_safe("Notaire en ligne", "pages/Notaire_en_ligne.py")


# =========================
# Header / Logo (grand)
# =========================
st.markdown('<a id="top"></a>', unsafe_allow_html=True)

logo = find_first_existing(LOGO_PATHS)
if logo:
    show_image_if_exists(logo, use_container_width=True)
else:
    st.warning("Logo introuvable dans /assets (ex: assets/logo_kidan_vid.png).")

# =========================
# Pitch principal
# =========================
st.markdown("## Envoyez des vidéos personnelles en toute confidentialité.")
st.write(
    "La première plateforme sécurisée qui permet d’envoyer une vidéo privée à une personne, "
    "accessible uniquement par elle, lorsque vous reposez en paix."
)

colA, colB, colC, colD = st.columns(4)
with colA:
    st.write("100% sécurisé")
with colB:
    st.write("Accès unique et contrôlé")
with colC:
    st.write("Programmation possible")
with colD:
    st.write("Accessible partout")

btn1, btn2 = st.columns([1, 1])
with btn1:
    if st.button("Découvrir comment ça marche"):
        st.session_state["_scroll"] = "how"
with btn2:
    if st.button("Créer un envoi sécurisé"):
        switch_page_safe("Créer un envoi sécurisé", "pages/Creer_un_envoi_securise.py")

st.divider()

# =========================
# Comment ça marche
# =========================
st.markdown('<a id="how"></a>', unsafe_allow_html=True)
st.markdown("## Comment ça marche ?")

st.markdown("**I. Vous téléchargez votre vidéo**")
st.write("Format sécurisé, cryptage immédiat.")

st.markdown("**II. Vous identifiez le destinataire**")
st.write("Email + téléphone + vérification d’identité.")

st.markdown("**III. Nous sécurisons l’accès**")
st.write("Code unique + double authentification (2FA).")

st.markdown("**IV. Le destinataire reçoit la vidéo (timing)**")
st.write("Accès personnel, protégé et traçable.")

# --- Connexion en bas de la section "Comment ça marche"
st.markdown("---")
st.markdown("### Connexion")

email = st.text_input("Adresse e-mail", placeholder="votre@email.com", key="home_email")
c1, c2 = st.columns([1, 1])
with c1:
    if st.button("Continuer", key="home_continue"):
        # Si tu veux forcer la page Connexion
        switch_page_safe("Connexion", "pages/Connexion.py")
with c2:
    if st.button("Accès bénéficiaire", key="home_benef"):
        switch_page_safe("Accès bénéficiaire", "pages/Acces_beneficiaire.py")

st.divider()

# =========================
# Pourquoi Kidan Vid ?
# =========================
st.markdown("## Pourquoi Kidan Vid ?")
st.markdown(
    """
- Cryptage de bout en bout
- Vidéo non téléchargeable
- Accès limité dans le temps
- Traçabilité des ouvertures
- Option "visionnage unique"
- Hébergement sécurisé conforme RGPD
"""
)

st.divider()

# =========================
# Cas d’usage
# =========================
st.markdown("## Cas d’usage")
st.markdown(
    """
- Messages personnels confidentiels
- Transmission de souvenirs familiaux
- Messages importants programmés
- Communication sensible
- Transmission patrimoniale numérique
"""
)

st.divider()

# =========================
# Nos offres
# =========================
st.markdown("## Nos offres")
st.markdown(
    """
- Abonnement mensuel
- Abonnement annuel
- Envoi unique premium
"""
)

st.divider()

# =========================
# Infos sécurité maximale (à collecter)
# =========================
st.markdown("## Informations à collecter pour une sécurité maximale")
st.write("Objectif : protéger l’expéditeur, le destinataire et la plateforme.")

st.markdown("### Informations demandées à l’abonné (expéditeur)")
st.markdown("**Identité vérifiée (KYC simplifié) – Obligatoire :**")
st.markdown(
    """
- Nom complet
- Date de naissance
- Pièce d’identité (vérification automatique)
- Email vérifié
- Numéro de téléphone vérifié (SMS OTP)
- Pays de résidence
- Adresse IP enregistrée
"""
)
st.markdown("**Pour formule premium :**")
st.markdown(
    """
- Pièce d’identité (vérification automatique)
- Selfie vidéo de validation
"""
)

st.markdown("### Sécurité compte")
st.markdown(
    """
- Mot de passe fort obligatoire
- Double authentification (2FA)
- Question secrète
- Code de récupération
"""
)

st.markdown("### Informations demandées pour le destinataire")
st.markdown("**Minimum requis :**")
st.markdown(
    """
- Nom complet
- Nom complet de ses parents
- Information sur sa famille (frère, sœur, cousin, cousine, tante, oncle si besoin)
- Email
- Numéro de téléphone
- Pays
- Adresse (localité)
"""
)

st.markdown("**Sécurité renforcée :**")
st.markdown(
    """
- Question secrète personnalisée
- Code OTP envoyé par SMS
- Lien à usage unique
- Date limite d’accès
- Limitation nombre de visionnages
- Option reconnaissance faciale (premium)
"""
)

st.divider()

# =========================
# Notaire en ligne (GLOBAL, sans NY)
# =========================
st.markdown("## Notaire en ligne")

st.markdown("### Pourquoi utiliser un notaire en ligne ?")
st.markdown(
    """
**Commodité**  
Obtenir des documents notariés à distance avec un notaire public via mobile ou webcam.

**Vitesse**  
Une séance moyenne ne prend pas plus de 5 à 10 minutes.

**Sécurité**  
Documents scellés numériquement pour se protéger contre la fraude et l'altération.

**Facilité d'utilisation**  
Cliquez sur un lien pour rejoindre la session de notaire via téléphone ou navigateur.
"""
)

st.markdown("### Questions fréquentes sur le notaire en ligne")
st.markdown(
    """
**Sécurité technique indispensable**
- Chiffrement AES-256 des vidéos
- Chiffrement SSL/TLS
- Hébergement conforme RGPD (selon région)
- Logs d’accès horodatés
- Suppression automatique après X jours dès le premier visionnage (options premium)
- Blocage capture écran (si possible techniquement)
- Filigrane invisible personnalisé
"""
)

st.markdown("### Formulaires courants")
st.write("Modèles que vous pouvez remplir et notarier en ligne.")

st.markdown("### Par insertion de texte et possibilité d’écrire")
st.write("Interface permettant de compléter des formulaires et d’écrire directement dans les documents.")

st.divider()

# =========================
# Scroll automatique (si bouton sidebar)
# =========================
# Note: Streamlit ne scroll pas nativement, mais on peut aider avec un petit JS simple.
# Ça marche sur la plupart des navigateurs.
scroll_target = st.session_state.pop("_scroll", None)
if scroll_target in ("top", "how"):
    anchor = scroll_target
    st.components.v1.html(
        f"""
<script>
  const el = window.parent.document.querySelector('a[id="{anchor}"]');
  if (el) el.scrollIntoView({{behavior: "smooth"}});
</script>
""",
        height=0,
)
