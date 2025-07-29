// 웰컴 키트
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0].trim());
let arr = inputData[1].trim().split(' ').map(Number);
const [T, P] = inputData[2].trim().split(' ').map(Number);

let count = 0;
let answer = [0, 0];
for (let i = 0; i < arr.length; ++i) {
    count += Math.floor(arr[i] / T) + 1;
    if (Math.floor(arr[i] % T) === 0) {
        count--;
    }
    answer[0] = Math.floor(N / P);
    answer[1] = Math.floor(N % P);
}
console.log(count);
console.log(`${answer[0]} ${answer[1]}`);