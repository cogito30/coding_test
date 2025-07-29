// 블랙잭
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = inputData[0].trim().split(' ').map(Number);
let arr = inputData[1].trim().split(' ').map(Number);

let maxVal = 0;
for (let i = 0; i < N - 2; ++i) {
    for (let j = i + 1; j < N - 1; ++j) {
        for (let k = j + 1; k < N; ++k) {
            if ((arr[i] + arr[j] + arr[k] > maxVal) && (arr[i] + arr[j] + arr[k] <= M)) {
                maxVal = arr[i] + arr[j] + arr[k];
            }
            
        }
    }
}

console.log(maxVal);