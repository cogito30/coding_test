// 문자와 문자열
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let S = inputData[0];
let i = parseInt(inputData[1]);

console.log(S[i-1]);