// 달팽이는 올라가고 싶다
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let [A, B, V] = inputData[0].trim().split(' ').map(Number);

let answer = ((V - A) / (A - B)) + 1;

if (((V - A) % (A - B)) !== 0) {
    answer += 1;
}

console.log(Math.floor(answer));