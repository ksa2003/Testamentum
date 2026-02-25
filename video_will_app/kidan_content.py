"""Kidan Vid - contenu issu du PDF (Kidan VF_2.pdf).

Objectif: rendre le site Streamlit lisible, avec des pages thématiques + les visuels du PDF.
Les textes ci-dessous proviennent de l'extraction texte du PDF (donc alignés sur les slides).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


BASE_DIR = Path(__file__).resolve().parent
SLIDES_DIR = BASE_DIR / "assets" / "kidan_slides"


@dataclass(frozen=True)
class Slide:
    page: int
    title: str
    text: str

    @property
    def image_path(self) -> str:
        # page_01.png ... page_18.png
        return str(SLIDES_DIR / f"page_{self.page:02d}.png")


SLIDES: List[Slide] = [
    Slide(
        page=1,
        title="Kidan Vid (couverture)",
        text=(
            "Kidan Vid. Transmettez vos mots. Préservez vos volontés. Sécurisez votre héritage. "
            "Laissez plus qu’un héritage, laissez un souvenir vivant. "
            "Avec Kidan Vid, nos mots ont plus de valeur que nos biens."
        ),
    ),
    Slide(
        page=2,
        title="Le testament authentique / Le testament Mystique Kidan Vid",
        text=(
            "Le testament authentique : reçu par un notaire en présence de témoins ou d’un second notaire. "
            "Le testament Mystique Kidan Vid : Confidentialité totale (seul le testateur connaît le contenu) ; "
            "Formalisme strict (vidéo réalisée par le testateur) ; Sécurité (acte de souscription établi par le notaire) ; "
            "Avantages (secret absolu)."
        ),
    ),
    Slide(
        page=3,
        title="Modèle : système en 3 niveaux",
        text=(
            "Message personnel simple : vidéo libre ; transmission via code unique ; hébergement sécurisé ; aucune valeur juridique. "
            "Déclaration de volontés encadrée : enregistrement vidéo ; certificat d’horodatage ; signature électronique ; "
            "option validation notaire partenaire ; valeur probatoire renforcée. "
            "Testament validé par notaire : la valeur juridique vient du notaire ; pas de vidéo seule ; utilisateur enregistre la vidéo ; "
            "transmission au notaire partenaire ; acte authentique rédigé ; vidéo annexée comme pièce complémentaire ; "
            "conservation double : notaire + Kidan Vid. "
            "Déclenchement post-mortem : déclenchement par certificat de décès ; double validation (certificat + validation notaire partenaire) ; "
            "mandataire désigné à l’avance ; transmission via codes uniques (chaque destinataire reçoit) : un accès personnel ; "
            "une expiration contrôlée ; un journal de consultation ; traçabilité totale."
        ),
    ),
    Slide(
        page=4,
        title="Modèle économique",
        text=(
            "Modèle économique : Formule Basic ; Formule Premium ; Offre Notaires ; Offre Entreprises (B2B2C). "
            "Kidan Vid devient un service inclus dans : de grandes études notariales ; les solutions intégrées aux assurances-vie ; "
            "la gestion de patrimoine."
        ),
    ),
    Slide(
        page=5,
        title="L’Alliance",
        text=(
            "L’Alliance : Un jour, nos proches ouvriront un message. Ils entendront notre voix. Ils verront notre regard. "
            "Ils comprendront nos choix. KIDAN Vid ne transmet pas seulement des données. Nous transmettons : "
            "des mots ; des vérités ; des intentions ; de l’amour. Nous transformons l’héritage en présence."
        ),
    ),
    Slide(
        page=6,
        title="Cadres reconnus / valeur juridique",
        text=(
            "Cadres reconnus : testament olographe (article 970 Code civil) ; testament authentique ; "
            "modèle Kidan Vid : intégration notariale + vidéo annexée. "
            "La valeur juridique vient du notaire. La force émotionnelle vient de la vidéo. "
            "Double conservation : étude notariale ; infrastructure KIDAN Vid. "
            "Kidan Vid est un prestataire technique d’enregistrement, d’horodatage et de transmission sécurisée."
        ),
    ),
    Slide(
        page=7,
        title="Les 3 piliers du modèle — La Transmission",
        text=(
            "Les 3 piliers du modèle : La Transmission. Infrastructure de délivrance post-décès. "
            "Déclenchement sécurisé : I. téléversement du certificat de décès ; II. double validation ; III. mandataire désigné ; "
            "IV. envoi de codes uniques. Chaque destinataire reçoit : un accès personnel ; une expiration contrôlée ; "
            "une traçabilité complète. "
            "Nous ne décidons pas. Nous transmettons."
        ),
    ),
    Slide(
        page=8,
        title="Technologie & sécurité",
        text=(
            "Technologie & sécurité : Infrastructure — cloud chiffré (AWS/Azure) ; authentification multi-facteurs ; "
            "horodatage certifié ; blockchain pour la traçabilité ; double validation humaine. "
            "Modèle hybride : IA + validation notariale + infrastructure sécurisée. Barrière à l’entrée élevée."
        ),
    ),
    Slide(
        page=9,
        title="Marché & opportunité",
        text=(
            "Marché & opportunité — Pourquoi maintenant ? "
            "Marché mondial des successions : plusieurs milliards € ; digitalisation massive des démarches légales ; "
            "sensibilité croissante à l’héritage émotionnel ; convergence IA + blockchain + droit. "
            "Kidan Vid : plus qu’un héritage, un souvenir vivant."
        ),
    ),
    Slide(
        page=10,
        title="Le constat humain",
        text=(
            "Le constat humain — Il n’existe pas de solution qui combine : l’émotion ; le cadre légal ; la sécurité technologique. "
            "La transmission est incomplète : les testaments classiques sont juridiques, froids, impersonnels ; "
            "beaucoup souhaitent laisser un message, mais ne le font pas. "
            "Aujourd’hui, nous transmettons des biens. Demain, nous transmettrons aussi notre voix."
        ),
    ),
    Slide(
        page=11,
        title="Le constat humain (problème / solution / marché)",
        text=(
            "Problème : les messages post-mortem disparaissent ; les volontés sont mal comprises ; "
            "la transmission émotionnelle est inexistante ; la digitalisation notariale est incomplète. "
            "Solution : plateforme sécurisée d’enregistrement et transmission vidéo post-mortem avec validation notariale optionnelle. "
            "Marché : 60M+ décès annuels monde ; marché succession mondial massif ; digital legacy en forte croissance."
        ),
    ),
    Slide(
        page=12,
        title="Notre vision — Humaniser la succession",
        text=(
            "Notre vision : Humaniser la succession. Créer la première infrastructure mondiale sécurisée "
            "de transmission vidéo post-mortem, accessible au grand public et certifiable par notaire. "
            "KIDAN Vid : positionnement hybride émotion + juridique ; système de déclenchement sécurisé ; "
            "valorisation et intégration des notaires comme seuls responsables de l’acte ; traçabilité complète."
        ),
    ),
    Slide(
        page=13,
        title="Notre solution",
        text=(
            "Notre solution : Une plateforme sécurisée qui permet : d’enregistrer des messages personnels ; "
            "transmettre ce qui compte vraiment ; vos mots, pour toujours ; protégez vos messages. "
            "Encadrer des volontés légales via l’intégration de notaire (meilleur juridique) : sécuriser juridiquement vos volontés ; "
            "adosser vos messages à un acte authentique ; conformité successorale certifiée. "
            "Déclencher la transmission après décès : codes d’accès uniques ; double validation ; traçabilité complète."
        ),
    ),
    Slide(
        page=14,
        title="Les 3 piliers — L’émotion",
        text=(
            "Les 3 piliers du modèle — L’émotion : transmission émotionnelle sécurisée : messages d’amour ; "
            "conseils pour ses enfants ; explications importantes ; révélations personnelles. "
            "Sans valeur juridique ; encadrement RGPD ; hébergement sécurisé. "
            "Parce qu’un sourire vaut plus qu’un document."
        ),
    ),
    Slide(
        page=15,
        title="Les 3 piliers — Le juridique",
        text=(
            "Les 3 piliers du modèle — Le juridique : préparation successorale digitale. "
            "Le testament vidéo seul n’a pas de valeur juridique en France. Kidan Vid propose une intégration notariale : "
            "1) vidéo annexée à un acte authentique ; 2) validation humaine obligatoire ; 3) conservation notaire + Kidan Vid. "
            "Une solution conforme aux cadres juridiques existants."
        ),
    ),
    Slide(
        page=16,
        title="Les 3 piliers — La transmission (rappel)",
        text=(
            "Les 3 piliers — La transmission : déclenchement sécurisé ; accès personnel ; expiration contrôlée ; "
            "traçabilité complète. Nous ne décidons pas. Nous transmettons."
        ),
    ),
    Slide(
        page=17,
        title="Positionnement stratégique global",
        text=(
            "Positionnement stratégique global : Architecture juridique sécurisée ; modèle notarial optimal. "
            "Offre Notaires : abonnement cabinet ; white label ; commission sur dossiers. "
            "Offre Entreprises (B2B2C) : assureurs ; banques privées ; gestionnaires de patrimoine. "
            "Architecture technique & sécurité : cloud + traçabilité. "
            "Très important : transmission émotionnelle sécurisée ; préparation successorale digitale ; infrastructure de délivrance post-décès. "
            "Bloc émotionnel + bloc juridique + bloc transmission."
        ),
    ),
    Slide(
        page=18,
        title="Infrastructure émotionnelle et juridique post-mortem sécurisée",
        text=(
            "Infrastructure émotionnelle et juridique post-mortem sécurisée : Bloc émotionnel ; bloc juridique ; bloc transmission. "
            "La perception conditionne la valorisation. On parle : d’infrastructure ; de certification ; de transmission sécurisée ; "
            "d’intégration notariale. Image mondiale : stable ; sérieux ; intemporel ; international. "
            "Digitalisation la transmission humaine avec rigueur, dignité et sécurité."
        ),
    ),
]


def get_slide(page: int) -> Slide:
    for s in SLIDES:
        if s.page == page:
            return s
    raise KeyError(f"Slide page {page} not found")


def all_slides() -> List[Slide]:
    return list(SLIDES)
