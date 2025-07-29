// A + B - 4
// trim()으로 공백을 제거하지 않는 경우 틀림
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for (let i = 0; i < inputData.length; ++i) {
    const [A, B] = inputData[i].split(" ").map(Number);
    console.log(A + B);
}