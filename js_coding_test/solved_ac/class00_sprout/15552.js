// 빠른 A+B
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(inputData[0]);

let answer = "";
for (let i = 1; i < N + 1; ++i) {
    let [A, B] = inputData[i].split(" ").map(Number);
    answer += A + B + "\n";
}
console.log(answer);