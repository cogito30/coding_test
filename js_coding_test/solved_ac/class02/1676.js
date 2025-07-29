// 팩토리얼 0의 개수
// 10은 2와 5로 이루어졌음을 활용
// overflow 주의 BigInt 사용
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

let num = 0;
let fiveCount = 0;
for (let i = 1; i <= N; ++i) {
    num = i;
    while (num % 5 === 0) {
        fiveCount++;
        num = Math.floor(num / 5);
    }
}
console.log(fiveCount);