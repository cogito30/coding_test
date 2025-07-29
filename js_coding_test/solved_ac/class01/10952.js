// A+B - 5
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let i = 0;
while (true) {
    let [A, B] = inputData[i].split(' ').map(Number);
    if (A == 0 && B == 0) {
        break;
    }

    console.log(A + B);
    i++;
}