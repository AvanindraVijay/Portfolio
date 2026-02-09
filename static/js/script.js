// Theme Management
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

// Load saved theme or default to light
const savedTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    });
}

// Mobile Menu Management
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileMenu = document.getElementById('mobileMenu');
const mobileLinks = document.querySelectorAll('.mobile-link');

if (mobileMenuToggle) {
    mobileMenuToggle.addEventListener('click', () => {
        mobileMenuToggle.classList.toggle('active');
        mobileMenu.classList.toggle('active');
    });
}

// Close mobile menu when clicking a link
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
        if (mobileMenu) mobileMenu.classList.remove('active');
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (mobileMenuToggle && mobileMenu) {
        if (!mobileMenuToggle.contains(e.target) && !mobileMenu.contains(e.target)) {
            mobileMenuToggle.classList.remove('active');
            mobileMenu.classList.remove('active');
        }
    }
});

// Header Shadow on Scroll
const header = document.querySelector('.header');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
    } else {
        header.style.boxShadow = 'none';
    }
});

// Contact Form Handling
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };
        
        try {
            const response = await fetch('/api/contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (response.ok) {
                formMessage.textContent = data.message || 'Thank you for your message! I will get back to you soon.';
                formMessage.className = 'form-message success';
                contactForm.reset();
            } else {
                throw new Error(data.message || 'Something went wrong');
            }
        } catch (error) {
            // For static version without backend
            formMessage.textContent = 'Thank you for your message! I will get back to you soon.';
            formMessage.className = 'form-message success';
            contactForm.reset();
        }
        
        // Hide message after 5 seconds
        setTimeout(() => {
            formMessage.style.display = 'none';
            formMessage.className = 'form-message';
        }, 5000);
    });
}

// Smooth Scroll for Anchor Links (if any on same page)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            const headerOffset = 70;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Intersection Observer for Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
const animatedElements = document.querySelectorAll(
    '.highlight-card, .expertise-card, .timeline-item, .project-card, .cert-card, .stat-box, .skill-category'
);

animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});

// Handle Resize Events
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // Close mobile menu on resize to desktop
        if (window.innerWidth > 768) {
            if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
            if (mobileMenu) mobileMenu.classList.remove('active');
        }
    }, 250);
});

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
        if (mobileMenu) mobileMenu.classList.remove('active');
    }
});

// Performance optimization: Lazy load images if any
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Initialize page
document.addEventListener('DOMContentLoaded', () => {
    // Add fade-in effect to body
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.3s ease';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

console.log('%cAvanindra Vijay - Portfolio', 'color: #2563eb; font-size: 20px; font-weight: bold;');
console.log('%cBuilt with Django, HTML, CSS, and JavaScript', 'color: #64748b; font-size: 12px;');
console.log('%cInterested in the code? Visit GitHub!', 'color: #0ea5e9; font-size: 12px;');

// ===================================
// INTERACTIVE TERMINAL - FIXED VERSION
// ===================================
(function initTerminal() {
    const terminalContent = document.getElementById('terminalContent');
    const terminalInput = document.getElementById('terminalInput');

    if (!terminalInput || !terminalContent) {
        return; // Terminal not on this page
    }

    const commands = {
        help: {
            output: [
                '<span class="terminal-success">Available Commands:</span>',
                ' ',
                '<span class="terminal-info">about</span>      - Learn about me',
                '<span class="terminal-info">skills</span>     - View my technical skills',
                '<span class="terminal-info">experience</span> - See my work history',
                '<span class="terminal-info">projects</span>   - Browse my projects',
                '<span class="terminal-info">contact</span>    - Get in touch',
                '<span class="terminal-info">education</span>  - View educational background',
                ' ',
                '<span class="terminal-info">clear</span>      - Clear terminal',
                '<span class="terminal-info">whoami</span>     - Display current user',
                '<span class="terminal-info">ls</span>         - List files',
                '<span class="terminal-info">pwd</span>        - Print working directory'
            ]
        },
        about: {
            output: [
                '<span class="terminal-success">About Me:</span>',
                ' ',
                'Software Engineer specializing in AI/ML and Data Science',
                'Currently @ BISAG-N (MeitY)',
                'B.Tech in CSE from KIIT (8.66 CGPA)',
                ' ',
                '<span class="terminal-info">Learn more:</span>'
            ],
            button: {
                text: 'View Full Profile →',
                link: '/about'
            }
        },
        skills: {
            output: [
                '<span class="terminal-success">Core Skills:</span>',
                ' ',
                '<span class="terminal-info">AI/ML:</span> LLaMA, RAG, LangChain, Hugging Face',
                '<span class="terminal-info">Backend:</span> Django, PostgreSQL, REST APIs',
                '<span class="terminal-info">Data:</span> Pandas, Plotly, Power BI',
                '<span class="terminal-info">Languages:</span> Python, SQL',
                ' ',
                '<span class="terminal-info">View complete skill set:</span>'
            ],
            button: {
                text: 'All Skills →',
                link: '/about#skills'
            }
        },
        experience: {
            output: [
                '<span class="terminal-success">Work Experience:</span>',
                ' ',
                '<span class="terminal-info">Young Professional (Current)</span>',
                'BISAG-N (MeitY) | Software Developer',
                'Building LLM-powered AI systems',
                ' ',
                '<span class="terminal-info">View complete experience timeline:</span>'
            ],
            button: {
                text: 'View All Experience →',
                link: '/experience'
            }
        },
        projects: {
            output: [
                '<span class="terminal-success">Featured Projects:</span>',
                ' ',
                '<span class="terminal-info">1. PMIS</span> - Multilingual RAG-based AI Assistant',
                '<span class="terminal-info">2. JK Samadhan</span> - Grievance Analytics (50K+ records)',
                '<span class="terminal-info">3. Raksha Yantra</span> - AI SQL Assistant',
                '<span class="terminal-info">4. Pratibimb</span> - CV-based Person ID',
                ' ',
                '<span class="terminal-info">Explore all projects:</span>'
            ],
            button: {
                text: 'View Portfolio →',
                link: '/portfolio'
            }
        },
        contact: {
            output: [
                '<span class="terminal-success">Contact Information:</span>',
                ' ',
                '<span class="terminal-info">Email:</span> vijayavanindra5793@gmail.com',
                '<span class="terminal-info">Phone:</span> +91 8881164451',
                '<span class="terminal-info">Location:</span> Delhi, India',
                ' ',
                '<span class="terminal-info">Send me a message:</span>'
            ],
            button: {
                text: 'Contact Me →',
                link: '/contact'
            }
        },
        education: {
            output: [
                '<span class="terminal-success">Education:</span>',
                ' ',
                '<span class="terminal-info">B.Tech in Computer Science Engineering</span>',
                'Kalinga Institute of Industrial Technology (KIIT)',
                'CGPA: 8.66/10.0 | 2020 - 2024',
                ' ',
                '<span class="terminal-info">Learn more:</span>'
            ],
            button: {
                text: 'View Education Details →',
                link: '/about'
            }
        },
        clear: {
            action: 'clear'
        },
        whoami: {
            output: [
                'Avanindra Vijay - Software Engineer & Data Scientist'
            ]
        },
        ls: {
            output: [
                '<span class="terminal-info">about.md</span>  <span class="terminal-info">skills.json</span>  <span class="terminal-info">projects/</span>  <span class="terminal-info">experience.log</span>  <span class="terminal-info">contact.txt</span>'
            ]
        },
        pwd: {
            output: [
                '/home/avanindra/portfolio'
            ]
        }
    };

    // Add command to terminal
    function addOutput(lines, isCommand = false) {
        lines.forEach(line => {
            const terminalLine = document.createElement('div');
            terminalLine.className = 'terminal-line';
            
            if (isCommand) {
                terminalLine.innerHTML = `<span class="terminal-prompt">$</span> <span class="terminal-command">${line}</span>`;
            } else {
                terminalLine.innerHTML = `<span class="terminal-output">${line}</span>`;
            }
            
            // Insert before input line
            const inputLine = terminalContent.querySelector('.terminal-input-line');
            if (inputLine) {
                terminalContent.insertBefore(terminalLine, inputLine);
            }
        });
    }

    // Add button to terminal
    function addButton(buttonConfig) {
        const buttonLine = document.createElement('div');
        buttonLine.className = 'terminal-line';
        
        const button = document.createElement('a');
        button.href = buttonConfig.link;
        button.className = 'terminal-button';
        button.innerHTML = `
            ${buttonConfig.text}
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
        `;
        
        buttonLine.appendChild(button);
        const inputLine = terminalContent.querySelector('.terminal-input-line');
        if (inputLine) {
            terminalContent.insertBefore(buttonLine, inputLine);
        }
    }

    // Process command
    function processCommand(cmd) {
        const trimmedCmd = cmd.trim().toLowerCase();
        
        // Show command that was entered
        if (cmd.trim()) {
            addOutput([cmd], true);
        }
        
        if (trimmedCmd === '') {
            return;
        }
        
        if (trimmedCmd === 'clear') {
            // Clear all output except input line
            const inputLine = terminalContent.querySelector('.terminal-input-line');
            const firstLine = terminalContent.querySelector('.terminal-line:first-child');
            const secondLine = terminalContent.querySelector('.terminal-line:nth-child(2)');
            const thirdLine = terminalContent.querySelector('.terminal-line:nth-child(3)');
            
            terminalContent.innerHTML = '';
            if (firstLine) terminalContent.appendChild(firstLine);
            if (secondLine) terminalContent.appendChild(secondLine);
            if (thirdLine) terminalContent.appendChild(thirdLine);
            if (inputLine) terminalContent.appendChild(inputLine);
            return;
        }
        
        const command = commands[trimmedCmd];
        
        if (command) {
            if (command.output) {
                addOutput(command.output);
            }
            if (command.button) {
                addButton(command.button);
            }
        } else {
            addOutput([
                `<span class="terminal-error">Command not found: ${trimmedCmd}</span>`,
                'Type <span class="terminal-info">help</span> to see available commands.'
            ]);
        }
        
        // Add empty line for spacing
        addOutput([' ']);
        
        // Scroll to bottom
        setTimeout(() => {
            terminalContent.scrollTop = terminalContent.scrollHeight;
        }, 10);
    }

    // Handle Enter key in terminal input
    terminalInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            const command = terminalInput.value.trim();
            if (command) {
                processCommand(command);
                terminalInput.value = '';
            }
        }
    });

    // FIXED: Only focus input when clicking INSIDE the terminal card, not anywhere on page
    terminalContent.addEventListener('click', function(e) {
        // Only focus if clicking on terminal background, not on links/buttons
        if (e.target === terminalContent || e.target.classList.contains('terminal-line') || e.target.classList.contains('terminal-output')) {
            terminalInput.focus();
        }
    });

    // REMOVED: The aggressive blur refocus that was preventing navigation
    // terminalInput.addEventListener('blur', function() {
    //     setTimeout(() => this.focus(), 100);
    // });

})();