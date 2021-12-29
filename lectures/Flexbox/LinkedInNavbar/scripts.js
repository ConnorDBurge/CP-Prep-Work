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