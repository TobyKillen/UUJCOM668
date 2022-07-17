import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfigurationAppComponent } from './configuration-app.component';

describe('ConfigurationAppComponent', () => {
  let component: ConfigurationAppComponent;
  let fixture: ComponentFixture<ConfigurationAppComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConfigurationAppComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConfigurationAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
