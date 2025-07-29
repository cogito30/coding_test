// 최소, 최대
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
let arr = inputData[1].split(' ').map(Number);

let answer = `${Math.min(...arr)} ${Math.max(...arr)}`;
console.log(answer);