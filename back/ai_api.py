# =======================
# 📁 ai_api.py – Version Ollama locale
# =======================
import subprocess
import os
from dotenv import load_dotenv
import requests 

load_dotenv()
HF_API_KEY = os.getenv("HUGGINGFACE_API_TOKEN") 
HF_MODEL = "black-forest-labs/FLUX.1-dev"
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def generate_image_from_text(prompt):
    """
    Generate an image using FLUX.1-dev model from Hugging Face
    """
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": f"Error {response.status_code}: {response.text}"}

    # Save image
    output_path = "generated_image.png"
    with open(output_path, "wb") as f:
        f.write(response.content)

    return {"image_path": output_path}

def generate_text(prompt: str):
    """
    Génère du texte localement avec Ollama (modèle Mistral ou autre).
    Aucun token, aucun quota requis.
    """
    try:
        # 🧠 Appel au modèle local "mistral" via le terminal
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True,
            timeout=120
        )

        # ✅ Résultat brut du modèle
        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Erreur : le modèle Ollama a mis trop de temps à répondre."
    except Exception as e:
        return f"Erreur Ollama : {str(e)}"
