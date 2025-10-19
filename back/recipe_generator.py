# =======================
# 📁 recipe_generator.py – Final Version (Ollama)
# =======================
from ai_api import generate_text
import re

def generate_recipe(ingredients: str):
    """
    Génère une recette structurée à partir d'une liste d'ingrédients
    via le modèle local Ollama (Mistral).
    Retourne un dictionnaire JSON propre avec :
    - title
    - steps
    """

    prompt = f"""
    Tu es un chef cuisinier professionnel. Crée une recette originale en français
    avec les ingrédients suivants : {ingredients}.
    Réponds toujours avec le format exact suivant :

    Titre: ...
    Temps de préparation: ...
    Difficulté: (Facile, Moyenne ou Difficile)
    Étapes:
    1. ...
    2. ...
    3. ...
    """

    try:
        recipe_text = generate_text(prompt)

        # 🔍 Extraction automatique
        title_match = re.search(r"Titre\s*:\s*(.*)", recipe_text)
        time_match = re.search(r"Temps de préparation\s*:\s*(.*)", recipe_text)
        diff_match = re.search(r"Difficulté\s*:\s*(.*)", recipe_text)
        steps_match = re.search(r"Étapes\s*:\s*(.*)", recipe_text, re.DOTALL)

        title = title_match.group(1).strip() if title_match else "Recette générée"
        time = time_match.group(1).strip() if time_match else "Non précisé"
        difficulty = diff_match.group(1).strip() if diff_match else "Moyenne"
        steps = steps_match.group(1).strip() if steps_match else recipe_text.strip()

        return {
            "title": title,
            
            
            "steps": steps
        }

    except Exception as e:
        return {
            "title": "Erreur",
            "time": "Non précisé",
            "difficulty": "Moyenne",
            "steps": f"Erreur Ollama : {str(e)}"
        }
