// 별 찍기 - 1
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

for (let i = 0; i < N; ++i) {
    let star = "";
    for (let j = 0; j < i + 1; ++j) {
        star += "*";
    }
    console.log(star);
}