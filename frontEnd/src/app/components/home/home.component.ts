import { Component } from '@angular/core';
import {ServiceService} from "../../services/service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  ingredients = '';
  loading = false;
  error = '';

  constructor(private recipeService: ServiceService, private router: Router) {}

  generate() {
    this.error = '';
    if (!this.ingredients.trim()) {
      this.error = 'Veuillez saisir au moins un ingrédient.';
      return;
    }

    this.loading = true;
    this.recipeService.generateRecipe(this.ingredients).subscribe({
      next: (res) => {
        this.loading = false;
        // passer la recette à la page suivante
        this.router.navigate(['/recipe'], { state: { recipe: res } });
      },
      error: (err) => {
        this.loading = false;
        this.error = 'Erreur lors de la génération de la recette.';
        console.error(err);
      }
    });
  }
}
