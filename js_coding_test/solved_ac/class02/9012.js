// 괄호
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

const N = parseInt(inputData[0]);

let result = [];
for (let t = 0; t < N; ++t) {
    let sentance = inputData[1 + t];

    let answer = "YES";
    let stack = [];
    for (let j = 0; j < sentance.length; ++j) {
        if (sentance[j] === "(") {
            stack.push(sentance[j]);
        } else if (sentance[j] === ")") {
            if (stack.pop() !== "(") {
                answer = "NO";
                break;
            }
        }
    }
    if (stack.length > 0) {
        answer = "NO";
    }
    result.push(answer);
}

console.log(result.join("\n"));