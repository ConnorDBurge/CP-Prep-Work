
const nameKey = "name"

window.onload = () => {
    let greetingOutput = document.querySelector("#greeting");
    let name = localStorage.getItem(nameKey)

    if (name) {
        let nameInput = document.querySelector("#form")
        nameInput.style.display = "none";
        greetingOutput.innerHTML = "Hello " + name + "!"
    }
}

const showGreeting = () => {
    let nameInput = document.querySelector("#name")
    let greetingOutput = document.querySelector("#greeting")
    if (nameInput && greetingOutput) {
        let name = nameInput.value
        localStorage.setItem(nameKey, name)
    }
}