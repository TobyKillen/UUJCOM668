import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavigationAppComponent } from './navigation-app.component';

describe('NavigationAppComponent', () => {
  let component: NavigationAppComponent;
  let fixture: ComponentFixture<NavigationAppComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NavigationAppComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NavigationAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
