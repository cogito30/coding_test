// 사파라월드
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const N = parseInt(inputData[0]);
const M = parseInt(inputData[1]);

console.log(Math.abs(N - M));