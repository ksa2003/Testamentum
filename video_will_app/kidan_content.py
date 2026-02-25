from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

# Root of this Streamlit app (video_will_app/)
APP_DIR = Path(__file__).resolve().parent

# Where your PNG slides live.
# Expected structure:
# video_will_app/
#   assets/
#     01_cover_kidan_vid.png
#     ...
ASSETS_DIR = APP_DIR / "assets"


@dataclass(frozen=True)
class Slide:
    page: int
    key: str
    title: str
    text: str
    image_filename: str

    @property
    def image_path(self) -> Path:
        return ASSETS_DIR / self.image_filename


# -------------------------------------------------------------------------
# Slides mapping (aligned with your renamed assets)
# -------------------------------------------------------------------------
_SLIDES: Dict[int, Slide] = {
    1: Slide(
        page=1,
        key="cover",
        title="Kidan Vid",
        text="Couverture du dossier (identité visuelle Kidan Vid).",
        image_filename="01_cover_kidan_vid.png",
    ),
    2: Slide(
        page=2,
        key="vision",
        title="Notre vision — Humaniser la succession",
        text="Créer une infrastructure mondiale sécurisée de transmission vidéo post-mortem, accessible au grand public et certifiable par notaire.",
        image_filename="02_vision_humaniser_succession.png",
    ),
    3: Slide(
        page=3,
        key="constat_global",
        title="Le constat humain (global)",
        text="Problème : messages post-mortem qui disparaissent, volontés mal comprises, absence de transmission émotionnelle, digitalisation notariale incomplète. Solution : plateforme sécurisée + validation notariale optionnelle.",
        image_filename="03_constat_humain_global.png",
    ),
    4: Slide(
        page=4,
        key="transmission_incomplete",
        title="La transmission est incomplète",
        text="Les testaments classiques sont juridiques, froids et impersonnels. Demain : transmettre aussi notre voix.",
        image_filename="04_constat_transmission_incomplete.png",
    ),
    5: Slide(
        page=5,
        key="marche_opportunite",
        title="Marché & opportunité",
        text="Marché mondial des successions (très grand), digitalisation massive des démarches légales, sensibilité croissante à l’héritage émotionnel.",
        image_filename="05_marche_opportunite.png",
    ),
    6: Slide(
        page=6,
        key="positionnement",
        title="Positionnement stratégique global",
        text="Architecture juridique sécurisée + architecture technique & sécurité + modèle économique. Offre Notaires (White label, commission) et Offre Entreprises (B2B2C).",
        image_filename="06_positionnement_strategique.png",
    ),
    7: Slide(
        page=7,
        key="modele_economique",
        title="Modèle économique",
        text="Formules Basic / Premium + Offres Notaires + Offres Entreprises (B2B2C).",
        image_filename="07_modele_economique.png",
    ),
    8: Slide(
        page=8,
        key="modele_3_niveaux",
        title="Modèle : système en 3 niveaux",
        text="Message personnel simple → déclaration de volontés encadrée → testament validé par notaire. Déclenchement post-mortem avec certificat de décès, double validation, codes uniques, traçabilité.",
        image_filename="08_modele_3_niveaux.png",
    ),
    9: Slide(
        page=9,
        key="pilier_juridique",
        title="Les 3 piliers — Le juridique",
        text="Un testament vidéo seul n’a pas de valeur juridique en France. Le modèle Kidan Vid intègre le notaire comme pilier central (acte authentique + vidéo annexée).",
        image_filename="09_pilier_juridique.png",
    ),
    10: Slide(
        page=10,
        key="pilier_transmission",
        title="Les 3 piliers — La transmission",
        text="Infrastructure de délivrance post-décès : certificat de décès, double validation, mandataire désigné, envoi de codes uniques. Chaque destinataire : accès personnel, expiration contrôlée, traçabilité.",
        image_filename="10_pilier_transmission.png",
    ),
    11: Slide(
        page=11,
        key="pilier_emotion",
        title="Les 3 piliers — L’émotion",
        text="Transmission émotionnelle sécurisée : messages d’amour, conseils, explications, révélations personnelles. Sans valeur juridique, encadrement RGPD, hébergement sécurisé.",
        image_filename="11_pilier_emotion.png",
    ),
    12: Slide(
        page=12,
        key="infrastructure_globale",
        title="Infrastructure émotionnelle et juridique post-mortem sécurisée",
        text="Bloc émotionnel (RGPD), bloc juridique (validation humaine, conservation chez notaire), bloc transmission (déclenchement post-décès, pas d’interprétation juridique).",
        image_filename="12_infrastructure_globale.png",
    ),
    13: Slide(
        page=13,
        key="technologie_securite",
        title="Technologie & sécurité",
        text="Cloud chiffré, MFA, horodatage certifié, traçabilité (blockchain possible), double validation humaine. Modèle hybride : IA + validation notariale + infrastructure sécurisée.",
        image_filename="13_technologie_securite.png",
    ),
    14: Slide(
        page=14,
        key="alliance",
        title="L’alliance",
        text="Transmission de mots, vérités, intentions et amour. Transformer l’héritage en présence. Rejoignez Kidan Vid.",
        image_filename="14_alliance_institutionnelle.png",
    ),
    15: Slide(
        page=15,
        key="reference_mondiale",
        title="La référence mondiale",
        text="Partenaire des grandes études notariales, intégré aux assurances-vie, standard européen de transmission vidéo post-mortem.",
        image_filename="15_reference_mondiale.png",
    ),
}


def get_slide(page: int) -> Slide:
    """Return a slide by page number (1..15). Raises KeyError if not found."""
    return _SLIDES[int(page)]


def all_slides() -> List[Slide]:
    """All slides in order."""
    return [_SLIDES[i] for i in sorted(_SLIDES)]
