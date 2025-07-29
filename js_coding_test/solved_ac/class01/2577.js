// 단어의 개수
// /(나눗셈)은 부동소수점으로 처리되므로 정수형으로 형변환이 필요!!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let A = inputData[0].trim().split(' ').map(Number);
let B = inputData[1].trim().split(' ').map(Number);
let C = inputData[2].trim().split(' ').map(Number);

let total = A * B * C;
let numberCount = [];
for (let i = 0; i < 10; ++i) {
    numberCount.push(0);
}

while (total > 0) {
    numberCount[total % 10]++;
    total = Math.floor(total / 10);
}

for (let i = 0; i < 10; ++i) {
    console.log(numberCount[i]);
}