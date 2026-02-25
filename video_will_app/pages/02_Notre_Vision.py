import streamlit as st
from theme import apply_theme, img
from kidan_content import get_slide

apply_theme("Notre Vision")

s = get_slide(2)

if s:
    img(s.image_path)
