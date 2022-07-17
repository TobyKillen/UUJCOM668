import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { DashboardAppComponent } from './dashboard-app/dashboard-app.component';
import { DomainAppComponent } from './domain-app/domain-app.component';
import { SettingsAppComponent } from './settings-app/settings-app.component';
import { LoginAppComponent } from './login-app/login-app.component';
import { ConfigurationAppComponent } from './configuration-app/configuration-app.component';
import { DomainInformationAppComponent } from './domain-information-app/domain-information-app.component';
import { AuthService } from '@auth0/auth0-angular';

const routes: Routes = [
  { path: "login", component: LoginAppComponent, canActivate: [],  },
  { path: "login", redirectTo: "/dashboard", pathMatch: "full"},
  { path: "domain", component: DomainAppComponent},
  { path: "dashboard", component: DashboardAppComponent},
  { path: "configuration/create", component: SettingsAppComponent},
  { path: "configuration/edit/:customer_configuration_name", component: SettingsAppComponent},
  { path: "configuration", component: ConfigurationAppComponent },
  { path: "domain/:Domain_Name", component: DomainInformationAppComponent },
  { path: "**", component: LoginAppComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponets = [AppComponent, DomainAppComponent, DashboardAppComponent, LoginAppComponent, SettingsAppComponent, ConfigurationAppComponent, SettingsAppComponent, DomainAppComponent]
