// 평균
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
let arr = inputData[1].trim().split(' ').map(Number);

let maxVal = Math.max(...arr);
let totalSum = 0;
for (let i = 0; i < arr.length; ++i) {
    totalSum += arr[i];
}
let answer = (totalSum * 100) / (maxVal * arr.length);
console.log(answer);