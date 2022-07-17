import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DomainAppComponent } from './domain-app.component';


describe('DomainAppComponent', () => {
  let component: DomainAppComponent;
  let fixture: ComponentFixture<DomainAppComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DomainAppComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DomainAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
