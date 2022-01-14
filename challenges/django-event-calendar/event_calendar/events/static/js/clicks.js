const displayForm = () => {
    const event_form = document.querySelector('#new-event-form');
    if (event_form.classList.contains('display-flex')) {
        event_form.classList.remove('display-flex');
    } else {
        event_form.classList.add('display-flex');
    }
}