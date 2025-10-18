import { Component } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-recipe',
  templateUrl: './recipe.component.html',
  styleUrls: ['./recipe.component.css']
})
export class RecipeComponent {
  recipe: any;

  constructor(private router: Router) {
    const nav = this.router.getCurrentNavigation();
    this.recipe = nav?.extras?.state?.['recipe'];
  }

  goBack() {
    this.router.navigate(['/']);
  }
}
