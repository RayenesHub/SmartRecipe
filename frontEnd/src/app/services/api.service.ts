// api.service.ts
// ------------------------------------------------------------------
// Service Angular : centralise les appels HTTP vers notre backend Flask
// ------------------------------------------------------------------

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Déclare l'interface de la réponse attendue du backend
export interface RecipeResponse {
  title: string;
  time: string;
  difficulty: string;
  steps: string;
  image_b64?: string | null;
}

@Injectable({ providedIn: 'root' })
export class ApiService {
  // URL du backend Flask (à adapter si tu déploies ailleurs)
  private BASE_URL = 'http://127.0.0.1:5000';

  // Injection du client HTTP Angular
  constructor(private http: HttpClient) {}

  // Appel POST /generate-recipe avec un JSON { ingredients: "..." }
  generateRecipe(ingredients: string): Observable<RecipeResponse> {
    return this.http.post<RecipeResponse>(`${this.BASE_URL}/generate-recipe`, {
      ingredients: ingredients
    });
  }
}
