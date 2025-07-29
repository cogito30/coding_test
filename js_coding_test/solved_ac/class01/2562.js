// A + B - C
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let num = 0;
let maxNum = parseInt(inputData[0]);
let maxIndex = 0;
for (let i = 0; i < 9; ++i) {
    num = parseInt(inputData[i]);
    if (maxNum < num) {
        maxNum = num;
        maxIndex = i;
    }
}
console.log(maxNum);
console.log(maxIndex + 1);

/*
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

const maxNum = Math.max(...input);
const indexNum = input.indexOf(maxNum);

console.log(maxNum);
console.log(indexNum + 1);
*/ 