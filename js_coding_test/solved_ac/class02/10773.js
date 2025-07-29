// 제로
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

const K = parseInt(inputData[0]);

let arr = [];
for (let i = 0; i < K; ++i) {
    let num = parseInt(inputData[1 + i]);
    if (num === 0) {
        arr.pop();
    } else {
        arr.push(num);
    }
}

let answer = 0;
arr.forEach((item) => {
    answer += item;
});

console.log(answer);