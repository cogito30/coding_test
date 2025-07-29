// A+B - 3
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

for (let i = 1; i < N + 1; ++i) {
    let [A, B] = inputData[i].split(' ').map(Number);

    console.log(A + B);
}