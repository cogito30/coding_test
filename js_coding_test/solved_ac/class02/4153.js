// 직각삼각형
// Array의 sort는 문자열을 기준으로 정렬
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let i = 0;
while (true) {
    let arr = inputData[i].trim().split(' ').map(Number);
    if ((arr[0] === 0) && (arr[1] === 0) && (arr[2] === 0)) {
        break;
    }
    // 정렬시 문자열 기준이므로 주의! 숫자 기준으로 변경
    arr.sort((a, b) => a - b);
    if ((arr[0] * arr[0] + arr[1] * arr[1]) === (arr[2] * arr[2])) {
        console.log("right");
    } else {
        console.log("wrong");
    }
    i++;
}