// 균형잡힌 세상
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

let i = 0;
let result = [];
while (true) {
    let sentance = inputData[i];
    if (sentance[0] === "." && sentance.length === 1) {
        break;
    }

    let answer = "yes";
    let stack = [];
    for (let j = 0; j < sentance.length; ++j) {
        if (sentance[j] === "[" || sentance[j] === "(") {
            stack.push(sentance[j]);
        } else if (sentance[j] === "]") {
            if (stack.pop() !== "[") {
                answer = "no";
                break;
            }
        } else if (sentance[j] === ")") {
            if (stack.pop() !== "(") {
                answer = "no";
                break;
            }
        }
    }
    if (stack.length > 0) {
        answer = "no";
    }
    result.push(answer);
    i++;
}
console.log(result.join('\n'));