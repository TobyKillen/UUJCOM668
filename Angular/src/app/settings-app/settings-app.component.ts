import { flatten, ThrowStmt } from '@angular/compiler';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { WebService } from '../web.service';

@Component({
  selector: 'app-settings-app',
  templateUrl: './settings-app.component.html',
  styleUrls: ['./settings-app.component.css']
})
export class SettingsAppComponent implements OnInit {

  constructor(private WebService: WebService, private formBuilder: FormBuilder, private Router: Router, private router: ActivatedRoute) { }

  configuration_form_default_value: any;
  configuration_form: any; 
  customer_configuration_name: any;

  ConfigurationChange: any;
  ConfigurationChangeEdit: any;
  ConfigurationChangeCreate: any;


  


  Configuration() {
    this.WebService.createConfiguration(this.configuration_form.value);
    console.log(this.configuration_form.value);
    this.Router.navigate(["/configuration"]);
  }

  updateConfiguration() {
    var customer_name = this.router.snapshot.params['customer_configuration_name'];
    this.WebService.updateConfiguration(customer_name, this.configuration_form.value);
    console.log(this.configuration_form.value);
    this.Router.navigate(["/configuration"]);
  }


  async ngOnInit() {

    this.ConfigurationChangeCreate = false;
    this.ConfigurationChangeEdit = false;

    var current_route = window.location.pathname;
    this.ConfigurationChange = current_route;
    if (this.ConfigurationChange.includes('edit')) {
      this.ConfigurationChangeEdit = true;
      console.log('True')
    }
    else {
      this.ConfigurationChangeCreate = true;
      console.log('False')
    }

    

    
    this.configuration_form = this.formBuilder.group({
      "customer_name": ["", Validators.required],
      "score_tld": ["", Validators.required],
      "score_close_match": ["", Validators.required],
      "score_look_alike": ["", Validators.required],
      "score_email": ["", Validators.required],
      "score_state": ["", Validators.required],
      "score_mx": ["", Validators.required],
      "score_spf": ["", Validators.required],
      "dashboard_percentage": ["", Validators.required],
    });

    this.customer_configuration_name = this.router.snapshot.params['customer_configuration_name'];
    this.configuration_form_default_value = await this.WebService.getConfiguration(this.customer_configuration_name);



    this.configuration_form.setValue({
      "customer_name": this.configuration_form_default_value[0].customer_configuration_name,
      "score_tld": this.configuration_form_default_value[0].score_top_level_domain,
      "score_close_match": this.configuration_form_default_value[0].score_close_match,
      "score_look_alike": this.configuration_form_default_value[0].score_look_alike,
      "score_email": this.configuration_form_default_value[0].score_email_activity, 
      "score_state": this.configuration_form_default_value[0].score_domain_state,
      "score_mx": this.configuration_form_default_value[0].score_mx_record,
      "score_spf": this.configuration_form_default_value[0].score_spf_record,
      "dashboard_percentage": this.configuration_form_default_value[0].dashboard_percentage
    })

    // console.log(this.configuration_form_default_value);




  }

}
