# app.py
# ------------------------------------------------------------------
# Application Flask (API REST)
# Expose :
# - GET  /           : ping de santé
# - POST /generate-recipe : génère recette + image (réponse JSON)
# ------------------------------------------------------------------

from flask import Flask, request, jsonify  # serveur web + JSON
from flask_cors import CORS                # autorise CORS (appel depuis Angular)
from recipe_generator import generate_recipe  # notre logique "métier"

# Crée l'app Flask
app = Flask(__name__)

# Active CORS sur toutes les routes (pratique en dev)
CORS(app)

@app.after_request
def add_charset_header(resp):
    # Si la réponse est de type JSON, on précise le charset
    if resp.mimetype == "application/json":
        resp.headers["Content-Type"] = "application/json; charset=utf-8"
    return resp

@app.route("/", methods=["GET"])
def home():
    """
    Route de test : permet de vérifier que le backend est opérationnel.
    """
    return jsonify({"message": "✅ Backend SmartRecipe (Ollama + HuggingFace) opérationnel 🚀"})


@app.route("/generate-recipe", methods=["POST"])
def recipe():
    """
    Reçoit un JSON {"ingredients": "..."} depuis le frontend Angular,
    appelle la génération (texte + image), renvoie un JSON complet.
    """
    try:
        # Récupère le JSON de la requête HTTP
        data = request.get_json()

        # Extrait la chaîne des ingrédients (strip pour nettoyer)
        ingredients = (data.get("ingredients") or "").strip()

        # Si aucun ingrédient : erreur 400 côté client
        if not ingredients:
            return jsonify({"error": "Veuillez fournir une liste d'ingrédients"}), 400

        # Appelle la fonction de génération (Ollama + Hugging Face)
        recipe_data = generate_recipe(ingredients)

        # Renvoie le JSON au frontend
        return jsonify(recipe_data)

    except Exception as e:
        # En cas d'erreur inattendue côté serveur : 500
        return jsonify({"error": f"Erreur serveur : {str(e)}"}), 500


if __name__ == "__main__":
    # Message console au démarrage + run serveur en debug
    print("🚀 Serveur SmartRecipe lancé sur http://127.0.0.1:5000")
    app.run(debug=True)
