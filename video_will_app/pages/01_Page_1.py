import streamlit as st
from pathlib import Path

from theme import apply_theme, img
from kidan_content import get_slide, ASSETS_DIR

apply_theme()

s1 = get_slide(1)

st.markdown(
    f"""
<div class="tm-card">
  <h1 class="tm-title">Page 1</h1>
  <div class="tm-sub">Référence visuelle (couverture du dossier)</div>
</div>
""",
    unsafe_allow_html=True,
)

p = Path(s1.image_path)
if p.exists():
    img(str(p))
else:
    st.warning(
        f"Image {p.name} introuvable.\n\n"
        f"Place-la dans: {ASSETS_DIR}\n"
        f"(video_will_app/assets/ sur GitHub)."
    )
