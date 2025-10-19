# recipe_generator.py
# ------------------------------------------------------------------
# Orchestration de la génération :
# 1) correction orthographique des ingrédients
# 2) demande à Ollama de générer la recette (texte)
# 3) extrait les sections (titre, temps, difficulté, étapes)
# 4) demande à Hugging Face de générer l'image du plat
# ------------------------------------------------------------------

from ai_api import generate_text, generate_image_from_text  # importe nos 2 fonctions IA
from spelling_corrector import correct_spelling  # nouveau module pour correction automatique
import re  # pour extraire les sections par regex

def generate_recipe(ingredients: str) -> dict:
    """
    Génère une recette (texte + image) à partir d'une liste d'ingrédients.
    Retour JSON avec : title, time, difficulty, steps, image_b64, ingredients_corriges
    """

    # ------------------------------------------------------------
    # 1) Correction orthographique automatique
    # ------------------------------------------------------------
    corrected_ingredients = correct_spelling(ingredients)
    print("🧹 Ingrédients corrigés :", corrected_ingredients)

    # ------------------------------------------------------------
    # 2) Prompt envoyé au modèle local (Mistral/LLaMA3) via Ollama
    # ------------------------------------------------------------
    prompt = f"""
    Tu es un chef cuisinier professionnel.
    Crée une recette originale en français avec les ingrédients suivants : {corrected_ingredients}.
    Réponds toujours avec ce format exact :
    Titre: ...
    Temps de préparation: ...
    Difficulté: (Facile, Moyenne ou Difficile)
    Étapes:
    1. ...
    2. ...
    3. ...
    """

    try:
        # 3) Génère la recette texte via Ollama (local)
        recipe_text = generate_text(prompt)

        # 4) Extrait les informations avec des regex robustes
        title_match = re.search(r"Titre\s*:\s*(.*)", recipe_text)
        time_match = re.search(r"Temps de préparation\s*:\s*(.*)", recipe_text)
        diff_match = re.search(r"Difficulté\s*:\s*(.*)", recipe_text)
        steps_match = re.search(r"Étapes\s*:\s*(.*)", recipe_text, re.DOTALL)

        # 5) Nettoyage / fallback si absent
        title = title_match.group(1).strip() if title_match else "Recette générée"
        time = time_match.group(1).strip() if time_match else "Non précisé"
        difficulty = diff_match.group(1).strip() if diff_match else "Moyenne"
        steps = steps_match.group(1).strip() if steps_match else recipe_text.strip()

        # 6) Génère automatiquement l'image à partir du titre de la recette
        image_prompt = f"photo réaliste du plat : {title}, présentation gastronomique"
        image_data = generate_image_from_text(image_prompt)
        print("image",image_data)
        # 7) Compose la réponse JSON pour le frontend Angular
        return {
            "title": title,
            "time": time,
            "difficulty": difficulty,
            "steps": steps,
            "image_b64": image_data.get("image_b64"),  # peut être None si erreur image
            "ingredients_corriges": corrected_ingredients   # info ajoutée
        }

    except Exception as e:
        # Gestion d'erreur globale : on renvoie un JSON cohérent
        return {
            "title": "Erreur",
            "time": "Non précisé",
            "difficulty": "Moyenne",
            "steps": f"Erreur lors de la génération : {str(e)}",
            "image_b64": None,
            "ingredients_corriges": ingredients
        }
