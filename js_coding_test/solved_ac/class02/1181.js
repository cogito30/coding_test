// 단어 정렬
// sort 함수의 비교 함수는 음수/0/양수를 반환해야 하고, true/false는 적절한 결과를 보장하지 않음
// 문자열 비교시 localeCompare 사용
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);
let arr = [];
for (let i = 0; i < N; ++i) {
    arr.push(inputData[1 + i].trim());
}

arr = [...new Set(arr)]

arr.sort((str1, str2) => {
    return str1.length !== str2.length ? (str1.length - str2.length) : str1.localeCompare(str2);
});

for (let i = 0; i < arr.length; ++i) {
    console.log(arr[i]);
}