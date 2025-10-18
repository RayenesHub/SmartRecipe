import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { RecipeComponent } from './components/recipe/recipe.component';
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {ServiceService} from "./services/service.service";

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    RecipeComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        FormsModule,
      HttpClientModule
    ],
  providers: [ServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
