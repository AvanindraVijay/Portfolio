"""
Django management command to populate the portfolio database with initial data

Usage:
    python manage.py populate_portfolio

This will create all the profile data, skills, experience, projects, certifications etc.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from app.models import (
    Profile, TechStack, SkillCategory, Skill,
    Experience, ExperienceSection, ExperienceTask, ExperienceTech,
    Project, ProjectMetric, ProjectHighlight, ProjectTech,
    Certification, Education, Highlight
)


class Command(BaseCommand):
    help = 'Populates the database with portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to populate database...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Profile.objects.all().delete()
        TechStack.objects.all().delete()
        SkillCategory.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Certification.objects.all().delete()
        Education.objects.all().delete()
        Highlight.objects.all().delete()
        
        # Create Profile
        self.stdout.write('Creating profile...')
        profile = Profile.objects.create(
            name="Avanindra Vijay",
            title="Software Engineer & Data Scientist",
            email="vijayavanindra5793@gmail.com",
            phone="+91 8881164451",
            location="Delhi, India",
            linkedin_url="https://www.linkedin.com/in/avanindra-vijay",
            github_url="https://github.com/avanindra",
            about_intro="I'm a software engineer specializing in artificial intelligence, machine learning, and data science. With a strong foundation in computer science from KIIT Bhubaneswar (8.66 CGPA) and hands-on experience at BISAG-N under the Ministry of Electronics and Information Technology, I focus on building intelligent systems that solve real-world problems.",
            about_details="My expertise spans from developing multilingual RAG-based conversational AI to creating comprehensive data analytics pipelines. I'm passionate about leveraging cutting-edge technologies like LLMs, vector databases, and computer vision to create impactful solutions for government and enterprise applications.",
            about_current="Currently, I'm building production-grade AI applications using Django, implementing RAG pipelines for semantic search, and fine-tuning large language models to improve accuracy and user experience.",
            cgpa=8.66,
            projects_count=5,
            certifications_count=7,
            data_records_processed="50K+",
            available_for_work=True
        )
        self.stdout.write(self.style.SUCCESS('✓ Profile created'))
        
        # Create Tech Stack
        self.stdout.write('Creating tech stack...')
        tech_items = [
            "Python", "Django", "LangChain", "LLaMA", "PostgreSQL", "RAG"
        ]
        for idx, tech in enumerate(tech_items):
            TechStack.objects.create(name=tech, order=idx, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(tech_items)} tech stack items'))
        
        # Create Skills
        self.stdout.write('Creating skills...')
        skills_data = {
            "Programming Languages": ["Python", "SQL"],
            "AI & Machine Learning": ["LLaMA", "Mistral", "CLIP", "RAG", "LangChain", "LangGraph", "Hugging Face", "VannaAI", "DeepSeek OCR"],
            "Frameworks & Libraries": ["Django", "RASA", "Pandas", "NumPy", "Scikit-learn", "OpenCV", "Transformers"],
            "Databases": ["PostgreSQL", "MySQL", "Vector Databases", "FAISS"],
            "Data Visualization": ["Power BI", "Plotly", "Matplotlib", "Seaborn"],
            "Developer Tools": ["VS Code", "Git & GitHub", "Jupyter Notebook", "Postman"]
        }
        
        for idx, (category_name, skills) in enumerate(skills_data.items()):
            category = SkillCategory.objects.create(
                name=category_name,
                order=idx,
                is_active=True
            )
            for skill_idx, skill_name in enumerate(skills):
                Skill.objects.create(
                    category=category,
                    name=skill_name,
                    order=skill_idx,
                    is_active=True
                )
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(skills_data)} skill categories'))
        
        # Create Education
        self.stdout.write('Creating education...')
        Education.objects.create(
            degree="Bachelor of Technology",
            field="Computer Science Engineering",
            institution="Kalinga Institute of Industrial Technology (KIIT)",
            location="Bhubaneswar, India",
            start_year=2020,
            end_year=2024,
            cgpa=8.66,
            max_cgpa=10.0,
            specialization="AI & Data Science",
            order=0,
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS('✓ Education created'))
        
        # Create Experiences
        self.stdout.write('Creating experiences...')
        
        # Experience 1: Current Role
        exp1 = Experience.objects.create(
            title="Young Professional (Software Developer)",
            company="BISAG-N (MeitY)",
            location="Gandhinagar, Gujarat",
            start_date=date(2025, 8, 1),
            end_date=None,
            is_current=True,
            description="",
            order=0,
            is_active=True
        )
        
        # Sections for Experience 1
        section1_1 = ExperienceSection.objects.create(
            experience=exp1,
            title="AI, Machine Learning & NLP",
            order=0
        )
        tasks_1_1 = [
            "Designed and developed LLM-powered intelligent chatbots using LLaMA, embeddings, and Retrieval-Augmented Generation (RAG)",
            "Implemented RAG pipelines for PDF summarization and contextual Q&A using semantic retrieval and vector databases",
            "Improved chatbot accuracy and relevance through prompt engineering, embedding optimization, and similarity search tuning",
            "Researched computer vision-based person identification techniques, comparing Sobel + SURF and Canny + PHOG methods"
        ]
        for idx, task in enumerate(tasks_1_1):
            ExperienceTask.objects.create(section=section1_1, description=task, order=idx)
        
        section1_2 = ExperienceSection.objects.create(
            experience=exp1,
            title="Backend & System Development",
            order=1
        )
        tasks_1_2 = [
            "Built and deployed production-grade AI applications using Django, ensuring modular design and scalable REST APIs",
            "Designed end-to-end chatbot architectures integrating LLMs, databases, and vector stores",
            "Evaluated LangChain vs LangGraph for workflow orchestration, scalability, and long-context handling"
        ]
        for idx, task in enumerate(tasks_1_2):
            ExperienceTask.objects.create(section=section1_2, description=task, order=idx)
        
        section1_3 = ExperienceSection.objects.create(
            experience=exp1,
            title="Database & Data Engineering",
            order=2
        )
        tasks_1_3 = [
            "Developed an AI-driven SQL Coder chatbot capable of generating, validating, and executing SQL queries from natural language",
            "Integrated relational databases for real-time data access and chatbot-driven analytics",
            "Created interactive analytics dashboards using Plotly and Pandas DataFrames for SQL insights"
        ]
        for idx, task in enumerate(tasks_1_3):
            ExperienceTask.objects.create(section=section1_3, description=task, order=idx)
        
        # Technologies for Experience 1
        tech_1 = ["LLaMA", "Django", "RAG", "LangChain", "PostgreSQL", "Plotly", "VannaAI"]
        for idx, tech in enumerate(tech_1):
            ExperienceTech.objects.create(experience=exp1, name=tech, order=idx)
        
        # Experience 2: Intern Role
        exp2 = Experience.objects.create(
            title="Software Developer Intern",
            company="BISAG-N (MeitY)",
            location="Gandhinagar, Gujarat",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 8, 1),
            is_current=False,
            description="",
            order=1,
            is_active=True
        )
        
        section2_1 = ExperienceSection.objects.create(
            experience=exp2,
            title="Key Achievements",
            order=0
        )
        tasks_2_1 = [
            "Fine-tuned CLIP, LLaMA (3B), and mBERT models using Hugging Face and Ollama",
            "Improved intent recognition accuracy by 10% and user engagement by 12% in conversational AI systems",
            "Built a RASA-integrated RAG conversational chatbot for government citizen services",
            "Implemented context-aware responses using PostgreSQL-backed retrieval and semantic search",
            "Cleaned, processed, and analyzed large-scale grievance datasets using Pandas",
            "Visualized complaint trends to identify resolution bottlenecks and efficiency gaps"
        ]
        for idx, task in enumerate(tasks_2_1):
            ExperienceTask.objects.create(section=section2_1, description=task, order=idx)
        
        tech_2 = ["RASA", "CLIP", "mBERT", "Hugging Face", "Pandas", "PostgreSQL"]
        for idx, tech in enumerate(tech_2):
            ExperienceTech.objects.create(experience=exp2, name=tech, order=idx)
        
        # Experience 3: Salesforce
        exp3 = Experience.objects.create(
            title="Salesforce Developer Intern",
            company="Deloitte",
            location="Remote",
            start_date=date(2023, 5, 1),
            end_date=date(2023, 7, 31),
            is_current=False,
            description="",
            order=2,
            is_active=True
        )
        
        section3_1 = ExperienceSection.objects.create(
            experience=exp3,
            title="Key Achievements",
            order=0
        )
        tasks_3_1 = [
            "Automated workflows using Salesforce Flows, Apex, and Lightning Web Components (LWC)",
            "Delivered custom Salesforce solutions with 20% process efficiency improvement",
            "Achieved 98% deployment success rate across multiple projects",
            "Collaborated with cross-functional teams to implement enterprise CRM solutions"
        ]
        for idx, task in enumerate(tasks_3_1):
            ExperienceTask.objects.create(section=section3_1, description=task, order=idx)
        
        tech_3 = ["Salesforce", "Apex", "Lightning Web Components", "Salesforce Flows"]
        for idx, tech in enumerate(tech_3):
            ExperienceTech.objects.create(experience=exp3, name=tech, order=idx)
        
        # Experience 4: Cisco
        exp4 = Experience.objects.create(
            title="Cyber Security Trainee",
            company="Cisco",
            location="Remote",
            start_date=date(2023, 3, 1),
            end_date=date(2023, 4, 30),
            is_current=False,
            description="",
            order=3,
            is_active=True
        )
        
        section4_1 = ExperienceSection.objects.create(
            experience=exp4,
            title="Training Focus",
            order=0
        )
        tasks_4_1 = [
            "Worked with IP protocols, routing, switching, and Ethernet technologies",
            "Trained in malware analysis, network security protocols, and threat mitigation",
            "Completed CCNA v7 certification training"
        ]
        for idx, task in enumerate(tasks_4_1):
            ExperienceTask.objects.create(section=section4_1, description=task, order=idx)
        
        tech_4 = ["CCNA", "Network Security", "Malware Analysis"]
        for idx, tech in enumerate(tech_4):
            ExperienceTech.objects.create(experience=exp4, name=tech, order=idx)
        
        self.stdout.write(self.style.SUCCESS('✓ Created 4 experiences'))
        
        # Create Projects
        self.stdout.write('Creating projects...')
        
        # Project 1: SQL Coder Chatbot
        proj1 = Project.objects.create(
            number="01",
            title="SQL Coder Chatbot with VannaAI",
            description="An AI-powered chatbot that converts natural language queries into SQL, executes them, and presents results through interactive visualizations.",
            is_featured=True,
            github_url="",
            live_url="",
            demo_url="",
            order=0,
            is_active=True
        )
        
        ProjectMetric.objects.create(project=proj1, value="90%+", label="Query Accuracy", order=0)
        ProjectMetric.objects.create(project=proj1, value="5x", label="Faster Analysis", order=1)
        
        highlights_1 = [
            "Built an intelligent SQL query generation system using VannaAI and LLMs",
            "Integrated with PostgreSQL for real-time database operations",
            "Created interactive Plotly dashboards for data visualization",
            "Implemented error handling and query validation mechanisms"
        ]
        for idx, highlight in enumerate(highlights_1):
            ProjectHighlight.objects.create(project=proj1, description=highlight, order=idx)
        
        tech_p1 = ["Python", "VannaAI", "LLaMA", "PostgreSQL", "Plotly", "Django"]
        for idx, tech in enumerate(tech_p1):
            ProjectTech.objects.create(project=proj1, name=tech, order=idx)
        
        # Project 2: RAG Chatbot
        proj2 = Project.objects.create(
            number="02",
            title="Multilingual RAG-Based PDF Chatbot",
            description="A sophisticated chatbot using Retrieval-Augmented Generation to answer questions from PDF documents in multiple languages.",
            is_featured=True,
            github_url="",
            live_url="",
            demo_url="",
            order=1,
            is_active=True
        )
        
        ProjectMetric.objects.create(project=proj2, value="85%+", label="Response Accuracy", order=0)
        ProjectMetric.objects.create(project=proj2, value="10+", label="Languages Supported", order=1)
        
        highlights_2 = [
            "Implemented RAG pipeline with semantic search using vector databases",
            "Fine-tuned LLaMA 3B model for improved context understanding",
            "Built embedding-based retrieval system with FAISS",
            "Designed modular architecture for easy language expansion"
        ]
        for idx, highlight in enumerate(highlights_2):
            ProjectHighlight.objects.create(project=proj2, description=highlight, order=idx)
        
        tech_p2 = ["LLaMA", "RAG", "FAISS", "LangChain", "Transformers", "Django"]
        for idx, tech in enumerate(tech_p2):
            ProjectTech.objects.create(project=proj2, name=tech, order=idx)
        
        # Project 3: Grievance Analysis
        proj3 = Project.objects.create(
            number="03",
            title="Grievance Data Analytics Dashboard",
            description="A comprehensive analytics platform for processing and visualizing 50K+ citizen grievance records to identify patterns and bottlenecks.",
            is_featured=True,
            github_url="",
            live_url="",
            demo_url="",
            order=2,
            is_active=True
        )
        
        ProjectMetric.objects.create(project=proj3, value="50K+", label="Records Processed", order=0)
        ProjectMetric.objects.create(project=proj3, value="30%", label="Faster Insights", order=1)
        
        highlights_3 = [
            "Cleaned and processed large-scale government grievance datasets",
            "Created interactive Power BI dashboards for trend analysis",
            "Identified key bottlenecks reducing resolution time by 25%",
            "Implemented automated data pipeline for regular updates"
        ]
        for idx, highlight in enumerate(highlights_3):
            ProjectHighlight.objects.create(project=proj3, description=highlight, order=idx)
        
        tech_p3 = ["Python", "Pandas", "Power BI", "SQL", "Plotly"]
        for idx, tech in enumerate(tech_p3):
            ProjectTech.objects.create(project=proj3, name=tech, order=idx)
        
        # Project 4: RASA Chatbot
        proj4 = Project.objects.create(
            number="04",
            title="RASA-Based Government Services Chatbot",
            description="An intelligent conversational AI system for citizen services with intent recognition and contextual responses.",
            is_featured=True,
            github_url="",
            live_url="",
            demo_url="",
            order=3,
            is_active=True
        )
        
        ProjectMetric.objects.create(project=proj4, value="90%+", label="Intent Accuracy", order=0)
        ProjectMetric.objects.create(project=proj4, value="12%", label="User Engagement ↑", order=1)
        
        highlights_4 = [
            "Built conversational AI using RASA framework with custom NLU pipeline",
            "Integrated PostgreSQL for context management and conversation history",
            "Fine-tuned mBERT for multilingual intent recognition",
            "Achieved 90%+ intent recognition accuracy through iterative training"
        ]
        for idx, highlight in enumerate(highlights_4):
            ProjectHighlight.objects.create(project=proj4, description=highlight, order=idx)
        
        tech_p4 = ["RASA", "mBERT", "PostgreSQL", "Python", "NLP"]
        for idx, tech in enumerate(tech_p4):
            ProjectTech.objects.create(project=proj4, name=tech, order=idx)
        
        # Project 5: Person Identification
        proj5 = Project.objects.create(
            number="05",
            title="Computer Vision Person Identification System",
            description="Research and implementation of person identification techniques using advanced computer vision algorithms.",
            is_featured=False,
            github_url="",
            live_url="",
            demo_url="",
            order=4,
            is_active=True
        )
        
        ProjectMetric.objects.create(project=proj5, value="88%", label="Detection Accuracy", order=0)
        
        highlights_5 = [
            "Compared Sobel + SURF vs Canny + PHOG edge detection methods",
            "Implemented feature extraction and matching algorithms",
            "Analyzed performance metrics for real-world applications",
            "Documented findings for future research applications"
        ]
        for idx, highlight in enumerate(highlights_5):
            ProjectHighlight.objects.create(project=proj5, description=highlight, order=idx)
        
        tech_p5 = ["OpenCV", "Python", "Computer Vision", "SURF", "PHOG"]
        for idx, tech in enumerate(tech_p5):
            ProjectTech.objects.create(project=proj5, name=tech, order=idx)
        
        self.stdout.write(self.style.SUCCESS('✓ Created 5 projects'))
        
        # Create Certifications
        self.stdout.write('Creating certifications...')
        
        certifications_data = [
            {
                "title": "AWS Cloud Foundation",
                "issuer": "AWS Academics",
                "category": "Cloud Computing",
                "description": "Comprehensive understanding of cloud computing fundamentals, AWS core services architecture, and cloud deployment models.",
                "order": 0
            },
            {
                "title": "PCAP: Programming Essentials in Python",
                "issuer": "OpenEDG",
                "category": "Programming",
                "description": "Advanced Python programming certification covering fundamentals, OOP, modules, and best practices for professional development.",
                "order": 1
            },
            {
                "title": "CCNA v7: Introduction to Networks",
                "issuer": "Cisco",
                "category": "Networking",
                "description": "Networking fundamentals, IP protocols, routing and switching technologies, and network security essentials.",
                "order": 2
            },
            {
                "title": "Generative AI",
                "issuer": "Microsoft & LinkedIn",
                "category": "Artificial Intelligence",
                "description": "Understanding of generative AI concepts, applications in business, and practical implementation strategies.",
                "order": 3
            },
            {
                "title": "Salesforce Developer",
                "issuer": "Deloitte",
                "category": "Enterprise Development",
                "description": "Salesforce platform development expertise including Apex programming, Lightning Web Components, and enterprise CRM solutions.",
                "order": 4
            },
            {
                "title": "SQL",
                "issuer": "HackerRank",
                "category": "Database",
                "description": "Advanced SQL skills including complex queries, database design, optimization techniques, and data manipulation.",
                "order": 5
            },
            {
                "title": "Data Analysis",
                "issuer": "Microsoft & LinkedIn",
                "category": "Data Science",
                "description": "Comprehensive data analysis techniques, statistical methods, visualization best practices, and insights extraction.",
                "order": 6
            }
        ]
        
        for cert_data in certifications_data:
            Certification.objects.create(**cert_data, is_active=True)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(certifications_data)} certifications'))
        
        # Create Highlights
        self.stdout.write('Creating highlights...')
        
        highlights_data = [
            {
                "title": "AI & Machine Learning",
                "description": "Expertise in LLM integration, RAG pipelines, and fine-tuning models like LLaMA and CLIP for production applications",
                "icon_name": "ai_ml",
                "order": 0
            },
            {
                "title": "Full-Stack Development",
                "description": "Building scalable applications with Django, REST APIs, and modern frontend technologies with clean architecture",
                "icon_name": "fullstack",
                "order": 1
            },
            {
                "title": "Data Analytics",
                "description": "Creating interactive dashboards and extracting insights from complex datasets using Python, Pandas, and Power BI",
                "icon_name": "analytics",
                "order": 2
            }
        ]
        
        for highlight_data in highlights_data:
            Highlight.objects.create(**highlight_data, is_active=True)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(highlights_data)} highlights'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'✓ Profile: 1')
        self.stdout.write(f'✓ Tech Stack: {TechStack.objects.count()}')
        self.stdout.write(f'✓ Skill Categories: {SkillCategory.objects.count()}')
        self.stdout.write(f'✓ Skills: {Skill.objects.count()}')
        self.stdout.write(f'✓ Education: {Education.objects.count()}')
        self.stdout.write(f'✓ Experiences: {Experience.objects.count()}')
        self.stdout.write(f'✓ Projects: {Project.objects.count()}')
        self.stdout.write(f'✓ Certifications: {Certification.objects.count()}')
        self.stdout.write(f'✓ Highlights: {Highlight.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\nYou can now login to admin and manage your portfolio!'))