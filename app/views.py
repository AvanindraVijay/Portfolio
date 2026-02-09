from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import json

from .models import (
    Profile, TechStack, SkillCategory, Skill,
    Experience, ExperienceSection, ExperienceTask,
    Project, ProjectMetric, ProjectHighlight,
    Certification, Education, Highlight, ContactMessage
)

# ===================================
# AUTHENTICATION VIEWS
# ===================================

def login_view(request):
    """Custom login page"""
    # If user is already authenticated, redirect to admin
    if request.user.is_authenticated:
        return redirect('/admin/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '/admin/')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login successful
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect(next_url)
        else:
            # Login failed
            context = {
                'error': 'Invalid username or password',
                'next': next_url,
                'username': username  # Keep username for convenience
            }
            return render(request, 'login.html', context)
    
    # GET request - show login form
    next_url = request.GET.get('next', '/admin/')
    return render(request, 'login.html', {'next': next_url})


def logout_view(request):
    """Logout and redirect to home"""
    username = request.user.username if request.user.is_authenticated else None
    auth_logout(request)
    
    if username:
        messages.success(request, f'Goodbye, {username}! You have been logged out.')
    else:
        messages.success(request, 'You have been logged out.')
    
    return redirect('/')


# ===================================
# HELPER FUNCTION
# ===================================

def get_profile_context():
    """Helper function to get profile for all views"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    return {'profile': profile}


# ===================================
# PAGE VIEWS (with profile context)
# ===================================

def home(request):
    """Home page view with dynamic content"""
    context = get_profile_context()
    context.update({
        'tech_stack': TechStack.objects.filter(is_active=True),
        'highlights': Highlight.objects.filter(is_active=True)[:3],
    })
    return render(request, 'home.html', context)


def about(request):
    """About page view with skills and education"""
    context = get_profile_context()
    context.update({
        'skill_categories': SkillCategory.objects.filter(is_active=True).prefetch_related('skills'),
        'education': Education.objects.filter(is_active=True).first(),
    })
    return render(request, 'about.html', context)


def experience(request):
    """Experience page view with timeline"""
    context = get_profile_context()
    context.update({
        'experiences': Experience.objects.filter(is_active=True).prefetch_related(
            'sections__tasks',
            'technologies'
        ),
    })
    return render(request, 'experience.html', context)


def portfolio(request):
    """Portfolio page view with projects"""
    context = get_profile_context()
    context.update({
        'projects': Project.objects.filter(is_active=True).prefetch_related(
            'metrics',
            'highlights',
            'technologies'
        ),
    })
    return render(request, 'portfolio.html', context)


def certifications(request):
    """Certifications page view"""
    context = get_profile_context()
    context.update({
        'certifications': Certification.objects.filter(is_active=True),
    })
    return render(request, 'certifications.html', context)


def contact(request):
    """Contact page view"""
    context = get_profile_context()
    return render(request, 'contact.html', context)


# ===================================
# API ENDPOINTS
# ===================================

@csrf_exempt
def contact_form(request):
    """
    Handle contact form submissions
    
    POST Parameters:
    - name: Sender's name
    - email: Sender's email
    - subject: Email subject
    - message: Message content
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            subject = data.get('subject', '').strip()
            message_text = data.get('message', '').strip()
            
            # Validation
            if not all([name, email, subject, message_text]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'All fields are required.'
                }, status=400)
            
            # Basic email validation
            if '@' not in email or '.' not in email:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Please provide a valid email address.'
                }, status=400)
            
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your message! I will get back to you soon.'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data.'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Something went wrong. Please try again later.'
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method. Only POST is allowed.'
    }, status=405)


# ===================================
# API ENDPOINTS (Public)
# ===================================

def get_projects(request):
    """API endpoint to fetch all projects data"""
    projects = Project.objects.filter(is_active=True).prefetch_related(
        'metrics',
        'highlights',
        'technologies'
    )
    
    projects_data = []
    for project in projects:
        project_dict = {
            'id': project.id,
            'number': project.number,
            'title': project.title,
            'description': project.description,
            'featured': project.is_featured,
            'github_url': project.github_url,
            'live_url': project.live_url,
            'demo_url': project.demo_url,
            'metrics': [
                {'value': m.value, 'label': m.label} 
                for m in project.metrics.all()
            ],
            'highlights': [h.description for h in project.highlights.all()],
            'tech_stack': [t.name for t in project.technologies.all()]
        }
        projects_data.append(project_dict)
    
    return JsonResponse({'projects': projects_data})


def get_skills(request):
    """API endpoint to fetch all skills data organized by category"""
    categories = SkillCategory.objects.filter(is_active=True).prefetch_related('skills')
    
    skills_data = {}
    for category in categories:
        skills_data[category.name] = [
            skill.name for skill in category.skills.filter(is_active=True)
        ]
    
    return JsonResponse({'skills': skills_data})


def get_certifications_api(request):
    """API endpoint to fetch all certifications data"""
    certs = Certification.objects.filter(is_active=True)
    
    certs_data = []
    for cert in certs:
        cert_dict = {
            'id': cert.id,
            'title': cert.title,
            'issuer': cert.issuer,
            'category': cert.category,
            'description': cert.description,
            'issue_date': cert.issue_date.isoformat() if cert.issue_date else None,
            'credential_id': cert.credential_id,
            'credential_url': cert.credential_url,
        }
        certs_data.append(cert_dict)
    
    return JsonResponse({'certifications': certs_data})


def get_experience_api(request):
    """API endpoint to fetch all experience data"""
    experiences = Experience.objects.filter(is_active=True).prefetch_related(
        'sections__tasks',
        'technologies'
    )
    
    exp_data = []
    for exp in experiences:
        sections_data = []
        for section in exp.sections.all():
            sections_data.append({
                'title': section.title,
                'tasks': [task.description for task in section.tasks.all()]
            })
        
        exp_dict = {
            'id': exp.id,
            'title': exp.title,
            'company': exp.company,
            'location': exp.location,
            'period': exp.period,
            'is_current': exp.is_current,
            'description': exp.description,
            'sections': sections_data,
            'technologies': [tech.name for tech in exp.technologies.all()]
        }
        exp_data.append(exp_dict)
    
    return JsonResponse({'experiences': exp_data})