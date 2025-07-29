// X보다 작은 수
// split시 ' ' 필수
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, X] = inputData[0].split(' ').map(Number);
const  numList = inputData[1].split(' ').map(Number);

let answer = "";
for (let i = 0; i < N + 1; ++i) {
    if (numList[i] < X) {
        answer += numList[i] + " ";
    }
}
console.log(answer);