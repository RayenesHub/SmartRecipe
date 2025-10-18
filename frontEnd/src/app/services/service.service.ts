import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  private apiUrl = 'http://127.0.0.1:5000'; // URL du backend Flask

  constructor(private http: HttpClient) {}

  generateRecipe(ingredients: string): Observable<any> {
    const body = { ingredients };
    return this.http.post(`${this.apiUrl}/generate-recipe`, body);
  }
}
