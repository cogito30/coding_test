// 분해합
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

let num = 0;
let totalNum = 0;
let answer = 0;
for (let i = 1; i <= N; ++i) {
    num = i;
    totalNum = i;
    while (num > 0) {
        totalNum += Math.floor(num % 10);
        num = Math.floor(num / 10);
    }
    
    if (totalNum === N) {
        answer = i;
        break;
    }
}
console.log(answer);