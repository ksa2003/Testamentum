from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict

APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"


@dataclass(frozen=True)
class Slide:
    id: int
    title: str
    subtitle: str
    image_path: Path


_SLIDES: Dict[int, Slide] = {
    1: Slide(1, "Kidan Vid", "Référence visuelle (couverture du dossier)", ASSETS_DIR / "01_cover_kidan_vid.png"),
    2: Slide(2, "Notre vision", "Humaniser la succession", ASSETS_DIR / "02_vision_humaniser_succession.png"),
    3: Slide(3, "Le constat humain", "Constat global", ASSETS_DIR / "03_constat_humain_global.png"),
    4: Slide(4, "Le constat humain", "Transmission incomplète", ASSETS_DIR / "04_constat_transmission_incomplete.png"),
    5: Slide(5, "Marché & Opportunité", "Pourquoi maintenant ?", ASSETS_DIR / "05_marche_opportunite.png"),
    6: Slide(6, "Positionnement stratégique global", "Offres et segmentation", ASSETS_DIR / "06_positionnement_strategique.png"),
    7: Slide(7, "Modèle économique", "Offres et formules", ASSETS_DIR / "07_modele_economique.png"),
    8: Slide(8, "Modèle : Système en 3 niveaux", "Architecture de l’offre", ASSETS_DIR / "08_modele_3_niveaux.png"),
    9: Slide(9, "Les 3 piliers du modèle", "Le Juridique", ASSETS_DIR / "09_pilier_juridique.png"),
    10: Slide(10, "Les 3 piliers du modèle", "La Transmission", ASSETS_DIR / "10_pilier_transmission.png"),
    11: Slide(11, "Les 3 piliers du modèle", "L’Émotion", ASSETS_DIR / "11_pilier_emotion.png"),
    12: Slide(12, "Infrastructure émotionnelle et juridique", "Vision globale", ASSETS_DIR / "12_infrastructure_globale.png"),
    13: Slide(13, "Technologie & Sécurité", "Infrastructure", ASSETS_DIR / "13_technologie_securite.png"),
    14: Slide(14, "L’Alliance", "Alliance institutionnelle", ASSETS_DIR / "14_alliance_institutionnelle.png"),
    15: Slide(15, "Référence mondiale", "Transmission digitale & légale", ASSETS_DIR / "15_reference_mondiale.png"),
}


def get_slide(slide_id: int) -> Slide:
    if slide_id not in _SLIDES:
        raise KeyError(f"Slide {slide_id} introuvable. IDs dispos: {sorted(_SLIDES.keys())}")
    return _SLIDES[slide_id]
