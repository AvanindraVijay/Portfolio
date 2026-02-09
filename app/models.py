from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# ===================================
# PROFILE & ABOUT
# ===================================

class Profile(models.Model):
    """Main profile information"""
    name = models.CharField(max_length=100, default="Avanindra Vijay")
    title = models.CharField(max_length=200, default="Software Engineer & Data Scientist")
    email = models.EmailField(default="vijayavanindra5793@gmail.com")
    phone = models.CharField(max_length=20, default="+91 8881164451")
    location = models.CharField(max_length=100, default="Delhi, India")
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    resume_url = models.URLField(blank=True, null=True)
    
    # About section
    about_intro = models.TextField(help_text="First paragraph of about section")
    about_details = models.TextField(help_text="Detailed description")
    about_current = models.TextField(help_text="What you're currently doing")
    
    # Stats
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=8.66)
    projects_count = models.IntegerField(default=5)
    certifications_count = models.IntegerField(default=7)
    data_records_processed = models.CharField(max_length=20, default="50K+")
    
    # Availability
    available_for_work = models.BooleanField(default=True)
    
    # Meta
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return f"{self.name} - Profile"
    
    def save(self, *args, **kwargs):
        # Ensure only one profile exists
        if not self.pk and Profile.objects.exists():
            raise ValueError("Only one Profile instance is allowed")
        return super().save(*args, **kwargs)


class TechStack(models.Model):
    """Technologies displayed in hero section"""
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Tech Stack Item"
        verbose_name_plural = "Tech Stack"
    
    def __str__(self):
        return self.name


# ===================================
# SKILLS
# ===================================

class SkillCategory(models.Model):
    """Skill categories like 'Programming Languages', 'AI & ML', etc."""
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    """Individual skills within categories"""
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"


# ===================================
# EXPERIENCE
# ===================================

class Experience(models.Model):
    """Work experience entries"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave empty if current")
    is_current = models.BooleanField(default=False)
    
    description = models.TextField(blank=True, help_text="Brief overview")
    
    order = models.IntegerField(default=0, help_text="Display order (lower = first)")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    @property
    def period(self):
        start = self.start_date.strftime("%B %Y")
        end = "Present" if self.is_current else self.end_date.strftime("%B %Y")
        return f"{start} - {end}"


class ExperienceSection(models.Model):
    """Sections within an experience (e.g., 'AI & ML', 'Backend Development')"""
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.experience.company} - {self.title}"


class ExperienceTask(models.Model):
    """Individual tasks/responsibilities within a section"""
    section = models.ForeignKey(ExperienceSection, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.section.title} - Task {self.order}"


class ExperienceTech(models.Model):
    """Technologies used in an experience"""
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.experience.company} - {self.name}"


# ===================================
# PROJECTS
# ===================================

class Project(models.Model):
    """Portfolio projects"""
    number = models.CharField(max_length=10, help_text="e.g., '01', '02'")
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    is_featured = models.BooleanField(default=False)
    
    # Links
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return f"{self.number}. {self.title}"


class ProjectMetric(models.Model):
    """Project metrics/achievements"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='metrics')
    value = models.CharField(max_length=50, help_text="e.g., '90%+', '$385K'")
    label = models.CharField(max_length=100, help_text="e.g., 'Intent Accuracy'")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - {self.value} {self.label}"


class ProjectHighlight(models.Model):
    """Key highlights/features of a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='highlights')
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - Highlight {self.order}"


class ProjectTech(models.Model):
    """Technologies used in a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - {self.name}"


# ===================================
# CERTIFICATIONS
# ===================================

class Certification(models.Model):
    """Professional certifications"""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    category = models.CharField(max_length=100, help_text="e.g., 'Cloud Computing', 'Programming'")
    description = models.TextField()
    
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True, help_text="Leave empty if no expiry")
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
    
    def __str__(self):
        return f"{self.title} - {self.issuer}"


# ===================================
# EDUCATION
# ===================================

class Education(models.Model):
    """Educational qualifications"""
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    max_cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=10.0)
    
    specialization = models.CharField(max_length=200, blank=True)
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-end_year']
        verbose_name = "Education"
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"


# ===================================
# HIGHLIGHTS (Home Page Cards)
# ===================================

class Highlight(models.Model):
    """Highlight cards on home page"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Icon identifier (for frontend)")
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Highlight"
        verbose_name_plural = "Highlights"
    
    def __str__(self):
        return self.title


# ===================================
# CONTACT MESSAGES
# ===================================

class ContactMessage(models.Model):
    """Messages submitted through contact form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"