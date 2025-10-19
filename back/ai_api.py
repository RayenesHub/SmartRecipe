# ai_api.py
# ------------------------------------------------------------------
# Module d'accès aux services IA :
# - Texte : via Ollama (local, gratuit)
# - Image : via Hugging Face (FLUX.1-dev)
# ------------------------------------------------------------------

import subprocess            # pour exécuter la commande 'ollama run'
import os                    # pour lire les variables d'environnement (.env)
import requests              # pour appeler l'API Hugging Face
import base64                # pour encoder l'image en base64 (utile côté front)
from dotenv import load_dotenv  # pour charger le fichier .env

# Charge les variables d'environnement depuis .env (HUGGINGFACE_API_TOKEN)
load_dotenv()

#la clé Hugging Face 
HF_API_KEY = os.getenv("HUGGINGFACE_API_TOKEN")

# Choix du modèle image
HF_MODEL = "black-forest-labs/FLUX.1-dev"

# Endpoint de l'API Inference de Hugging Face
API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

# En-têtes HTTP incluant la clé d'authentification
headers = {"Authorization": f"Bearer {HF_API_KEY}"}


def generate_image_from_text(prompt):
    """
    Génère une image depuis Hugging Face (FLUX.1-dev) et renvoie en base64.
    """
    print(f"🎨 Génération d'image pour : {prompt}")
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        if response.status_code != 200:
            print("⚠️ Erreur HuggingFace:", response.text)
            return {"error": f"HuggingFace {response.status_code}: {response.text}"}

        # Vérifie le type MIME pour s'assurer qu'on reçoit bien une image
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type:
            print("⚠️ Réponse inattendue :", response.text[:300])
            return {"error": "Réponse non-image renvoyée par Hugging Face."}

        # Encode l'image en base64
        import base64
        image_b64 = base64.b64encode(response.content).decode("utf-8")
        return {"image_b64": f"data:image/png;base64,{image_b64}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur de connexion Hugging Face: {str(e)}"}


def generate_text(prompt: str) -> str:
    """
    Génère du texte localement via Ollama (UTF-8).
    Sur Windows, 'text=True' peut décoder en cp1252 → forcer encoding='utf-8'.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],   # ou "llama3"
            capture_output=True,                    # capture stdout/stderr
            text=True,                              # retourne des str (pas bytes)
            encoding="utf-8",                       # 🔴 forcer UTF-8 (clé du fix)
            errors="replace",                       # remplace tout char illégal (sécurité)
            timeout=120
        )

        # stdout est maintenant correctement décodé en UTF-8
        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Erreur : Ollama a mis trop de temps à répondre."
    except Exception as e:
        return f"Erreur Ollama : {str(e)}"
