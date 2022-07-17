import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { WebService } from '../web.service';

@Component({
  selector: 'app-domain-information-app',
  templateUrl: './domain-information-app.component.html',
  styleUrls: ['./domain-information-app.component.css']
})
export class DomainInformationAppComponent implements OnInit {

  constructor(public WebService: WebService, public router: ActivatedRoute) { }

  domain_data: any;

  async ngOnInit() {
    var Domain_Name: any = this.router.snapshot.params['Domain_Name'];
    this.domain_data = await this.WebService.getDomainSingle(Domain_Name);
    console.log(this.domain_data[0]);
  }

}
