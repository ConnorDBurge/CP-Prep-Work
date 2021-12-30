const smallDropNav = () => {
    let dropNav = document.getElementById('drop-nav');
    if (dropNav.style.display === 'flex') {
        dropNav.style.display = 'none';
    } else {
        dropNav.style.display = 'flex';
    }
}

const showMore = () => {
    let button = document.getElementById('more-btn');
    let section = document.getElementById('profile-more');
    if (button.value === 'More') {
        section.style.display = 'block';
        button.style.backgroundColor = "#EBEBEB";
        button.value = 'Close';
    } else if (button.value === 'Close') {
        section.style.display = 'none';
        button.style.backgroundColor = "white";
        button.value = 'More';
    }
}

const follow = () => {
    let button = document.getElementById('follow-btn');
    let prompt = document.getElementById('follow-prompt');
    if (button.innerHTML === "Follow") {
        button.innerHTML = "&#x2714;";
        button.style.paddingLeft = "10px";
        button.style.paddingRight = "10px";
        button.classList.remove('blue-outline-btn');
        button.classList.add('green-btn');
    } else {
        button.innerHTML = "Follow";
        button.classList.add('blue-outline-btn');
        button.classList.remove('green-btn');
    }
}