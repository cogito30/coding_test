// 부녀회장이 될테야
// 입력 k, n 주의
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = parseInt(inputData[0]);
for (let t = 0; t < T; ++t) {
    let k = parseInt(inputData[1 + 2*t]);
    let n = parseInt(inputData[1+ 2*t + 1]);
    
    let people = [];
    for (let i = 0; i < n; ++i) {
        people.push(i + 1);
    }

    for (let i = 0; i < k; ++i) {
        for (let j = 1; j < n; ++j) {
            people[j] += people[j-1];
        }
    }
    console.log(people[n-1]);
}