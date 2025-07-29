// 문자열
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(inputData[0]);
for (let t = 0; t < T; ++t) {
    console.log(inputData[1 + t][0] + inputData[1 + t][inputData[1 + t].length - 1]);
}