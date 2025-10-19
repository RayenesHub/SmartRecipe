# =======================
# 📁 app.py – SmartRecipe (Ollama version)
# =======================
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from recipe_generator import generate_recipe
from image_generator import generate_image

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "✅ Backend SmartRecipe (Ollama local) opérationnel 🚀"})

@app.route('/generate-recipe', methods=['POST'])
def recipe():
    try:
        data = request.get_json()
        ingredients = data.get("ingredients", "").strip()

        if not ingredients:
            return jsonify({"error": "Veuillez fournir une liste d'ingrédients"}), 400

        recipe_data = generate_recipe(ingredients)
        return jsonify(recipe_data)
    except Exception as e:
        return jsonify({"error": f"Erreur serveur : {str(e)}"}), 500


@app.route("/generate-image", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    result = generate_image(prompt)

    if "error" in result:
        return jsonify(result), 500

    return send_file(result["image_path"], mimetype="image/png")


if __name__ == "__main__":
    print("🚀 Serveur SmartRecipe (Ollama) lancé sur http://127.0.0.1:5000")
    app.run(debug=True)
