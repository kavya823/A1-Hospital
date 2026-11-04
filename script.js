// Medical ECG Page-to-Page Transition Animation (0.5s Swift Dissolve)
function initPageTransition() {
    if (window.__hospitalTransitionInitialized) return;
    window.__hospitalTransitionInitialized = true;

    const overlay = document.getElementById('hospital-page-transition');
    if (!overlay) return;

    let hasFaded = false;
    const hideTransition = () => {
        if (hasFaded) return;
        hasFaded = true;
        overlay.classList.add('transition-fade-out');
        overlay.classList.remove('transition-active');
        overlay.setAttribute('aria-hidden', 'true');
    };

    // Stays visible for ~250ms, then smoothly dissolves over 250ms (total ~0.5s)
    const displayTimer = setTimeout(hideTransition, 250);

    // Safety fallback
    setTimeout(hideTransition, 600);

    // Intercept internal page switching clicks for smooth transition
    document.addEventListener('click', (e) => {
        // If user held modifier keys (new tab/window) or not primary click, skip
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) {
            return;
        }

        const link = e.target.closest('a');
        if (!link) return;

        const href = link.getAttribute('href');
        if (!href) return;

        // Skip anchor jumps, phone calls, email links, js actions, blank targets, downloads
        if (
            href.startsWith('#') ||
            href.startsWith('tel:') ||
            href.startsWith('mailto:') ||
            href.startsWith('javascript:') ||
            link.getAttribute('target') === '_blank' ||
            link.hasAttribute('download')
        ) {
            return;
        }

        // Determine destination URL
        let targetUrl;
        try {
            targetUrl = new URL(link.href, window.location.href);
        } catch (err) {
            return;
        }

        // Only transition for same-origin internal pages
        if (targetUrl.origin !== window.location.origin) {
            return;
        }

        // If clicking on same page with an anchor hash (e.g. index.html#appointment)
        if (targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) {
            if (targetUrl.hash) return;
        }

        e.preventDefault();
        clearTimeout(displayTimer);

        // Re-display transition overlay for page switch
        overlay.classList.remove('transition-fade-out');
        overlay.classList.add('transition-active');
        overlay.setAttribute('aria-hidden', 'false');

        // Swift handoff delay so user sees transition before browser navigation
        setTimeout(() => {
            window.location.href = link.href;
        }, 75);
    });

    // Handle browser back / forward cache gracefully
    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {
            hideTransition();
        }
    });
}

// Immediate invocation for instantaneous transition timing
initPageTransition();

// Initialize A1 Hospital Application
function initHospitalApp() {
    initPageTransition();
    initCounterAnimation();

    // Universal Succession Entrance, Pop & 3D Interactive Engines
    initSuccessionScrollAnimations();
    initMinimalContentCursorEffects();
    initSmallFramePopAnimations();
    initPhotoFlippingAnd3D();

    // Render Lucide icons if loaded
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
        window.lucide.createIcons();
    }

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
            let deptName = '';

            // Detect if clicked from department dropdown item
            if (link.closest('.dropdown-column')) {
                deptName = link.textContent.trim();
            }

            openAppointmentModal('', deptName);
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

    // Navigation to explanation anchors
    setupExplanationNavigation();
}

// Ensure execution whether DOMContentLoaded has already fired or is pending
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHospitalApp);
} else {
    initHospitalApp();
}

// ==========================================================================
// 1. UNIVERSAL SUCCESSION SCROLL REVEAL (SLOW, VISIBLE STAGGERED ENTRANCE)
// ==========================================================================
function initSuccessionScrollAnimations() {
    document.body.classList.add('reveal-active');

    // Automatically discover grids and card groups across ALL pages to apply staggered succession
    const staggerContainers = document.querySelectorAll(
        '.services-grid, .dept-grid-home, .doctors-grid, .blog-grid, ' +
        '.pinnacle-counter-strip, .detail-cap-grid, .detail-hero-content, ' +
        '.hero-content, .smera-hero-duo-wrapper, .hospital-intro-grid, ' +
        '.reception-facility-card, .detail-explore-others .carousel-track, ' +
        '.service-showcase-grid, .dept-showcase-grid'
    );

    staggerContainers.forEach(container => {
        container.classList.add('stagger-container');
        const children = Array.from(container.children).filter(child => {
            return !child.classList.contains('carousel-btn') && child.tagName !== 'SCRIPT';
        });

        children.forEach((child, index) => {
            child.classList.add('stagger-item');
            child.style.setProperty('--stagger-i', index);
            if (!child.style.transitionDelay && !child.className.includes('delay-')) {
                child.style.transitionDelay = `${(index * 0.11).toFixed(2)}s`;
            }
        });
    });

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.08
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                entry.target.classList.add('in-view');

                // Trigger child cards smoothly
                const innerCards = entry.target.querySelectorAll('.stagger-item, .service-card, .doctor-card, .dept-card-photo, .blog-card, .pinnacle-stat-col, .dept-showcase-card, .service-showcase-card, .detail-cap-card');
                innerCards.forEach(item => {
                    item.classList.add('show');
                    item.classList.add('in-view');
                });
            }
        });
    }, observerOptions);

    const animatables = document.querySelectorAll(
        '.framed-section, .hero, .animate-up, .animate-left, .animate-right, ' +
        '.animate-pop, .stagger-container, .stagger-item, .doctor-card, ' +
        '.service-card, .dept-card-photo, .blog-card, .dept-showcase-card, ' +
        '.service-showcase-card, .pinnacle-counter-strip, .hospital-intro-section, ' +
        '.reception-desk-section, .detail-cap-card'
    );

    animatables.forEach(el => sectionObserver.observe(el));

    // Immediate soft reveal for above-the-fold content upon page view
    setTimeout(() => {
        animatables.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                el.classList.add('show');
                el.classList.add('in-view');
                el.querySelectorAll('.stagger-item').forEach(si => {
                    si.classList.add('show');
                    si.classList.add('in-view');
                });
            }
        });
    }, 120);
}

// ==========================================================================
// 2. CURSOR MICRO-INTERACTIONS FOR MINIMAL / LESS-CONTENT ELEMENTS
// ==========================================================================
function initMinimalContentCursorEffects() {
    const minimalElements = document.querySelectorAll(
        '.doctor-dept-pill, .doctor-tag, .doc-exp-chip, .pinnacle-stat-col, ' +
        '.hospital-intro-para-card, .reception-phone-pill, .detail-cap-card, ' +
        '.detail-feature-item, .emergency-compact-card, .blog-filter-pill, ' +
        '.duo-doc-experience-tag, .dept-info, .service-photo-badge, ' +
        '.card-icon-badge, .doctor-emblem-badge, .dept-badge, .service-showcase-badge'
    );

    minimalElements.forEach(el => {
        el.classList.add('minimal-interactive');

        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = (((e.clientX - rect.left) / rect.width) * 100).toFixed(1);
            const y = (((e.clientY - rect.top) / rect.height) * 100).toFixed(1);
            el.style.setProperty('--cursor-x', `${x}%`);
            el.style.setProperty('--cursor-y', `${y}%`);
        });

        el.addEventListener('mouseleave', () => {
            el.style.removeProperty('--cursor-x');
            el.style.removeProperty('--cursor-y');
        });
    });
}

// ==========================================================================
// 3. POP ANIMATION FOR SMALL FRAMES & BADGES (SERVICES & DEPARTMENTS)
// ==========================================================================
function initSmallFramePopAnimations() {
    const smallFrames = document.querySelectorAll(
        '.service-card-photo-frame, .pharmacy-carousel-photo-frame, ' +
        '.service-showcase-photo-frame, .dept-showcase-header-box, ' +
        '.service-photo-badge, .card-icon-badge, .doctor-emblem-badge, ' +
        '.dept-badge, .detail-floating-badge, .dept-card-photo, .duo-arch-frame'
    );

    smallFrames.forEach(frame => {
        frame.classList.add('pop-frame');

        // Tactile micro-press feedback
        frame.addEventListener('mousedown', () => {
            frame.style.transform = 'scale(0.96) translateY(0)';
        });
        frame.addEventListener('mouseup', () => {
            frame.style.removeProperty('transform');
        });
    });
}

// ==========================================================================
// 4. 3D PHOTO FLIPPING & PERSPECTIVE PARALLAX SYSTEM (ALL PAGES)
// ==========================================================================
function initPhotoFlippingAnd3D() {
    // A. 3D Photo Flip Cards (Doctors, Founders & Leaders)
    const flipCards = document.querySelectorAll('.photo-flip-frame, .duo-arch-frame.photo-flip-frame');

    flipCards.forEach(card => {
        card.setAttribute('tabindex', '0');

        card.addEventListener('click', (e) => {
            // Don't toggle flip if user clicked direct booking button on the back
            if (e.target.closest('.btn-flip-book') || e.target.closest('a')) return;
            card.classList.toggle('is-flipped');
        });

        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                card.classList.toggle('is-flipped');
            }
        });
    });

    // B. Interactive 3D Cursor Parallax & Depth on All Cards & Photos (All Pages)
    const tiltCards = document.querySelectorAll(
        '.service-card, .dept-card-photo, .doctor-card, .emergency-compact-card, ' +
        '.dept-showcase-card, .service-showcase-card, .detail-arch-frame, ' +
        '.hospital-building-card, .reception-img-frame'
    );

    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            // If the card has a 3D flip photo that is currently flipped, avoid tilt conflict
            if (card.querySelector('.photo-flip-frame.is-flipped')) return;

            const rect = card.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;
            card.style.transform = `perspective(1000px) rotateY(${(x * 7).toFixed(2)}deg) rotateX(${(-y * 7).toFixed(2)}deg) translateY(-8px) scale3d(1.015, 1.015, 1.015)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0) scale3d(1, 1, 1)';
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
function openAppointmentModal(param1 = '', param2 = '') {
    const modal = document.getElementById('appointment-modal');
    if (!modal) return;

    // Reset views
    const formView = document.getElementById('appointment-form-view');
    const successView = document.getElementById('appointment-success-view');
    if (formView) formView.style.display = 'block';
    if (successView) successView.style.display = 'none';

    // Auto-select department if provided
    const departmentName = param2 || param1;

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
    const doctor = (form.doctor && form.doctor.value) ? form.doctor.value : 'Hospital Specialist';
    const date = form.preferred_date.value;
    const time = form.time_slot.value;
    const notes = form.notes.value.trim();

    // 1. Prepare Hospital Email Draft (a1hospitalsrikakulam@gmail.com)
    const hospitalEmail = 'a1hospitalsrikakulam@gmail.com';
    const emailSubject = `New Appointment Booking Request - ${name} - A1 Hospital`;
    const emailBody = 
`==================================================
A1 HOSPITAL SRIKAKULAM - APPOINTMENT BOOKING DETAILS
==================================================
Patient Name:     ${name}
Contact Number:   ${phone}
Department:       ${dept}
Preferred Doctor: ${doctor}
Preferred Date:   ${date}
Time Slot:        ${time}
Symptoms / Notes: ${notes ? notes : 'None specified'}
==================================================
Submitted through A1 Hospital Official Web Portal (www.a1hospitalsrikakulam.com)
Direct Contact:   ${phone}
Hospital Email:   ${hospitalEmail}`;

    const mailtoUrl = `mailto:${hospitalEmail}?subject=${encodeURIComponent(emailSubject)}&body=${encodeURIComponent(emailBody)}`;

    // Automatically trigger user's mail application to drag details to hospital email
    const mailLink = document.createElement('a');
    mailLink.href = mailtoUrl;
    mailLink.style.display = 'none';
    document.body.appendChild(mailLink);
    mailLink.click();
    document.body.removeChild(mailLink);

    // Update Email Confirmation Button in Success Modal
    const emailBtn = document.getElementById('email-confirm-btn');
    if (emailBtn) {
        emailBtn.href = mailtoUrl;
    }

    // 2. Prepare WhatsApp Confirmation Link
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

    // 3. Update Success Modal Summary Text
    const summaryText = document.getElementById('success-summary-text');
    if (summaryText) {
        summaryText.innerHTML = `Thank you <strong>${name}</strong>! Your appointment request with <strong>${doctor}</strong> (${dept}) for <strong>${date}</strong> (${time}) has been generated for <strong>${hospitalEmail}</strong>. Our hospital desk will verify your slot promptly.`;
    }

    // 4. Toggle views
    const formView = document.getElementById('appointment-form-view');
    const successView = document.getElementById('appointment-success-view');
    if (formView) formView.style.display = 'none';
    if (successView) {
        successView.style.display = 'block';
        if (window.lucide) window.lucide.createIcons();
    }

    form.reset();
}

// Blog Filter & Interactive Modal Functions
function filterBlog(category, pillElem) {
    document.querySelectorAll('.blog-filter-pill').forEach(btn => btn.classList.remove('active'));
    if (pillElem) pillElem.classList.add('active');
    
    const cards = document.querySelectorAll('.blog-card');
    cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

function openArticleModal(title, category, date, readTime, encodedContent) {
    const modal = document.getElementById('article-modal');
    if (!modal) return;
    
    document.getElementById('modal-article-title').textContent = title;
    document.getElementById('modal-article-category').textContent = category;
    document.getElementById('modal-article-meta').textContent = `${date} · ${readTime}`;
    document.getElementById('modal-article-body').innerHTML = decodeURIComponent(encodedContent);
    
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (window.lucide) window.lucide.createIcons();
}

function closeArticleModal() {
    const modal = document.getElementById('article-modal');
    if (!modal) return;
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

/* ==========================================================================
   PINNACLE-INSPIRED DYNAMIC NUMBER COUNTER ANIMATION ENGINE
   Reference: pinnaclehospitals.com (Smooth easing, comma formatting, suffix support)
   ========================================================================== */
function initCounterAnimation() {
    const counterElements = document.querySelectorAll('[data-counter]');
    if (!counterElements.length) return;

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                animateSingleCounter(el);
                observer.unobserve(el); // Fire once per session for crisp UX
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -30px 0px'
    });

    counterElements.forEach(el => counterObserver.observe(el));
}

function animateSingleCounter(el) {
    const targetValue = parseInt(el.getAttribute('data-counter'), 10);
    if (isNaN(targetValue)) return;

    const prefix = el.getAttribute('data-prefix') || '';
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = parseInt(el.getAttribute('data-duration'), 10) || (targetValue > 1000 ? 1900 : 1300);

    let startTime = null;

    // Smooth cubic ease-out curve (decelerates into final number)
    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    function step(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easedProgress = easeOutCubic(progress);

        const currentVal = Math.floor(easedProgress * targetValue);
        el.textContent = `${prefix}${currentVal.toLocaleString('en-US')}${suffix}`;

        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            el.textContent = `${prefix}${targetValue.toLocaleString('en-US')}${suffix}`;
            el.classList.add('counter-completed');
        }
    }

    // Set initial zero display and trigger animation frame
    el.textContent = `${prefix}0${suffix}`;
    requestAnimationFrame(step);
}
