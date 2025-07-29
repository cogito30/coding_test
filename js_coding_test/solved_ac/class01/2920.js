// 음계
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let arr = inputData[0].trim().split(' ').map(Number);
let ascending = true;
let descending = true;
for (let i = 0; i < arr.length; ++i) {
    if (arr[i] > arr[i+1]) {
        ascending = false;
    } else if (arr[i] < arr[i+1]) {
        descending = false;
    }
}

if (ascending) {
    console.log("ascending");
} else if (descending) {
    console.log("descending");
} else {
    console.log("mixed");
}