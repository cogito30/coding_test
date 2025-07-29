// 소수 찾기
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
let arr = inputData[1].trim().split(' ').map(Number);

const isPrime = (num) => {
    if (num <= 1) {
        return false;
    }
    for (let i = 2; i * i <= num; ++i) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
};

let count = 0;
for (let i = 0; i < arr.length; ++i) {
    if (isPrime(arr[i])) {
        count++;
    }
}
console.log(count);