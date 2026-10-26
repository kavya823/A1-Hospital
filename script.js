// Initialize A1 Hospital Application
function initHospitalApp() {
    // Enable progressive scroll animations
    document.body.classList.add('reveal-active');

    const observerOptions = {
        root: null,
        rootMargin: '60px 0px',
        threshold: 0.05
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-up, .animate-left, .animate-right');
    animatedElements.forEach(el => observer.observe(el));

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 30) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        // Close mobile drawer on link tap
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768 && !link.classList.contains('dropdown-toggle')) {
                    navLinks.classList.remove('active');
                }
            });
        });
    }

    // Mobile dropdown toggle
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdown = document.querySelector('.dropdown');
    if (dropdownToggle && dropdown && window.innerWidth <= 768) {
        dropdownToggle.addEventListener('click', (e) => {
            // Only toggle dropdown if they click the chevron icon
            if (e.target.closest('svg') || e.target.closest('i')) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
            // Otherwise, it allows the default navigation to departments.html
        });
    }

    // Highlight active nav link (button should look dark like static way)
    let currentPage = window.location.pathname.split('/').pop();
    if (currentPage === '' || currentPage === '/') currentPage = 'index.html';
    
    const navItems = document.querySelectorAll('.nav-links > li > a:not(.btn-primary)');
    navItems.forEach(link => {
        const href = link.getAttribute('href');
        if (href && (href === currentPage || href.startsWith(currentPage + '#'))) {
            link.classList.add('active-link');
        }
    });

    // Set today as minimum date for appointment
    const dateInput = document.getElementById('appointment-date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.min = today;
        dateInput.value = today;
    }

    // Attach click listeners to all appointment links
    document.querySelectorAll('a[href="#appointment"]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            let docName = '';
            let deptName = '';

            // Detect if clicked from doctor card
            const docCard = link.closest('.doctor-card') || link.closest('.doctor-carousel-card');
            if (docCard) {
                const nameEl = docCard.querySelector('h3');
                if (nameEl) docName = nameEl.textContent.trim();
            }

            // Detect if clicked from department dropdown item
            if (link.closest('.dropdown-column')) {
                deptName = link.textContent.trim();
            }

            openAppointmentModal(docName, deptName);
        });
    });

    // Close modal on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeAppointmentModal();
        }
    });

    // Close modal on background click
    const modalOverlay = document.getElementById('appointment-modal');
    if (modalOverlay) {
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) {
                closeAppointmentModal();
            }
        });
    }

    // Initialize Home Page 3D Flip & Parallax and Detail Page Interactions
    setupHomePageInteractions();
    setupDetailPageInteractions();
    setupExplanationNavigation();
}

// Ensure execution whether DOMContentLoaded has already fired or is pending
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHospitalApp);
} else {
    initHospitalApp();
}

// Interactive 3D Cursor Parallax & Flip Animation (Home Page Only)
function setupHomePageInteractions() {
    const isHomePage = document.body.getAttribute('data-page') === 'home' || 
                       window.location.pathname.endsWith('index.html') || 
                       window.location.pathname === '/' || 
                       window.location.pathname === '';

    if (!isHomePage) return;

    const interactiveCards = document.querySelectorAll('.service-card, .dept-card-photo, .doctor-card, .emergency-compact-card');

    interactiveCards.forEach(card => {
        // Smooth luxury cursor parallax tilt
        card.addEventListener('mousemove', (e) => {
            if (card.classList.contains('is-flipping')) return;
            const rect = card.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            card.style.transform = `perspective(1000px) rotateY(${(x * 6).toFixed(2)}deg) rotateX(${(-y * 6).toFixed(2)}deg) translateY(-8px) scale3d(1.012, 1.012, 1.012)`;
        });

        // Smooth slip back on mouse leave
        card.addEventListener('mouseleave', () => {
            if (card.classList.contains('is-flipping')) return;
            card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0) scale3d(1, 1, 1)';
        });

        // Luxury micro-elevation bounce on click
        card.addEventListener('click', (e) => {
            if (e.target.closest('a') || e.target.closest('button') || e.target.closest('.card-action-link')) return;

            card.classList.add('is-flipping');
            setTimeout(() => {
                card.classList.remove('is-flipping');
                card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0) scale3d(1, 1, 1)';
            }, 550);
        });
    });
}

// Interactive 3D Cursor Parallax for Detail Pages & Showcase Cards
function setupDetailPageInteractions() {
    const tiltElements = document.querySelectorAll('.detail-arch-frame, .detail-cap-card, .service-showcase-card, .dept-showcase-card');
    tiltElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            el.style.transform = `perspective(1000px) rotateY(${(x * 8).toFixed(2)}deg) rotateX(${(-y * 8).toFixed(2)}deg) translateY(-6px)`;
        });
        el.addEventListener('mouseleave', () => {
            el.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0)';
        });
    });
}

// Navigation to Explanations on Services & Departments Pages
function setupExplanationNavigation() {
    // Intercept clicks on cards or links that navigate to explanations
    document.querySelectorAll('a[href^="#service-"], a[href^="#dept-"], .nav-to-explanation').forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href') || link.getAttribute('data-target');
            if (href && (href.startsWith('#service-') || href.startsWith('#dept-'))) {
                const targetId = href.substring(1);
                const targetEl = document.getElementById(targetId);
                if (targetEl) {
                    e.preventDefault();
                    targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    targetEl.classList.add('highlight-card');
                    setTimeout(() => {
                        targetEl.classList.remove('highlight-card');
                    }, 2600);
                }
            }
        });
    });

    // Check if page loaded directly with an explanation hash
    if (window.location.hash) {
        const hash = window.location.hash;
        if (hash.startsWith('#service-') || hash.startsWith('#dept-')) {
            setTimeout(() => {
                const targetEl = document.querySelector(hash);
                if (targetEl) {
                    targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    targetEl.classList.add('highlight-card');
                    setTimeout(() => {
                        targetEl.classList.remove('highlight-card');
                    }, 2600);
                }
            }, 350);
        }
    }
}

function scrollCarousel(carouselId, direction) {
    const track = document.getElementById(carouselId);
    if (!track) return;
    const scrollAmount = 304; 
    track.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}

/* Appointment Modal Functions */
function openAppointmentModal(doctorName = '', departmentName = '') {
    const modal = document.getElementById('appointment-modal');
    if (!modal) return;

    // Reset views
    const formView = document.getElementById('appointment-form-view');
    const successView = document.getElementById('appointment-success-view');
    if (formView) formView.style.display = 'block';
    if (successView) successView.style.display = 'none';

    // Auto-select doctor if matched
    const docSelect = document.getElementById('appointment-doctor');
    if (docSelect && doctorName) {
        let matched = false;
        for (let i = 0; i < docSelect.options.length; i++) {
            if (docSelect.options[i].value.toLowerCase().includes(doctorName.toLowerCase()) ||
                doctorName.toLowerCase().includes(docSelect.options[i].text.toLowerCase())) {
                docSelect.selectedIndex = i;
                matched = true;
                break;
            }
        }
        if (!matched && doctorName) {
            // Add custom option or select first
            const newOption = new Option(doctorName, doctorName, true, true);
            docSelect.add(newOption);
        }
    }

    // Auto-select department if matched
    const deptSelect = document.getElementById('appointment-dept');
    if (deptSelect && departmentName) {
        for (let i = 0; i < deptSelect.options.length; i++) {
            if (deptSelect.options[i].text.toLowerCase().includes(departmentName.toLowerCase())) {
                deptSelect.selectedIndex = i;
                break;
            }
        }
    }

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Refresh lucide icons inside modal if needed
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

function closeAppointmentModal() {
    const modal = document.getElementById('appointment-modal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

function handleAppointmentSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const name = form.patient_name.value.trim();
    const phone = form.patient_phone.value.trim();
    const dept = form.department.value;
    const doctor = form.doctor.value || 'Any Available Specialist';
    const date = form.preferred_date.value;
    const time = form.time_slot.value;
    const notes = form.notes.value.trim();

    // Prepare WhatsApp Confirmation Link
    const waPhone = '916399144444';
    let waMessage = `*A1 Hospital Appointment Request*\n` +
                    `*Patient Name:* ${name}\n` +
                    `*Contact:* ${phone}\n` +
                    `*Department:* ${dept}\n` +
                    `*Doctor:* ${doctor}\n` +
                    `*Preferred Date:* ${date}\n` +
                    `*Preferred Time:* ${time}`;
    if (notes) {
        waMessage += `\n*Symptoms/Notes:* ${notes}`;
    }

    const waUrl = `https://wa.me/${waPhone}?text=${encodeURIComponent(waMessage)}`;
    const waBtn = document.getElementById('whatsapp-confirm-btn');
    if (waBtn) {
        waBtn.href = waUrl;
    }

    const summaryText = document.getElementById('success-summary-text');
    if (summaryText) {
        summaryText.innerHTML = `Thank you <strong>${name}</strong>! Your appointment request with <strong>${doctor}</strong> (${dept}) for <strong>${date}</strong> (${time}) has been noted. Our hospital desk will verify your slot promptly.`;
    }

    // Toggle views
    const formView = document.getElementById('appointment-form-view');
    const successView = document.getElementById('appointment-success-view');
    if (formView) formView.style.display = 'none';
    if (successView) {
        successView.style.display = 'block';
        if (window.lucide) window.lucide.createIcons();
    }

    form.reset();
}

