

# 🍳 **SmartRecipe – Générateur de Recettes Intelligentes**

> *“L’intelligence au service du goût !”*
> Application web propulsée par **IA locale (LLaMA 3 via Ollama)** permettant de générer automatiquement des recettes à partir des ingrédients disponibles.

---

## 🧠 **Présentation**

**SmartRecipe** est une application web innovante développée dans le cadre d’un atelier académique à **ESPRIT**.
Elle génère automatiquement des recettes personnalisées à partir d’ingrédients saisis par l’utilisateur, grâce à une **intelligence artificielle locale**.

* 🎯 **Objectif :** Simplifier la création de recettes à partir des ressources disponibles.
* 🧩 **Approche :** Intégration d’un modèle IA (LLaMA 3) dans une architecture web complète.
* 🧑‍💻 **Technologies :** Angular, Flask, Ollama.

---

## ⚙️ **Fonctionnalités**

✅ Saisie des ingrédients
🤖 Génération automatique de recettes via IA
🧾 Résultat clair : titre, durée, étapes, difficulté
🖼️ (Optionnel) Génération d’image du plat
🔒 Fonctionnement 100 % local (aucune donnée en ligne)

---

## 🏗️ **Architecture du projet**

```
SmartRecipe/
│
├── backend/
│   ├── app.py               # Serveur Flask
│   ├── ai_api.py            # Connexion avec Ollama
│   ├── requirements.txt     # Dépendances Python
│
├── frontend/
│   ├── src/                 # Code Angular
│   ├── package.json         # Dépendances Node.js
│
├── docs/                    # Documentation, schémas UML
│
└── README.md                # Ce fichier 😄
```

🧩 **Schéma simplifié :**

```
[Utilisateur] ⇄ [Interface Angular] ⇄ [Serveur Flask] ⇄ [IA Locale Ollama (LLaMA 3)]
```

---

## 💻 **Technologies utilisées**

| 🧰 Outil                     | 📝 Description        |
| ---------------------------- | --------------------- |
| **Angular**                  | Frontend moderne      |
| **Flask (Python)**           | Backend REST          |
| **Ollama (LLaMA 3)**         | Modèle IA local       |
| **HTML / CSS / TypeScript**  | Interface utilisateur |
| **Hugging Face (optionnel)** | Génération d’images   |
| **Git / GitHub**             | Gestion de versions   |

---

## 🚀 **Installation et exécution**

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/<utilisateur>/<nom-du-repo>.git
cd SmartRecipe
```

### 2️⃣ Installer le backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

🟢 Serveur Flask : `http://localhost:5000`

### 3️⃣ Lancer le frontend

```bash
cd frontend
npm install
ng serve
```

🟢 Interface Angular : `http://localhost:4200`

---

## 🌿 **Workflow Git**

### 🔧 Créer une branche

```bash
git checkout -b feature/<nom-fonctionnalite>
```

### 💾 Sauvegarder le travail

```bash
git add .
git commit -m "feat: ajout de la génération de recette"
git push origin feature/<nom-fonctionnalite>
```

### 🔁 Fusionner après validation

```bash
git checkout main
git merge feature/<nom-fonctionnalite>
git push origin main
```

---

## 🧾 **Conventions de commits**

| Type           | Exemple                                  |
| -------------- | ---------------------------------------- |
| ✨ `feat:`      | `feat: ajout du service IA`              |
| 🐛 `fix:`      | `fix: correction d’un bug Flask`         |
| 🧹 `refactor:` | `refactor: amélioration du code Angular` |
| 📄 `docs:`     | `docs: mise à jour du README`            |

---

## 🧪 **Tests et validation**

| Type          | Description                         | Résultat |
| ------------- | ----------------------------------- | -------- |
| ✅ Fonctionnel | Génération de recette IA            | OK       |
| ✅ API         | Test de la route `/generate-recipe` | OK       |
| ⚡ Performance | Temps de réponse < 5 secondes       | OK       |
| 🧍 Robustesse | Gestion d’entrées vides             | OK       |

---

## 👩‍💻 **Équipe de développement**

**Groupe 4 – SmartRecipe**

* Ons Fendouli
* Dina Bouchaddekh
* Balkis Sekri
* Rayen Ksouri
* Moatez Chouchen


🙏 **Remerciements**

Nous remercions **Mme Malak Maha** pour le cours et les ateliers pratiques qui nous ont permis de réaliser ce projet.
Merci également à **ESPRIT** pour son cadre d’apprentissage stimulant et son accompagnement.
Enfin, merci à toute l’équipe pour leur collaboration et leur engagement.

