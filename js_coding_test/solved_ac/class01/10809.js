// 알파벳 찾기
// 문자열 메서드, ascii 변환
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const S = inputData[0].trim();
let arr = [];
for (let i = 0; i < 26; ++i) {
    arr.push(String.fromCharCode(97 + i));
}

let index = 0;
let answer = "";
for (let i = 0; i < arr.length; ++i) {
    index = S.indexOf(arr[i]);
    answer += index.toString() + " ";
}

console.log(answer);