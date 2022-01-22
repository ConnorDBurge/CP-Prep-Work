// Filter function => [2,4,6]
/* "Filter the array to return only the even numbers." */
const arr = [1, 2, 3, 4, 5, 6, 7];
const evenNumbers = arr.filter((a) =>
    a % 2 === 0 // returns True or False
)

// Map function
/* Mapping each element in the array to a new value. */
const arr1 = [1, 2, 3, 4, 5, 6, 7];
const mapNumbers = arr1.map((a) =>
    a * 2
)

// Reduce function
/* Adding all the numbers in the array together. */
const arr2 = [1, 2, 3, 4, 5, 6, 7];
const sumNumbers = arr2.reduce((a, b) =>
    a + b
)

// Sum of even squares
/* 
1. Filter the array to only include even numbers.
2. Square each of the even numbers.
3. Sum the squares of the even numbers. 
*/
const arr3 = [1, 2, 3, 4, 5, 6, 7];
const sum = arr3
    .filter((a) => a % 2 === 0)
    .map((a) => a * a)
    .reduce((a, b) => a + b)
console.log(sum)


const orders = [
    {
        userId: 1,
        amount: 10
    },
    {
        userId: 1,
        amount: 15
    }, {
        userId: 2,
        amount: 5
    },
    {
        userId: 2,
        amount: 100
    }
];

/* Filter the orders for the user with ID 1, then map the orders to their amounts, and finally reduce
the mapped amounts to get the total. */
const a = orders
    .filter((order) => order.userId === 1)
    .map(order => order.amount)
    .reduce((a, b) => a + b)
console.log(a)