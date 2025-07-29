// 좌표 정렬하기2
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().split('\n');

const N = parseInt(inputData[0]);

let arr = [];
for (let i = 0; i < N; ++i) {
    let [x, y] = inputData[1 + i].trim().split(' ').map(Number);
    arr.push([x, y]);
}

arr.sort((a, b) => {
    if (a[1] === b[1]) {
        return a[0] - b[0];
    } else {
        return a[1] - b[1];
    }
});

for (let i = 0; i < N; ++i) {
    console.log(`${arr[i][0]} ${arr[i][1]}`);
}