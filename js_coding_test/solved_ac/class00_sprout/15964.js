// 이상한 기호
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const [A, B] = inputData[0].split(' ').map(Number);
console.log((A + B) * (A - B));