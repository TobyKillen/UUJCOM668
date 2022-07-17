import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardAppComponent } from './dashboard-app.component';

describe('DashboardAppComponent', () => {
  let component: DashboardAppComponent;
  let fixture: ComponentFixture<DashboardAppComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashboardAppComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
