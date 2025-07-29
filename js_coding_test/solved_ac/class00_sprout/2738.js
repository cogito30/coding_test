// 행렬 덧셈
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = inputData[0].split(' ').map(Number);

let matrixA = []
for (let i = 0; i < N; ++i) {
    matrixA.push(inputData[1 + i].split(' ').map(Number));
}

let matrixB = []
for (let i = 0; i < N; ++i) {
    matrixB.push(inputData[N + 1 + i].split(' ').map(Number));
}

for (let i = 0; i < N; ++i) {
    for (let j = 0; j < M; ++j) {
        matrixA[i][j] += matrixB[i][j];
    }
}


for (let i = 0; i < N; ++i) {
    let str = "";
    for (let j = 0; j < M; ++j) {
        str += matrixA[i][j] + " ";
    }
    console.log(str);
}