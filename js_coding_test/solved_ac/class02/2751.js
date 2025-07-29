// 수 정렬하기 2
// 정답 출력시 join 사용하지 않으면 시간 초과
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
let arr = []
for (let i = 0; i < N; ++i) {
    arr.push(parseInt(inputData[1 + i]));
}

arr.sort((a, b) => a - b);

console.log(arr.join('\n'));