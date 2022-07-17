import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { WebService } from '../web.service';

@Component({
  selector: 'app-configuration-app',
  templateUrl: './configuration-app.component.html',
  styleUrls: ['./configuration-app.component.css']
})
export class ConfigurationAppComponent implements OnInit {

  constructor(public WebService: WebService, private Toastr: ToastrService) { }

  customer_configuration_list: any;

  DeleteCustomerConfiguration(customer_configuration_name: any) {
    this.WebService.deleteConfiguration(customer_configuration_name).subscribe((response: any) => {this.customer_configuration_list = this.WebService.getCustomerConfigAll(), this.Toastr.error("Successfully deleted user configuration", "Deleted!")});
  }


  async ngOnInit() {
    this.customer_configuration_list = this.WebService.getCustomerConfigAll();

  }

}
