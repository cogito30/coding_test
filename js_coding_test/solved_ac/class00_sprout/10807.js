// 개수 세기
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
const numList = inputData[1].split(' ').map(Number);
const v = parseInt(inputData[2]);

let answer = 0;
for (let i = 0; i < N; ++i) {
    if (numList[i] == v) {
        answer++;
    }
}
console.log(answer);