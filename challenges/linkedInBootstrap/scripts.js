let lastKnownScrollPosition = 0;
let ticking = false;

function doSomething(scrollPos) {
    if (scrollPos > 400) {
        dropNav = document.querySelector("#drop-nav");
        dropNav.classList.remove("d-none");
    }
    if (scrollPos <= 400) {
        dropNav = document.querySelector("#drop-nav");
        dropNav.classList.add("d-none");
    }
}

document.addEventListener('scroll', function (e) {
    lastKnownScrollPosition = window.scrollY;

    if (!ticking) {
        window.requestAnimationFrame(function () {
            doSomething(lastKnownScrollPosition);
            ticking = false;
        });

        ticking = true;
    }
});