// 설탕 배달
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

let N = parseInt(inputData[0]);

let fiveCount = Math.floor(N / 5);
N %= 5;
let threeCount = Math.floor(N / 3);
N %= 3;
while (N > 0) {
    N += 5;
    fiveCount--;
    threeCount += Math.floor(N / 3);
    N %= 3;
    if (fiveCount < 0) {
        break;
    }
}
if (fiveCount < 0) {
    console.log(-1); 
} else {
    console.log(fiveCount + threeCount);
}