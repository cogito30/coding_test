// 숫자의 합
// split내 문자 주의!!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
const numList = inputData[1].split('').map(Number);

let answer = 0;
for (let i = 0; i < N; ++i) {
    answer += numList[i];
}
console.log(answer);