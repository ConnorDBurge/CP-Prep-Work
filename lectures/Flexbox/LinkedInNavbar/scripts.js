const smallDropNav = () => {
    let dropNav = document.getElementById('drop-nav');
    if (dropNav.style.display === 'flex') {
        dropNav.style.display = 'none';
    } else {
        dropNav.style.display = 'flex';
    }
}