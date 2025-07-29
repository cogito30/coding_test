// N 찍기
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const N = parseInt(inputData[0]);

for (let i = 1; i <= N; ++i) {
    console.log(i);
}