from dataclasses import dataclass
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"


@dataclass
class Slide:
    id: int
    image_path: Path


SLIDES = {
    1: Slide(1, ASSETS_DIR / "01_cover_kidan_vid.png"),
    2: Slide(2, ASSETS_DIR / "02_vision_humaniser_succession.png"),
    3: Slide(3, ASSETS_DIR / "03_constat_humain_global.png"),
    4: Slide(4, ASSETS_DIR / "04_constat_transmission_incomplete.png"),
    5: Slide(5, ASSETS_DIR / "05_marche_opportunite.png"),
    6: Slide(6, ASSETS_DIR / "06_positionnement_strategique.png"),
    7: Slide(7, ASSETS_DIR / "07_modele_economique.png"),
    8: Slide(8, ASSETS_DIR / "08_modele_3_niveaux.png"),
    9: Slide(9, ASSETS_DIR / "09_pilier_juridique.png"),
    10: Slide(10, ASSETS_DIR / "10_pilier_transmission.png"),
    11: Slide(11, ASSETS_DIR / "11_pilier_emotion.png"),
    12: Slide(12, ASSETS_DIR / "12_infrastructure_globale.png"),
    13: Slide(13, ASSETS_DIR / "13_technologie_securite.png"),
    14: Slide(14, ASSETS_DIR / "14_alliance_institutionnelle.png"),
    15: Slide(15, ASSETS_DIR / "15_reference_mondiale.png"),
}


def get_slide(slide_id: int):
    return SLIDES.get(slide_id)
