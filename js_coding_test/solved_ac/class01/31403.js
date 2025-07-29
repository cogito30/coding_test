// A + B - C
// JS는 기본으로 문자열 - 는 숫자로 연산
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = inputData[0];
const B = inputData[1];
const C = inputData[2];

console.log(Number(A) + Number(B) - Number(C));
console.log(A + B - C);