# spelling_corrector.py
# ------------------------------------------------------------------
# Module de correction automatique d'orthographe et de syntaxe
# via un modèle local Ollama (Mistral ou LLaMA3)
# ------------------------------------------------------------------

from ai_api import generate_text

def correct_spelling(text: str) -> str:
    """
    Corrige automatiquement l'orthographe d'une liste d'ingrédients.
    Retourne la version corrigée du texte.
    """
    prompt = f"""
    Corrige uniquement les fautes d'orthographe dans le texte suivant,
    sans changer les mots valides ni la langue.
    Réponds uniquement avec la version corrigée :
    "{text}"
    """

    try:
        corrected = generate_text(prompt)
        # Nettoyage du texte
        return corrected.strip().replace("\n", " ")
    except Exception as e:
        return text  # En cas d'erreur, on garde le texte original
