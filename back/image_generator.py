# =======================
# 📁 image_generator.py
# =======================
from ai_api import generate_image_from_text

def generate_image(prompt):
    """
    Wrapper for the image generation function.
    """
    result = generate_image_from_text(prompt)
    return result
