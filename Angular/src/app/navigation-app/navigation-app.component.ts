import { Component, OnInit } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-navigation-app',
  templateUrl: './navigation-app.component.html',
  styleUrls: ['./navigation-app.component.css']
})
export class NavigationAppComponent implements OnInit {

  constructor(public AuthService: AuthService) { }

 async ngOnInit() {
  }

}
