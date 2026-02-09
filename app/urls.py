from django.urls import path
from . import views

# REMOVED app_name to avoid namespace conflicts
# app_name = 'portfolio'  # <-- This was causing the issue

urlpatterns = [
    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Page routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('certifications/', views.certifications, name='certifications'),
    path('contact/', views.contact, name='contact'),
    
    # API endpoints
    path('api/contact/', views.contact_form, name='contact_form'),
    path('api/projects/', views.get_projects, name='get_projects'),
    path('api/skills/', views.get_skills, name='get_skills'),
    path('api/certifications/', views.get_certifications_api, name='get_certifications'),
    path('api/experience/', views.get_experience_api, name='get_experience'),
]