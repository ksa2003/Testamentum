# image_loader.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union, Tuple

import streamlit as st

PathLike = Union[str, Path]


@dataclass(frozen=True)
class ImageResolveResult:
    path: Optional[Path]
    found: bool
    tried: Tuple[Path, ...]


def project_root() -> Path:
    """
    Retourne le dossier racine du projet de l'app (celui qui contient ce fichier).
    Fonctionne local et sur Streamlit Cloud.
    """
    return Path(__file__).resolve().parent


def resolve_asset(
    filename: str,
    assets_dir: str = "assets",
    extra_dirs: Optional[list[PathLike]] = None,
) -> ImageResolveResult:
    """
    Résout un fichier image dans /assets, avec fallback sur d'autres dossiers si besoin.
    Ne lève pas d'exception : renvoie found=False si introuvable.
    """
    root = project_root()
    tried = []

    candidates = [
        root / assets_dir / filename,           # video_will_app/assets/xxx.png
        root / filename,                        # video_will_app/xxx.png
        Path.cwd() / assets_dir / filename,     # CWD/assets/xxx.png (selon exécution)
        Path.cwd() / filename,                  # CWD/xxx.png
    ]

    if extra_dirs:
        for d in extra_dirs:
            candidates.append(Path(d) / filename)

    for p in candidates:
        tried.append(p)
        if p.exists() and p.is_file():
            return ImageResolveResult(path=p, found=True, tried=tuple(tried))

    return ImageResolveResult(path=None, found=False, tried=tuple(tried))


@st.cache_data(show_spinner=False)
def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def show_asset_image(
    filename: str,
    caption: Optional[str] = None,
    assets_dir: str = "assets",
    width: Optional[int] = None,
    use_container_width: bool = True,
    show_warning: bool = True,
):
    """
    Affiche une image (robuste) :
    - si introuvable : warning clair + chemins testés
    - si trouvée : lecture en bytes (stable sur Streamlit Cloud)
    """
    res = resolve_asset(filename, assets_dir=assets_dir)

    if not res.found or res.path is None:
        if show_warning:
            st.warning(
                f"Image '{filename}' introuvable dans {assets_dir}/.\n"
                f"Chemins testés :\n- " + "\n- ".join(str(p) for p in res.tried)
            )
        return

    img_bytes = _read_bytes(res.path)
    st.image(img_bytes, caption=caption, width=width, use_container_width=use_container_width)
