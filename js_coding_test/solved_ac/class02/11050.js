// 이항 계수 1
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, K] = inputData[0].trim().split(' ').map(Number);

let answer = 1;
for (let i = N - K + 1; i < N + 1; ++i) {
    answer *= i;
}
for (let i = 1; i < K + 1; ++i) {
    answer /= i;
}

console.log(Math.floor(answer));