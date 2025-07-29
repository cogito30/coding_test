// 문자열 반복
// 변수 자료형 주의!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(inputData[0].trim());

for (let t = 0; t < T; ++t){
    let [R, S] = inputData[1 + t].trim().split(' ');
    R = parseInt(R);
    let answer = "";
    for (let i = 0; i < S.length; ++i) {
        for (let r = 0; r < R; ++r) {
            answer += S[i];
        }
    }
    console.log(answer);
}