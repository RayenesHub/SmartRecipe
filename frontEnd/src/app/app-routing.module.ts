// app-routing.module.ts
// ------------------------------------------------------------------
// Déclare les routes de l'app :
//  - /       -> HomeComponent
//  - /recipe -> RecipeComponent (affichage du résultat)
// ------------------------------------------------------------------

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { RecipeComponent } from './components/recipe/recipe.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'recipe', component: RecipeComponent },
  { path: '**', redirectTo: '' } // fallback si route inconnue
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
