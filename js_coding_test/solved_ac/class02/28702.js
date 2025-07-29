// FizzBuzz
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let string1 = inputData[0];
let string2 = inputData[1];
let string3 = inputData[2];

let answer = 0;
if (string1[0] !== "F" && string1[0] !== "B") {
    answer = parseInt(string1) + 3;
} else if (string2[0] !== "F" && string2[0] !== "B") {
    answer = parseInt(string2) + 2;
} else if (string3[0] !== "F" && string3[0] !== "B") {
    answer = parseInt(string3) + 1;
}

if (answer % 3 === 0 && answer % 5 === 0) {
    console.log("FizzBuzz");
} else if (answer % 3 === 0 && answer % 5 !== 0) {
    console.log("Fizz");
} else if (answer % 3 !== 0 && answer % 5 === 0) {
    console.log("Buzz");
} else {
    console.log(answer);
}