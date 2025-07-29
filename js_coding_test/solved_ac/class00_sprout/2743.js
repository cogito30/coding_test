// 단어 길이 재기
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

console.log(inputData[0].length);