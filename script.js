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

    const animatedElements = document.querySelectorAll('.animate-up, .animate-fade, .animate-left, .animate-right');
    animatedElements.forEach(el => observer.observe(el));
});

function scrollCarousel(carouselId, direction) {
    const track = document.getElementById(carouselId);
    if (!track) return;
    const scrollAmount = 304; 
    track.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}
