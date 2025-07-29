// Hashing
// 정수 오버플로우 주의!!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const L = parseInt(inputData[0]);
let words = inputData[1].trim().split('');

let answer = 0;
let pow31 = 1;
for (let i = 0; i < L; ++i) {
    answer =  answer + (words[i].charCodeAt() - 97 + 1) * (pow31) % 1234567891;
    pow31 = (pow31 * 31) % 1234567891;
}
console.log(answer % 1234567891);