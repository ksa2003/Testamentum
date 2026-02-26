from pathlib import Path
from dataclasses import dataclass


BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"


@dataclass
class Slide:
    id: int
    image_path: Path


SLIDES = {
    1: "01_cover_kidan_vid.png",
    2: "02_vision_humaniser_succession.png",
    3: "03_constat_humain_global.png",
    4: "04_constat_transmission_incomplete.png",
    5: "05_marche_opportunite.png",
    6: "06_positionnement_strategique.png",
    7: "07_modele_economique.png",
    8: "08_modele_3_niveaux.png",
    9: "09_pilier_juridique.png",
    10: "10_pilier_transmission.png",
    11: "11_pilier_emotion.png",
    12: "12_infrastructure_globale.png",
    13: "13_technologie_securite.png",
    14: "14_alliance_institutionnelle.png",
    15: "15_reference_mondiale.png",
}


def get_slide(slide_id: int):
    filename = SLIDES.get(slide_id)
    if not filename:
        return None

    return Slide(
        id=slide_id,
        image_path=ASSETS_DIR / filename
    )
