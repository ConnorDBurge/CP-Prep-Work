let nextListId = 0;
let taskList = [];
const taskListKey = 'tasks';

initializeData();
function initializeData() {
    let stringData = localStorage.getItem(taskListKey);
    if (stringData) { // if data is stored
        taskList = JSON.parse(stringData); // opposite of JSON.stringify()
        for (let i = 0; i < taskList.length; i++) {
            addTaskToPage(taskList[i]);
        }
    }
}

const addTask = () => {
    // find input element
    let input = document.querySelector('#input-task');
    // grab text from input
    let taskName = input.value;
    addTaskToPage(taskName);
    // add task to taskList for local localStorage
    taskList.push(taskName);
    let stringData = JSON.stringify(taskList)
    localStorage.setItem(taskListKey, stringData);
    input.value = '';
}

function addTaskToPage(taskName) {
    // find existing list element
    let taskListElement = document.querySelector('#to-do-list');
    // create a new list item
    let newListItem = document.createElement('li');
    newListItem.id = `list-item-${nextListId++}`; // assign, then increment
    newListItem.classList.add('list-group-item');
    newListItem.addEventListener('click', toggleItemState);
    // add text as a list item
    newListItem.innerHTML = taskName;
    // add list item to existing list
    taskListElement.appendChild(newListItem);
}

function toggleItemState(element) {
    // get item
    let listItem = document.getElementById(element.target.id);
    // change strike-through state
    let isCheckedOff = listItem.style.textDecoration === 'line-through'
    listItem.style.textDecoration = isCheckedOff ? 'none' : 'line-through';
    listItem.style.color = isCheckedOff ? 'white' : 'red';
}
