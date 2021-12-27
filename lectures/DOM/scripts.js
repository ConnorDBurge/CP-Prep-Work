const nameKey = "name"

window.onload = () => {
    let greetingOutput = document.getElementById("output");
    if (!greetingOutput) {
        return;
    }

    let name = localStorage.getItem(nameKey);
    if (name !== "") {
        greetingOutput.innerHTML = "Hello " + name + "!"
    }

    greetingOutput.addEventListener("click", () => {
        greetingOutput.innerHTML = ""
    })
}

const showGreeting = () => {
    let nameInput = document.getElementById("input-name")
    let greetingOutput = document.getElementById("output")
    if (nameInput && greetingOutput) {
        let name = nameInput.value
        localStorage.setItem(nameKey, name)
        greetingOutput.innerHTML = "Hello " + nameInput.value + "!"
    }
}