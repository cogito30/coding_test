// 과제 안 내신 분..?
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let arr = [];
for (let i = 0; i < 30; ++i) {
    arr.push(0);
}

for (let i = 0; i < 28; ++i) {
    arr[inputData[i] - 1] = 1;
}

for (let i = 0; i < 30; ++i) {
    if (arr[i] == 0) {
        console.log(i + 1);
    }
}