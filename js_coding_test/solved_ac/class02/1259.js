// 팰린드롬수
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

let i = 0;
let state = true;
while (true) {
    state = true;
    let stringNumber = inputData[i].trim();
    if (stringNumber === "0") {
        break;
    }

    for (let j = 0; j < stringNumber.length; ++j) {
        if (stringNumber[j] !== stringNumber[stringNumber.length - j - 1]) {
            state = false;
        }
    }

    if (state) {
        console.log("yes");
    } else {
        console.log("no");
    }
    i++;
}