from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


@dataclass
class Slide:
    page: int
    title: str
    subtitle: str
    bullets: list[str]

    @property
    def image_path(self) -> str:
        return str(ASSETS_DIR / f"kidan_page_{self.page:02d}.png")


def get_slide(page: int) -> Slide:
    slides: dict[int, Slide] = {
        1: Slide(
            page=1,
            title="Kidan Vid",
            subtitle="Transmettez vos mots. Préservez vos volontés. Sécurisez votre héritage.",
            bullets=[
                "Infrastructure de transmission vidéo post-mortem",
                "Option d’intégration notariale",
                "Traçabilité, confidentialité, sécurité",
            ],
        ),
        2: Slide(
            page=2,
            title="Notre vision",
            subtitle="Humaniser la succession",
            bullets=[
                "Créer une infrastructure mondiale sécurisée post-mortem",
                "Concilier émotion, cadre juridique et technologie",
                "Préparer une transmission structurée et digne",
            ],
        ),
        3: Slide(
            page=3,
            title="Modèle : système en 3 niveaux",
            subtitle="Un parcours qui s’adapte au besoin juridique",
            bullets=[
                "Message personnel simple (vidéo libre)",
                "Déclaration de volontés encadrée (signature, horodatage, option notariale)",
                "Testament validé par notaire (valeur juridique renforcée)",
            ],
        ),
        4: Slide(
            page=4,
            title="Les 3 piliers du modèle",
            subtitle="Émotion, Juridique, Transmission",
            bullets=[
                "Émotion : messages personnels (RGPD, hébergement sécurisé)",
                "Juridique : préparation successorale et validation notariale",
                "Transmission : déclenchement post-mortem, codes d’accès, traçabilité",
            ],
        ),
        5: Slide(
            page=5,
            title="Technologie & sécurité",
            subtitle="Infrastructure et conformité",
            bullets=[
                "Cloud chiffré (AWS / Azure)",
                "Authentification multi-facteurs",
                "Horodatage certifié",
                "Blockchain pour la traçabilité (option)",
                "Double validation humaine (modèle hybride)",
            ],
        ),
        6: Slide(
            page=6,
            title="Modèle économique",
            subtitle="Offres adaptées aux particuliers et aux professionnels",
            bullets=[
                "Formule Basic / Premium",
                "Offre Notaires (cabinet / white label)",
                "Offre Entreprises (B2B2C)",
                "Valorisation et différenciation forte",
            ],
        ),
        7: Slide(
            page=7,
            title="Marché & opportunité",
            subtitle="Pourquoi maintenant ?",
            bullets=[
                "Digitalisation des démarches légales",
                "Marché mondial des successions",
                "Sensibilité croissante à l’héritage et au patrimoine",
            ],
        ),
        8: Slide(
            page=8,
            title="L’Alliance",
            subtitle="Plus qu’un héritage : un souvenir vivant",
            bullets=[
                "Un jour, nos proches ouvriront un message",
                "Nous transmettons des mots, des vérités, des intentions",
                "Nous transformons l’héritage en présence",
            ],
        ),
    }

    if page not in slides:
        raise KeyError(f"Slide {page} non définie")

    return slides[page]
