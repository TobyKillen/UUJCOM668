import { Injectable, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { WebService } from './web.service';
import { HttpClientModule } from '@angular/common/http';
import { DomainAppComponent } from './domain-app/domain-app.component';
import { DashboardAppComponent } from './dashboard-app/dashboard-app.component';
import { ReactiveFormsModule } from '@angular/forms';
import { SettingsAppComponent } from './settings-app/settings-app.component';
import { AuthModule } from '@auth0/auth0-angular';
import { ClipboardModule } from '@angular/cdk/clipboard';


// TOASTR IMPORTS FOR USER TOASTS
import { ToastrModule } from 'ngx-toastr';



// ANGULAR CHARTS IMPORTS
import { FusionChartsModule } from "angular-fusioncharts";
import { NgChartsModule } from 'ng2-charts';
import { LoginAppComponent } from './login-app/login-app.component';
import { ConfigurationAppComponent } from './configuration-app/configuration-app.component';
import { DomainInformationAppComponent } from './domain-information-app/domain-information-app.component';
import { NavigationAppComponent } from './navigation-app/navigation-app.component';
import { FooterAppComponent } from './footer-app/footer-app.component';
import { CanActivate } from '@angular/router';



class AlwaysAuthGuard implements CanActivate {
  canActivate() {
    console.log("AlwaysAuthGuard");
    return true;
  }
}




@NgModule({
  declarations: [
    AppComponent,
    DomainAppComponent,
    DashboardAppComponent,
    SettingsAppComponent,
    LoginAppComponent,
    ConfigurationAppComponent,
    DomainInformationAppComponent,
    NavigationAppComponent,
    FooterAppComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    ReactiveFormsModule,
    FusionChartsModule,
    NgChartsModule,
    ClipboardModule,
    AuthModule.forRoot( {
      domain:'dev-84px7oyo.eu.auth0.com',
      clientId: 'VxNXi2AyGBbed3KtXiB7UANFdVCQ1TvE'
      })
  ],
  providers: [WebService, AlwaysAuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
