import { Component, OnInit } from '@angular/core';
import { WebService } from '../web.service';
import { FormBuilder, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-domain-app',
  templateUrl: './domain-app.component.html',
  styleUrls: ['./domain-app.component.css']
})
export class DomainAppComponent implements OnInit {

  constructor(public WebService: WebService, private formBuilder: FormBuilder, private Toastr: ToastrService) { }
  
  selectedCSV: any = null;
  customer_configuration: any;
  domain_information: any = [];
  domainForm: any;
  customer_configuration_name: any
  customer_configuration_dropdown_form: any;

  CustomerConfigSelector(event: any) {
    sessionStorage.setItem('CustomerConfigSelectorValue', event.target.value);
    this.Toastr.info("Successfuly Changed Configuration.", "Customer Configuration Change Detected")
    var dropdown = document.getElementById("customer_dropdown_selector")
    dropdown?.blur()
  }

  DeleteDomain(Domain_Name: any) {
    this.WebService.deleteDomain(Domain_Name).subscribe((response: any ) => { this.domain_information = this.WebService.getDomain() });
    this.Toastr.error("Domain Deleted from Database.", "Successful Domain Deletion")
  }

  DeleteAllDomain() {
    this.WebService.deleteAllDomain().subscribe((response: any ) => { this.domain_information = this.WebService.getDomain() });
    this.Toastr.error("All Domain Data has been removed.", "Successfully Nuked Database.")

  }

  


  SelectedFile(event: any) {
    this.selectedCSV = <File>event.target.files[0];
  }

  uploadCSV() {
    this.WebService.uploadCSV(this.selectedCSV).subscribe((response: any ) => { this.domain_information = this.WebService.getDomain() });
    this.domainForm.reset();
    this.Toastr.warning("Attempting to upload CSV File.", "Please Wait!")
  }

  RiskScore() {
    this.customer_configuration_name = sessionStorage.getItem("CustomerConfigSelectorValue");
    this.WebService.RiskScore(this.customer_configuration_name).subscribe((response: any ) => { this.domain_information = this.WebService.getDomain() });
    this.Toastr.warning("Attempting to Apply Risk Score from Configuration.", "Please Wait!")

  }

  ngOnInit() {

    this.domainForm = this.formBuilder.group({
      "domain_csv_file":["", Validators.required]
    })

    this.customer_configuration_dropdown_form = this.formBuilder.group({
      "customer_dropdown_selector":["", Validators.required]
    })

    if(!sessionStorage["CustomerConfigSelectorValue"]) {
      this.customer_configuration_dropdown_form.setValue({
        "customer_dropdown_selector": 1
      })
    } else {
      this.customer_configuration_dropdown_form.setValue({
        "customer_dropdown_selector": sessionStorage.getItem('CustomerConfigSelectorValue')
      })
    }

    this.domain_information = this.WebService.getDomain();
    // console.log(this.domain_information);
    this.customer_configuration = this.WebService.getCustomerConfigDropdown();
    // console.log(this.customer_configuration);
    
  }


}
