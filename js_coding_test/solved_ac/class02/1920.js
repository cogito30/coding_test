// 수 찾기
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

const N = parseInt(inputData[0]);
const nSet = new Set(inputData[1].trim().split(' ').map(Number));
const M = parseInt(inputData[2]);
const mArr = inputData[3].trim().split(' ').map(Number);

let answer = mArr.map(num => nSet.has(num) ? 1 : 0);
console.log(answer.join('\n'));


/* 시간초과
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().split('\n');

const N = parseInt(inputData[0]);
let nArr = inputData[1].trim().split(' ').map(Number);
const M = parseInt(inputData[2]);
let mArr = inputData[3].trim().split(' ').map(Number);

nArr = [...new Set(nArr)];

let result = [];
mArr.forEach(ele => {
    if (nArr.includes(ele)) {
        result.push(1);
    } else {
        result.push(0);
    }
});

console.log(result.join("\n"));
*/
