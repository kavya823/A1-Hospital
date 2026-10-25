// Intersection Observer for scroll animations
document.addEventListener("DOMContentLoaded", () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.animate-up, .animate-fade, .animate-left, .animate-right, .animate-zoom, .animate-flip, .framed-section');
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
});

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
    const waPhone = '919193774444';
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

