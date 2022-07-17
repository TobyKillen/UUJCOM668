import { Component, OnInit } from '@angular/core';
import { WebService } from '../web.service';
import * as moment from 'moment';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Clipboard } from '@angular/cdk/clipboard';

@Component({
  selector: 'app-dashboard-app',
  templateUrl: './dashboard-app.component.html',
  styleUrls: ['./dashboard-app.component.css']
})
export class DashboardAppComponent implements OnInit {

  constructor(public WebService: WebService, public FormBulder: FormBuilder, public Router: Router, public Toastr: ToastrService, private clipboard: Clipboard) { }

  start_date_filter: any;
  end_date_filter: any;
  graph_range_fiter_form: any;
  domainDataMinor: any;
  DomainDataAPI: any;
  EndpointStatus: any;




  temp: any;
  domain_threat_analysis: any;
  payload: any;
  testdata: any;


  UpdateGraphs() {
    var GraphFilter = this.graph_range_fiter_form.value;
    sessionStorage['start_date'] = GraphFilter['start_date_range']
    sessionStorage['end_date'] = GraphFilter['end_date_range']
    window.location.reload();
  }

  LastThreeMonths() {
    sessionStorage['start_date'] = moment().subtract(3, 'month').format("YYYY-MM-DD");
    sessionStorage['end_date'] = moment().format("YYYY-MM-DD");
    window.location.reload();
  }




  DTATable() {
    this.Toastr.success("Success!.", "Copied Table To Clipboard.")
  }

  public GeneralBarChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true,
    backgroundColor: 'rgb(112, 186, 255)',
    borderColor: 'rgb(112, 186, 255)',
    pointBackgroundColor: 'rgb(112, 186, 255)',
    hoverBackgroundColor: 'rgb(112, 186, 255)',
    pointBorderColor: 'rgb(112, 186, 255)',
    pointHoverBackgroundColor: 'green',
    pointHoverBorderColor: 'rgb(112, 186, 255)',
    scales: {
      x2: {
        reverse: true
      }
    },
    showToolTips: true, 
    options: {
      spanGaps: true
    }
  };

  public MonthlyRegistrationsLabels: any;
  public MonthlyRegistrationsLegend = true;
  public MonthlyRegistrationsData: any;


  

  // All Domain Bar Chart Data Vars
  public DomainBarChartLabels: any;
  public DomainBarChartLegend = true;
  public DomainBarChartData: any;
   // All Domain Bar Chart Data Vars END



  // DTA Domain Bar Chart Data Vars

  public DTADomainBarChartLabels: any;
  public DTADomainBarChartLegend: any;
  public DTADomainBarChartData : any;
  // DTA Domain Bar Chart Data Vars END



  // Live Domain Bar Chart Data Vars 
  public LiveDomainBarChartLabels: any;
  public LiveDomainBarChartLegend: any;
  public LiveDomainBarChartData : any;
  // Live Domain Bar Chart Data Vars End


    // Live Domain Bar Chart Data Vars 
    public DownDomainBarChartLabels: any;
    public DownDomainBarChartLegend: any;
    public DownDomainBarChartData : any;
    // Live Domain Bar Chart Data Vars End

  // MX Domain Bar Chart Data Vars 
  public MXDomainBarChartLabels: any;
  public MXDomainBarChartLegend: any;
  public MXDomainBarChartData : any;
  // MX Domain Bar Chart Data Vars End



  // Takedown Successful Domain Bar Chart Data Vars 
  public VTDBarChartLabelsSuccessful: any;
  public VTDBarChartLegendSuccessful: any;
  public VTDBarChartDataSuccessful: any;

  // Takedown Unsuccessful Domain Bar Chart Data Vars 
  public VTDBarChartLabelsUnsuccessful: any;
  public VTDBarChartLegendUnsuccessful: any;
  public VTDBarChartDataUnsuccessful: any;

    
  // Takedown Pending Domain Bar Chart Data Vars 
  public VTDBarChartLabelsPending: any;
  public VTDBarChartLegendPending: any;
  public VTDBarChartDataPending: any;




  // DTA Pie Chart 
  public DTAPieChartLabels: any;
  public DTAPieChartLegend: any;
  public DTAPieChartData: any;

  // Domain State Doughnut
  public DomainStateChartLabels: any;
  public DomainStateLegend: any;
  public DomainStateData: any;


  public TakedownLabels: any;
  public TakedownLegend: any;
  public TakedownData: any;

  public SPFDomainBarChartLabels: any;

  start_date: any;
  end_date: any;

    async ngOnInit() {

      this.Toastr.info("Feteching Dashboard Information.", "Please Wait..");

      if (sessionStorage['start_date'] && sessionStorage['end_date']) {
        this.start_date = sessionStorage['start_date']
        this.end_date = sessionStorage['end_date']
      }
      else {
        sessionStorage['start_date'] = moment().subtract(3, 'month').format("YYYY-MM-DD");
        sessionStorage['end_date'] = moment().format("YYYY-MM-DD");
      }

      this.graph_range_fiter_form = this.FormBulder.group({
        start_date_range: "",
        end_date_range: "",
      });

      this.graph_range_fiter_form.setValue({
        start_date_range: sessionStorage['start_date'],
        end_date_range: sessionStorage['end_date']
      });



      this.MonthlyRegistrationsData = [{data: [10, 20, 30, 10, 0, 0, 10, 50, 199, 19, 111, 120], label: 'Monthly Domain Registration Activity', type: 'bar'}];
      this.MonthlyRegistrationsLabels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December '];




      this.domain_threat_analysis = this.WebService.getDomainThreatAnalysis();

      this.WebService.getDomainDataMinor().subscribe(response => {this.domainDataMinor = response});
      var DomainDataAPI = await this.WebService.getDomainDataMajorFILTERED(sessionStorage['start_date'], sessionStorage['end_date']);


      
      // All Domain Data Bar Chart
      var AllDomainDataJSON = JSON.parse(DomainDataAPI);
      this.DomainBarChartLabels = AllDomainDataJSON.AllDomainDates;
      this.DomainBarChartData = [{data: AllDomainDataJSON.AllDomainValues, label: 'All Domain Registration(s)', type: 'bar'}];

      // DTA Domain Bar Chart
      var DTADomainDataJSON = JSON.parse(DomainDataAPI);
      this.DTADomainBarChartLabels = DTADomainDataJSON.DTADomainDates;
      this.DTADomainBarChartData = [{data: DTADomainDataJSON.DTADomainValues, label: 'DTA - High Risk Domain Registration(s)', type: 'line'}];


      // Live Domain Bar Chart
      var LiveDomainDataJSON = JSON.parse(DomainDataAPI);
      this.LiveDomainBarChartLabels = LiveDomainDataJSON.LiveDomainDates;
      this.LiveDomainBarChartData = [{data: LiveDomainDataJSON.LiveDomainValues, label: 'Live Domain Registration(s)', type: 'bar'}];

      // Down Domain Bar Chart
      var DownDomainDataJSON = JSON.parse(DomainDataAPI);
      this.DownDomainBarChartLabels = LiveDomainDataJSON.DownDomainDates;
      this.DownDomainBarChartData = [{data: DownDomainDataJSON.DownDomainValues, label: 'Down Domain Registration(s)', type: 'bar'}];


      // MX Record Bar Chart
      var MXDomainDataJSON = JSON.parse(DomainDataAPI);
      this.MXDomainBarChartLabels = MXDomainDataJSON.MXDomainDates;
      this.SPFDomainBarChartLabels = MXDomainDataJSON.SPFDomainDates;

      this.MXDomainBarChartData = [
        {data: MXDomainDataJSON.MXDomainValues, label: 'MX Record(s)', type: 'bar'},
        {data: MXDomainDataJSON.SPFDomainValues, label: 'SPF Record(s)', type: 'line', lineTension: 0.5, pointRadius: 0.5, backgroundColor: "orange", borderColor: "orange", pointBackgroundColor: "orange"},
      ];

      // Virtual Takedown Chart - Successful
      var VTDDataJSON = JSON.parse(DomainDataAPI);
      this.VTDBarChartLabelsSuccessful = VTDDataJSON.VirtualTakedownDatesSuccessful;
      this.VTDBarChartDataSuccessful = [{data: VTDDataJSON.VirtualTakedownValuesSuccessful, label: 'Virtual Takedown - Takedown Successful', type: 'line'}];


      // Virtual Takedown Chart - Unsuccessful
      var VTDDataJSON = JSON.parse(DomainDataAPI);
      this.VTDBarChartLabelsUnsuccessful = VTDDataJSON.VirtualTakedownDatesUnsuccessful;
      this.VTDBarChartDataUnsuccessful = [{data: VTDDataJSON.VirtualTakedownValuesUnsuccessful, label: 'Virtual Takedown - Takedown Unsuccessful', type: 'line'}];


      // Virtual Takedown Chart - Pending
      var VTDDataJSON = JSON.parse(DomainDataAPI);
      this.VTDBarChartLabelsPending = VTDDataJSON.VirtualTakedownDatesPending;
      this.VTDBarChartDataPending = [{data: VTDDataJSON.VirtualTakedownValuesPending, label: 'Virtual Takedown - Takedown Pending', type: 'line'}];

      
      // Domain State Snapshot
      var DomainState = JSON.parse(DomainDataAPI);
      var LiveDomain = [DomainState.LiveDomainCount]
      var DownDomain = [DomainState.DownDomainCount]
      var DomainData = [LiveDomain, DownDomain]
      this.DomainStateChartLabels = ['Live Domain(s)', "Down Domain(s)"]
      this.DomainStateData = [{data: DomainData, label:["Domain State | Live vs Down"], type: "doughnut"}]


      var TakedownData = JSON.parse(DomainDataAPI);
      var Unsuccessful = [TakedownData.TakedownUnsuccessful]
      var Successful = [TakedownData.TakedownSuccessful]
      var Pending = [TakedownData.TakedownPending]
      var SourceData = [Unsuccessful, Successful, Pending]
      this.TakedownLabels = ["Unsuccessful", "Successful", "Pending"]
      this.TakedownData = [
        {data: SourceData, label:["Domain Takedown Status"], type: "doughnut"}, 
      ]


      this.EndpointStatus = this.WebService.getEndpointStatus();
      console.log(this.EndpointStatus.value);
      if (this.EndpointStatus) {
        this.Toastr.success("Successfully Loaded Dashboard Information.", "Success!");
      } 
      else {
        this.Toastr.error("Status Update: Endpoint Server is not running.", "Error!");
      }
      




  }
}
