// 벌집
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

let num = 1, count = 1;
while (true) {
    if (N <= num) {
        break;
    }
    num += 6 * count;
    count++;
}
console.log(count);