// =========================================================
// SCROLL ANIMATIONS · PREMIUM
// =========================================================

document.addEventListener("DOMContentLoaded", function () {

    const elements = document.querySelectorAll(".reveal, .reveal-up, .reveal-left, .reveal-right, .section-fade");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                    observer.unobserve(entry.target);
                }
            });
        },
        {
            threshold: 0.15
        }
    );

    elements.forEach((el) => {
        observer.observe(el);
    });

});
