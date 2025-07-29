// ACM 호텔
// 나눗셈 연산시 반환 자료형 주의!!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(inputData[0]);
for (let t = 0; t < T; ++t) {
    const [H, W, N] = inputData[1 + t].split(' ').map(Number);
    let q = N % H;
    let r = Math.floor(N / H) + 1;

    if (q == 0) {
        q = H;
        r = Math.floor(N / H);
    }
    console.log(`${q * 100 + r}`);
}