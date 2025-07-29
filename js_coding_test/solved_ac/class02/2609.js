// 최대공약수와 최소공배수
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const gcd = (minNumber, maxNumber) => {
    return (minNumber % maxNumber) === 0 ? maxNumber : gcd(maxNumber, minNumber % maxNumber);
};

let [num1, num2] = inputData[0].trim().split(' ').map(Number);

let minNum = Math.min(num1, num2);
let maxNum = Math.max(num1, num2);
    
let answer = [0, 0]
answer[0] = Math.floor(gcd(minNum, maxNum));
answer[1] = Math.floor((minNum * maxNum) / answer[0]);

console.log(answer[0]);
console.log(answer[1]);