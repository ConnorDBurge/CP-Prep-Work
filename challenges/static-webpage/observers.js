//
// 
// 
// Change Navbar Color
const navbar = document.querySelector('#navbar');
const productSection = document.querySelector('#product');
const productSectionOptions = {
    rootMargin: '-52px 0px 0px 0px'
}
const productSectionObserver = new IntersectionObserver(function (entries, productSectionObserver) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) { // is productSection is off the page
            navbar.classList.add('light-mode');
        } else { // if productSection is on the page
            navbar.classList.remove('light-mode');
        }
    })
}, productSectionOptions);
productSectionObserver.observe(productSection);

// 
// 
// 
// Appear class Intersection Observer
const appearOptions = {
    rootMargin: "0px 0px -100px 0px"
}
const appearObserver = new IntersectionObserver(function (entries, appearObserver) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add('appear');
            appearObserver.unobserve(entry.target);
        }
    })
}, appearOptions);
// Sliders for Product Section
const sliders = document.querySelectorAll('.slide-in');
sliders.forEach(slider => {
    appearObserver.observe(slider);
});
// Faders for Portfolio Section
const faders = document.querySelectorAll('.portfolio-item');
faders.forEach(fader => {
    appearObserver.observe(fader);
})
