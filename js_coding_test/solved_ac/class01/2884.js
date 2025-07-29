// 알람 시계
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let [hour, minute] = inputData[0].split(' ').map(Number);

minute -= 45;
if (minute < 0) {
    minute += 60;
    hour -= 1;
}

if (hour < 0) {
    hour += 24;
}

console.log(`${hour} ${minute}`);