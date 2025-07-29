// 단어의 개수
// 공백만 입력되는 경우 주의!!
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let words = inputData[0].trim().split(' ');
if (words[0] === '') {
    console.log(0);
} else {
    console.log(words.length);
}
