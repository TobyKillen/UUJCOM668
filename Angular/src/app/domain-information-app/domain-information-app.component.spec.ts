import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DomainInformationAppComponent } from './domain-information-app.component';

describe('DomainInformationAppComponent', () => {
  let component: DomainInformationAppComponent;
  let fixture: ComponentFixture<DomainInformationAppComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DomainInformationAppComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DomainInformationAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
