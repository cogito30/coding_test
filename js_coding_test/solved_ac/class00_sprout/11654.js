// 아스키 코드
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

console.log(inputData[0].charCodeAt());