import { HttpClient } from "@angular/common/http";
import { Inject, Injectable } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";
import * as moment from "moment";


@Injectable()
export class WebService {
    constructor(public http: HttpClient, public Router: Router, private router: ActivatedRoute) {}

    getDomain() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain").toPromise();
    }

    getDomainSingle(Domain_Name: any) {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain/" + Domain_Name).toPromise();
    }

    getCustomerConfigDropdown() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/configuration-dropdown").toPromise();
    }

    getCustomerConfigAll()  {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/configuration").toPromise();
    }

    getDomainDataMinor() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain-data-minor");
    }

    getEndpointStatus() {
        return this.http.get<any>("http://127.0.0.1:5000/status");
    }

    getTestData() {
        // return this.http.get<any>("http://127.0.0.1:5000/testing?start=" + start_date + "&end=" + end_date ).toPromise();
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/testing");
    }

    getDomainDataMajor() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain-data-major").toPromise();      
    }

    getDomainDataMajorFILTERED(start_date: any, end_date: any) {
        // var start_date_from_form = GraphFormData.start_date_range;
        // var end_date_from_form = GraphFormData.end_date_range;
        
        // var start_date = moment(start_date_from_form).format('DD-MM-YYYY');
        // var end_date = moment(end_date_from_form).format('DD-MM-YYYY');
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain-time-series?start=" + start_date + "&end=" + end_date ).toPromise();

    }

    getDomainThreatAnalysis() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/domain-threat-analysis").toPromise();      

    }

    deleteDomain(Domain_Name: any) {
        return this.http.delete<any>("http://127.0.0.1:5000/api/v1/domain/" + Domain_Name );
    }

    deleteAllDomain() {
        return this.http.delete("http://127.0.0.1:5000/api/v1/domain");
    }

    uploadCSV(Domain_CSV: any) {
        const FileInformation = new FormData();
        FileInformation.append("Domain_CSV", Domain_CSV, Domain_CSV.name);
        console.log(Domain_CSV, Domain_CSV.name)
        return this.http.post<any>("http://127.0.0.1:5000/api/v1/domain/upload", FileInformation );
    }

    RiskScore(customer_configuration_name: any) { 
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/risk_score/compute/" + customer_configuration_name);
    }

    getRiskScore() {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/risk_score").toPromise();
    }

    createConfiguration(New_Configuration: any) {
        let Configuration_Form_Data = new FormData();
        Configuration_Form_Data.append("customer_configuration_name", New_Configuration.customer_name);
        Configuration_Form_Data.append("score_top_level_domain", New_Configuration.score_tld);
        Configuration_Form_Data.append("score_close_match", New_Configuration.score_close_match);
        Configuration_Form_Data.append("score_look_alike", New_Configuration.score_look_alike);
        Configuration_Form_Data.append("score_email_activity", New_Configuration.score_email);
        Configuration_Form_Data.append("score_domain_state", New_Configuration.score_state);
        Configuration_Form_Data.append("score_mx_record", New_Configuration.score_mx);
        Configuration_Form_Data.append("score_spf_record", New_Configuration.score_spf);
        Configuration_Form_Data.append("dashboard_percentage", New_Configuration.dashboard_percentage);
        return this.http.post<any>("http://127.0.0.1:5000/api/v1/configuration", Configuration_Form_Data).toPromise();
    }

    updateConfiguration(customer_configuration_name:any, New_Configuration: any) {
        let Configuration_Form_Data = new FormData();
        Configuration_Form_Data.append("customer_configuration_name", New_Configuration.customer_name);
        Configuration_Form_Data.append("score_top_level_domain", New_Configuration.score_tld);
        Configuration_Form_Data.append("score_close_match", New_Configuration.score_close_match);
        Configuration_Form_Data.append("score_look_alike", New_Configuration.score_look_alike);
        Configuration_Form_Data.append("score_email_activity", New_Configuration.score_email);
        Configuration_Form_Data.append("score_domain_state", New_Configuration.score_state);
        Configuration_Form_Data.append("score_mx_record", New_Configuration.score_mx);
        Configuration_Form_Data.append("score_spf_record", New_Configuration.score_spf);
        Configuration_Form_Data.append("dashboard_percentage", New_Configuration.dashboard_percentage);
        return this.http.put<any>("http://127.0.0.1:5000/api/v1/configuration/" + customer_configuration_name, Configuration_Form_Data).toPromise();
    }

    getConfiguration(customer_configuration_name: any) {
        return this.http.get<any>("http://127.0.0.1:5000/api/v1/configuration/" + customer_configuration_name).toPromise();   
    }

    deleteConfiguration(customer_configuration_name: any) {
        return this.http.delete<any>("http://127.0.0.1:5000/api/v1/configuration/" + customer_configuration_name);

    }



}

