// 검증수
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const arr = inputData[0].split(' ').map(Number);

let sumNumber = 0;
for (let i = 0; i < arr.length; ++i) {
    sumNumber += arr[i] * arr[i];
}
console.log(sumNumber % 10);