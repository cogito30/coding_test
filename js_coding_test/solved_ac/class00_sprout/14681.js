// 사분면 고르기
const fs = require('fs'); 
// 런타임 에러(EACCES)가 발생
// const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');
const inputData = fs.readFileSync(0, 'utf-8').trim().split('\n');

const x = parseInt(inputData[0]);
const y = parseInt(inputData[1]);

if ((x > 0) && (y > 0)) {
    console.log(1);
} else if ((x < 0) && (y > 0)) {
    console.log(2);
} else if ((x < 0) && (y < 0)) {
    console.log(3);
} else if ((x > 0) && (y < 0)) {
    console.log(4);
}