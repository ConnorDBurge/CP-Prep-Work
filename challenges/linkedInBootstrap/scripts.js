// let lastKnownScrollPosition = 0;
// let ticking = false;

// function doSomething(scrollPos) {
//     if (scrollPos > 400) {
//         dropNav = document.querySelector("#drop-nav");
//         dropNav.classList.remove("d-none");
//     }
//     if (scrollPos <= 400) {
//         dropNav = document.querySelector("#drop-nav");
//         dropNav.classList.add("d-none");
//     }
// }

// document.addEventListener('scroll', function (e) {
//     lastKnownScrollPosition = window.scrollY;

//     if (!ticking) {
//         window.requestAnimationFrame(function () {
//             doSomething(lastKnownScrollPosition);
//             ticking = false;
//         });

//         ticking = true;
//     }
// });

let navLogo = document.querySelector('.global-nav__logo');
let navLogoClicks = 0;
navLogo.addEventListener('click', () => {
    navLogoClicks++;
    if (navLogoClicks % 2 == 0) {
        navLogo.style.color = 'rgb(10, 81, 151)'
    } else {
        navLogo.style.color = '#C37D16';
    }
})

function dismiss() {
    let elem = document.querySelector('.offer-me');
    elem.style.display = 'none';
}

function more() {
    let elem = document.querySelector('.offer-me');
    elem.style.display = '';
}

function closeAd() {
    let elem1 = document.querySelector('#ad-content');
    let elem2 = document.querySelector('#ad-button')
    if (elem1.style.display === 'none') {
        elem1.style.display = ''
        elem2.style.margin = ''
    } else {
        elem1.style.display = 'none'
        elem2.style.margin = '0 0 0 0'
    }
}

function follow() {
    let elem = document.querySelector("#follow-button");
    elem.innerHTML = 'Following'
    elem.style.border = '2px solid rgb(7, 65, 122)';
    elem.style.backgroundColor = 'rgb(220, 237, 253)';
    elem.style.color = 'rgb(7, 65, 122)';
    elem.style.pointerEvents = 'none';
}

function rotate() {
    let elem = document.querySelector("#head-shot");
    elem.classList.add('rotated-image')
}

let input = document.querySelector("#open-to-text");
let button = document.querySelector("#open-btn");
button.addEventListener('click', () => {

    if (button.innerHTML === 'Save') {
        button.innerHTML = 'Open to';
        button.style.backgroundColor = 'rgb(10, 102, 194)'
        input.style.display = 'none';
        if (input.value !== '') {
            let name = document.querySelector('#name');
            name.innerHTML = input.value;
        }
        input.value = '';
    } else {
        input.style.display = 'inline';
        button.innerHTML = 'Save';
        button.style.backgroundColor = '#C37D16'
    }
})

function openTo() {



}