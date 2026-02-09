from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, TechStack, SkillCategory, Skill,
    Experience, ExperienceSection, ExperienceTask, ExperienceTech,
    Project, ProjectMetric, ProjectHighlight, ProjectTech,
    Certification, Education, Highlight, ContactMessage
)

# ===================================
# PROFILE ADMIN
# ===================================

class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 1
    fields = ('name', 'order', 'is_active')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url', 'resume_url')
        }),
        ('About Section', {
            'fields': ('about_intro', 'about_details', 'about_current')
        }),
        ('Statistics', {
            'fields': ('cgpa', 'projects_count', 'certifications_count', 'data_records_processed')
        }),
        ('Status', {
            'fields': ('available_for_work',)
        }),
    )
    
    readonly_fields = ('updated_at',)
    
    def has_add_permission(self, request):
        # Prevent adding more than one profile
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the profile
        return False


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)


# ===================================
# SKILLS ADMIN
# ===================================

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ('name', 'order', 'is_active')


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_count', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)
    inlines = [SkillInline]
    
    def skill_count(self, obj):
        return obj.skills.filter(is_active=True).count()
    skill_count.short_description = 'Active Skills'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('category', 'order')


# ===================================
# EXPERIENCE ADMIN
# ===================================

class ExperienceSectionInline(admin.StackedInline):
    model = ExperienceSection
    extra = 1
    fields = ('title', 'order')


class ExperienceTechInline(admin.TabularInline):
    model = ExperienceTech
    extra = 3
    fields = ('name', 'order')


class ExperienceTaskInline(admin.TabularInline):
    model = ExperienceTask
    extra = 3
    fields = ('description', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'period_display', 'is_current', 'is_active')
    list_filter = ('is_current', 'is_active', 'company')
    list_editable = ('is_active',)
    ordering = ('-start_date',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
    
    inlines = [ExperienceSectionInline, ExperienceTechInline]
    
    def period_display(self, obj):
        return obj.period
    period_display.short_description = 'Period'


@admin.register(ExperienceSection)
class ExperienceSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'experience', 'task_count', 'order')
    list_filter = ('experience',)
    ordering = ('experience', 'order')
    inlines = [ExperienceTaskInline]
    
    def task_count(self, obj):
        return obj.tasks.count()
    task_count.short_description = 'Tasks'


# ===================================
# PROJECTS ADMIN
# ===================================

class ProjectMetricInline(admin.TabularInline):
    model = ProjectMetric
    extra = 2
    fields = ('value', 'label', 'order')


class ProjectHighlightInline(admin.StackedInline):
    model = ProjectHighlight
    extra = 2
    fields = ('description', 'order')


class ProjectTechInline(admin.TabularInline):
    model = ProjectTech
    extra = 5
    fields = ('name', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_featured', 'is_active', 'updated_at')
    list_filter = ('is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')
    ordering = ('order',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('number', 'title', 'description')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url', 'demo_url'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'order', 'is_active')
        }),
    )
    
    inlines = [ProjectMetricInline, ProjectHighlightInline, ProjectTechInline]
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['created_at', 'updated_at']
        return []


# ===================================
# CERTIFICATIONS ADMIN
# ===================================

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'category', 'issue_date', 'is_active')
    list_filter = ('category', 'issuer', 'is_active')
    list_editable = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'issuer', 'category', 'description')
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date')
        }),
        ('Credential', {
            'fields': ('credential_id', 'credential_url'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )


# ===================================
# EDUCATION ADMIN
# ===================================

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year_range', 'cgpa_display', 'is_active')
    list_filter = ('is_active', 'institution')
    list_editable = ('is_active',)
    ordering = ('-end_year',)
    
    fieldsets = (
        ('Degree Information', {
            'fields': ('degree', 'field', 'specialization')
        }),
        ('Institution', {
            'fields': ('institution', 'location')
        }),
        ('Duration', {
            'fields': ('start_year', 'end_year')
        }),
        ('Performance', {
            'fields': ('cgpa', 'max_cgpa')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )
    
    def year_range(self, obj):
        return f"{obj.start_year} - {obj.end_year}"
    year_range.short_description = 'Years'
    
    def cgpa_display(self, obj):
        if obj.cgpa:
            return f"{obj.cgpa} / {obj.max_cgpa}"
        return "-"
    cgpa_display.short_description = 'CGPA'


# ===================================
# HIGHLIGHTS ADMIN
# ===================================

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description', 'icon_name')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
    )


# ===================================
# CONTACT MESSAGES ADMIN
# ===================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status_badges', 'created_at')
    list_filter = ('is_read', 'is_replied', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Message Information', {
            'fields': ('name', 'email', 'subject', 'message', 'created_at')
        }),
        ('Status', {
            'fields': ('is_read', 'is_replied')
        }),
    )
    
    def status_badges(self, obj):
        read_badge = '✓ Read' if obj.is_read else '✗ Unread'
        reply_badge = '✓ Replied' if obj.is_replied else '✗ Not Replied'
        
        read_color = '#28a745' if obj.is_read else '#dc3545'
        reply_color = '#28a745' if obj.is_replied else '#ffc107'
        
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; border-radius: 3px; margin-right: 5px;">{}</span>'
            '<span style="background: {}; color: white; padding: 3px 10px; border-radius: 3px;">{}</span>',
            read_color, read_badge, reply_color, reply_badge
        )
    status_badges.short_description = 'Status'
    
    def has_add_permission(self, request):
        return False
    
    actions = ['mark_as_read', 'mark_as_replied']
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marked as read.')
    mark_as_read.short_description = 'Mark selected as read'
    
    def mark_as_replied(self, request, queryset):
        updated = queryset.update(is_replied=True)
        self.message_user(request, f'{updated} message(s) marked as replied.')
    mark_as_replied.short_description = 'Mark selected as replied'


# ===================================
# ADMIN SITE CUSTOMIZATION
# ===================================

admin.site.site_header = "Portfolio Admin Panel"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Management"