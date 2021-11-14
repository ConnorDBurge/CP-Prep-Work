var ls = require("./linearSearch");
var shallowEqualArrays = require('shallow-equal/arrays');

console.log(`${ls.linearSearch(3, [1, 2, 3]) === 2}: ${ls.linearSearch(3, [1, 2, 3])}`);
console.log(`${ls.linearSearch(4, [1, 2, 3]) === undefined}: ${ls.linearSearch(4, [1, 2, 3])}`);
console.log(`${ls.linearSearch(13, [1, 2, 3]) === undefined}: ${ls.linearSearch(13, [1, 2, 3])}`);
console.log(`${ls.linearSearch(1, [1, 2, 3]) === 0}: ${ls.linearSearch(1, [1, 2, 3])}`);
console.log(`${ls.linearSearch(4, [1, 2, 3, 4]) === 3}: ${ls.linearSearch(4, [1, 2, 3, 4])}`);

// console.log(shallowEqualArrays(ls.linearSearchGlobal("a", ["b", "a", "n", "a", "n", "a", "s"]), [1, 3, 5]))
// console.log(shallowEqualArrays(ls.linearSearchGlobal("s", ["b", "a", "n", "a", "n", "a", "s"]), [6]))
// console.log(shallowEqualArrays(ls.linearSearchGlobal("n", ["b", "a", "n", "a", "n", "a", "s"]), [2, 4]))
