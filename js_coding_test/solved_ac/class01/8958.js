// OX퀴즈
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(inputData[0]);

for (let t = 0; t < T; ++t) {
    let quiz = inputData[1 + t].trim();
    let score = 1;
    let totalScore = 0;
    for (let i = 0; i < quiz.length; ++i) {
        if (quiz[i] == "O") {
            totalScore += score;
            score++;
        } else {
            score = 1;
        }
    }
    console.log(totalScore);
}