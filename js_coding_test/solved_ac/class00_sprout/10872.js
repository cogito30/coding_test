// 팩토리얼
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const N = parseInt(inputData[0]);

let factorial = 1;
for (let i = 1; i <= N; ++i) {
    factorial *= i;
}
console.log(factorial);