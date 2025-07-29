// 대소문자 바꾸기
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let answer = "";
for (let i = 0; i < inputData[0].length; ++i) {
    if (inputData[0][i] === inputData[0][i].toUpperCase()) {
        answer += inputData[0][i].toLowerCase();
    } else {
        answer += inputData[0][i].toUpperCase();
    }
}
console.log(answer);