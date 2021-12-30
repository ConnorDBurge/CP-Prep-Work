const showMore = () => {
    let button = document.getElementById('more-btn');
    let section = document.getElementById('profile-more');
    if (button.innerHTML === 'More') {
        section.style.display = 'block';
        button.classList.remove('grey-outline-btn');
        button.classList.add('red-btn');
        button.style.paddingLeft = "10px";
        button.style.paddingRight = "10px";
        button.innerHTML = '&#10007;'
    } else {
        section.style.display = 'none';
        button.innerHTML = "More";
        button.classList.add('grey-outline-btn');
        button.classList.remove('red-btn');
    }
}

const follow = () => {
    let button = document.getElementById('follow-btn');
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

