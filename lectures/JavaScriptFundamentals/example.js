// 'string'
// "string"
// `string`
let firstName = 'Connor';
let lastName = 'Burge';
console.log(`${firstName} ${lastName}`);

// 55 integer
// 3.14 float point number
console.log(1 + 2);
console.log(1 - 2);
console.log(1 * 2);
console.log(1 / 2);
console.log(1 ** 2);
console.log(1 % 2);

// true, false  Booleans
console.log(3 == 3); // true
console.log(3 == '3'); // true
console.log(3 === '3'); // false
console.log(1 !== 4); // true
console.log(1 >= 4); // false
console.log(1 === 1 && 4 % 2 === 0); // true AND true = true
console.log(1 === 1 || 4 % 2 === 1); // true OR false = true
console.log(!true); // false
console.log(!false); // true

// undefined, the value that hasn't been defined
// null, explicitly this has no value

let numbers = [1, 2, 3, 4, 5, 'strings', [1, 2], { key: 'value' }];
console.log(numbers[2]);

// Objects
let user = {
    'name': 'Tom',
    'age': 35
}
console.log(user['name']); // preferred method
console.log(user.age);

// Variables
var age = 25; // can change and be re-declared
let age1 = 25; // global scope, cam be changed but not re-declared
const age2 = 25; // is final

// Functions
function fullName1(firstName, lastName) { // Regular
    return `${firstName} ${lastName}`;
}

const fullName = (firstName, lastName) => { // Fat arrow
    return `${firstName} ${lastName}`;
}

// If statements
if (true) {
    // return;
} else if (true) {
    // return;
} else {
    // return;
}

// Loops
// For loop
for (let i = 0; i < 10; i++) {
    console.log(i);
}
// While
let x = 0;
while (x > 100) {
    x++;
}
// For each
for (let key in user) {
    console.log(user[key]);
}

let numbers1 = [1, 2, 3, 4, 5];
numbers.push(6); // push to back
console.log(numbers);
numbers.unshift(0); // adds to front
console.log(numbers);
numbers.pop(); // takes off 6
console.log(numbers);
numbers.shift(); // takes off front
console.log(numbers);