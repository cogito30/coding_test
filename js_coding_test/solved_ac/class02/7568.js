// 덩치
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().split('\n');

const N = parseInt(inputData[0]);

let arr = []
for (let i = 0; i < N; ++i) {
    let weight, height = inputData[1 + i].trim().split(' ').map(Number);
    arr.push((weight, height));
}

let answer = [];
for (let i = 0; i < arr.length; ++i) {
    let rank = 1;
    for (let j = 0; j < arr.length; ++j) {
        if ((arr[i][0] < arr[j][0]) && (arr[i][1] < arr[j][1])) {
            rank++;
        }
    }
    answer.push(rank);
}

console.log(answer.join(' '));