// 시험 성적
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ');

const score = parseInt(inputData[0]);

if ((score >= 90) && (score <= 100)) {
    console.log("A");
} else if ((score >= 80) && (score <= 89)) {
    console.log("B");
} else if ((score >= 70) && (score <= 79)) {
    console.log("C");
} else if ((score >= 60) && (score <= 69)) {
    console.log("D");
} else {
    console.log("F");
}
