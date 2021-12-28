let random = 0;
const pickRandomNumber = () => {
    random = Math.ceil(Math.random() * 100);
    console.log(random);
}
pickRandomNumber(); // runs on load page

document.getElementById('submit').onclick = () => {
    const inputNumber = document.getElementById('input-number')
    let userNumber = inputNumber.value;
    inputNumber.value = '';
    addNumberToList(userNumber);
    return checkNumber(+userNumber);
}

const checkNumber = (number) => {
    let message = document.getElementById('game-message');
    if (number === random) {
        message.innerHTML = 'You won!'
    } else if (number > random) {
        message.innerHTML = 'Guess Lower!'
    } else {
        message.innerHTML = 'Guess Higher!'
    }
}

const addNumberToList = (number) => {
    let newElem = document.createElement('LI');
    const node = document.createTextNode(number);
    newElem.appendChild(node);
    const list = document.getElementById('number-list');
    list.appendChild(newElem);
}

const doesUserExist = () => {
    if (localStorage.getItem('user-name')) {
        let name = localStorage.getItem('user-name');
        document.getElementById('welcome').innerHTML = `Welcome ${name}!`;
        return document.getElementById('get-username').remove();
    }
}

document.getElementById('submit-username').onclick = () => {
    const userName = document.getElementById('user-name').value;
    if (userName.length > 0) {
        localStorage.setItem('user-name', document.getElementById('user-name').value);
        document.getElementById('user-name').value = '';
        return doesUserExist();
    }
}
doesUserExist();