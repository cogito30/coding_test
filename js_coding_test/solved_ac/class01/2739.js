// 구구단
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

for (let i = 1; i < 10; ++i) {
    console.log(`${N} * ${i} = ${N * i}`);
}