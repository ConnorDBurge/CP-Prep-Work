const showAdditionalInfo = () => {
    const additionalInfo = document.querySelector('#add_info_text')
    if (additionalInfo.style.display == 'none') {
        additionalInfo.style.display = 'block'
    } else {
        additionalInfo.style.display = 'none'
    }
}