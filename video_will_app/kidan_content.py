# kidan_content.py
from dataclasses import dataclass
from typing import List, Dict

# Dossier assets (relatif au projet)
ASSETS_DIR = "assets"

# Mapping officiel des images (noms à mettre dans /assets)
ASSET_FILES: Dict[str, str] = {
    "cover": "01_cover.png",
    "marche_opportunite": "02_marche_opportunite.png",
    "vision": "03_vision.png",
    "modele_economique": "04_modele_economique.png",
    "positionnement_strategique": "05_positionnement_strategique.png",
    "accroche_principale": "06_accroche_principale.png",
    "constat_humain": "07_constat_humain.png",
    "pilier_juridique": "08_pilier_juridique.png",
    "pilier_transmission": "09_pilier_transmission.png",
    "infrastructure_blocs": "10_infrastructure_blocs.png",
    "modele_3_niveaux": "11_modele_3_niveaux.png",
    "alliance": "12_alliance.png",
    "reference_mondiale": "13_reference_mondiale.png",
    "solution": "14_solution.png",
    "constat_humain_detail": "15_constat_humain_detail.png",
    "technologie_securite": "16_technologie_securite.png",
    "focus_testament_video": "17_focus_testament_video.png",
    "pilier_emotion": "18_pilier_emotion.png",
    "image_mondiale": "19_image_mondiale.png",
}

@dataclass(frozen=True)
class KidanPage:
    key: str
    title: str
    subtitle: str
    asset_key: str
    bullets: List[str]

# Pages “pitch” alignées sur le PDF (à adapter si tu veux plus/moins de texte)
PAGES: List[KidanPage] = [
    KidanPage(
        key="page_1",
        title="Page 1",
        subtitle="Référence visuelle (couverture du dossier)",
        asset_key="accroche_principale",
        bullets=[
            "Transmettez vos mots. Préservez vos volontés. Sécurisez votre héritage.",
            "Laissez plus qu’un héritage, laissez un souvenir vivant.",
            "Un service conçu pour la transmission post-mortem, structurée et sécurisée.",
        ],
    ),
    KidanPage(
        key="vision",
        title="Notre vision",
        subtitle="Humaniser la succession",
        asset_key="vision",
        bullets=[
            "Créer la première infrastructure mondiale sécurisée de transmission vidéo post-mortem.",
            "Accessible au grand public et certifiable par notaire.",
            "Positionnement hybride : émotion + juridique + transmission sécurisée.",
            "Traçabilité complète et déclenchement contrôlé.",
        ],
    ),
    KidanPage(
        key="modele_3_niveaux",
        title="Modèle : système en 3 niveaux",
        subtitle="De la vidéo libre au testament validé par notaire",
        asset_key="modele_3_niveaux",
        bullets=[
            "Niveau 1 : message personnel (sans valeur juridique).",
            "Niveau 2 : volontés encadrées (horodatage, signature électronique).",
            "Niveau 3 : validation notariale, acte authentique, conservation double.",
            "Déclenchement post-mortem : certificat de décès, double validation, mandataire.",
        ],
    ),
    KidanPage(
        key="piliers_transmission",
        title="Les 3 piliers du modèle",
        subtitle="La transmission",
        asset_key="pilier_transmission",
        bullets=[
            "Infrastructure de délivrance post-décès.",
            "Téléversement du certificat de décès.",
            "Double validation.",
            "Mandataire désigné, codes uniques, expiration contrôlée, traçabilité.",
        ],
    ),
    KidanPage(
        key="technologie_securite",
        title="Technologie & sécurité",
        subtitle="Infrastructure sécurisée et traçable",
        asset_key="technologie_securite",
        bullets=[
            "Cloud chiffré (AWS / Azure).",
            "Authentification multi-facteurs.",
            "Horodatage certifié.",
            "Blockchain pour la traçabilité.",
            "Double validation humaine + validation notariale (modèle hybride).",
        ],
    ),
    KidanPage(
        key="modele_economique",
        title="Modèle économique",
        subtitle="Offres et segments",
        asset_key="modele_economique",
        bullets=[
            "Formule Basic : accès simple, transmission via code unique.",
            "Formule Premium : vidéos illimitées, transmission conditionnelle, coffre-fort numérique.",
            "Offre Notaires : abonnement cabinet, white label, commissions sur dossiers.",
            "Offre Entreprises (B2B2C) : assureurs, banques privées, gestionnaires de patrimoine.",
        ],
    ),
    KidanPage(
        key="marche_opportunite",
        title="Marché & opportunité",
        subtitle="Pourquoi maintenant ?",
        asset_key="marche_opportunite",
        bullets=[
            "Marché mondial des successions : plusieurs milliards.",
            "Digitalisation massive des démarches légales.",
            "Sensibilité croissante à l’héritage émotionnel.",
            "Faible concurrence structurée : création d’une nouvelle catégorie.",
        ],
    ),
    KidanPage(
        key="alliance",
        title="L’Alliance",
        subtitle="Transformer l’héritage en présence",
        asset_key="alliance",
        bullets=[
            "Un jour, nos proches ouvriront un message.",
            "Ils entendront notre voix. Ils verront notre regard. Ils comprendront nos choix.",
            "KIDAN Vid ne transmet pas seulement des données : des mots, des vérités, des intentions, de l’amour.",
        ],
    ),
]
