// 나머지
// 집합 Set 메서드 확인
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let arr = [];
for (let i = 0; i < 10; ++i) {
    let r = Math.floor(parseInt(inputData[i]) % 42);
    arr.push(r);
}

const set = new Set(arr);
const unique = [...set];
console.log(unique.length);
