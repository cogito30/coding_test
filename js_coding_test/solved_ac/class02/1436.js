// 영화감독 숌
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

const check666 = (num) => {
    let countSix = 0;
    let r = 0;
    while (num > 0) {
        r = num % 10;
        num = Math.floor(num / 10);

        if (r === 6) {
            countSix++;
        } else {
            countSix = 0;
        }

        if (countSix === 3) {
            return true;
        }
    }
    return false;
}

let count = 0;
let number = 0;
while (true) {
    number++;
    if (check666(number)) {
        count++;
    }
    if (count === N) {
        break;
    }
}

console.log(number);


/*
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(inputData[0]);

let num = 666;
let count = 1;
while (count !== N) {
    num++;
    if (String(num).includes("666")) count++;
}
console.log(num);
*/ 