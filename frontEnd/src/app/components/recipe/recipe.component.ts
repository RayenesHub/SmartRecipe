// recipe.component.ts
// ------------------------------------------------------------------
// Composant d'affichage : récupère les données passées par /home,
// et les affiche (titre, temps, difficulté, étapes + image IA).
// ------------------------------------------------------------------

import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RecipeResponse } from '../../services/api.service';

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe.component.html',
  styleUrls: ['./recipe.component.css']
})
export class RecipeComponent {
  recipe?: RecipeResponse;

  constructor(private router: Router) {
    // Récupère les données passées via la navigation (state)
    const nav = this.router.getCurrentNavigation();
    this.recipe = nav?.extras?.state?.['recipe'];
    console.log("Données de la recette reçues :", this.recipe);

    // Si aucune donnée (accès direct à /recipe), on renvoie vers l'accueil
    if (!this.recipe) {
      this.router.navigate(['/']);
    }
  }
}
