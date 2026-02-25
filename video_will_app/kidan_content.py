from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


@dataclass
class Slide:
    page: int
    title: str
    text: str

    @property
    def image_path(self):
        return str(ASSETS_DIR / f"kidan_page_{self.page:02d}.png")


def get_slide(page):
    slides = {
        1: Slide(
            1,
            "Couverture",
            "Kidan Vid — Transmettez vos mots. Préservez vos volontés. Sécurisez votre héritage."
        ),
    }
    return slides[page]
