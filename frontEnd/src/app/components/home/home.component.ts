// home.component.ts
// ------------------------------------------------------------------
// Composant d'accueil : saisie des ingrédients et envoi au backend.
// A la réponse, on redirige vers la page "recipe" avec les données.
// ------------------------------------------------------------------

import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService, RecipeResponse } from '../../services/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  // Modèle lié au textarea ([(ngModel)])
  ingredients: string = '';

  // Injection service API + Router
  constructor(private api: ApiService, private router: Router) {}

  // Soumission du formulaire
  onSubmit() {
    // Trim pour éviter d'envoyer des espaces vides
    const value = this.ingredients.trim();

    if (!value) {
      alert("Veuillez saisir au moins un ingrédient.");
      return;
    }

    // Appel backend → reçoit RecipeResponse (texte + image)
    this.api.generateRecipe(value).subscribe({
      next: (res: RecipeResponse) => {
        // Navigue vers /recipe en passant la réponse via l'état de navigation
        this.router.navigate(['/recipe'], { state: { recipe: res } });
      },
      error: (err) => {
        console.error(err);
        alert("Erreur lors de la génération. Vérifiez le backend.");
      }
    });
  }
}
