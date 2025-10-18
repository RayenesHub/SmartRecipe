import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {RecipeComponent} from "./components/recipe/recipe.component";
import {HomeComponent} from "./components/home/home.component";

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'recipe', component: RecipeComponent },
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
