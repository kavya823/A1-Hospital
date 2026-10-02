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
});

function scrollCarousel(carouselId, direction) {
    const track = document.getElementById(carouselId);
    if (!track) return;
    const scrollAmount = 304; 
    track.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}
