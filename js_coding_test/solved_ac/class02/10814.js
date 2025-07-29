// 나이순 정렬
// (a, b)는 연산자로 b를 반환
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().split('\n');

const N = parseInt(inputData[0]);

let member = [];
for (let i = 0; i < N; ++i) {
    let [age, name] = inputData[1 + i].trim().split(' ');
    age = parseInt(age);
    member.push([age, name]);
}

member.sort((m1, m2) => m1[0] - m2[0]);

for (let i = 0; i < member.length; ++i) {
    console.log(`${member[i][0]} ${member[i][1]}`);
}