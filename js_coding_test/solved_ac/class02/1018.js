// 체스판 다시 칠하기
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().split('\n');

const [N, M] = inputData[0].trim().split(' ').map(Number);

let board = [];
for (let i = 0; i < N; ++i) {
    let rows = inputData[1 + i].trim().split('');
    board.push(rows);
}

const check = (row, col, board) => {
    let [bCount, wCount] = [0, 0];
    for (let i = row; i < row + 8; ++i) {
        for (let j = col; j < col + 8; ++j) {
            if ((i + j) % 2 == 0) {
                if (board[i][j] == 'B') {
                    wCount++;
                } else {
                    bCount++;
                }
            } else {
                if (board[i][j] == 'W') {
                    wCount++;
                } else {
                    bCount++;
                }
            }
        }
    }
    return (wCount > bCount) ? bCount: wCount;
};

let count = 0;
let minCount = N * M;
for (let row = 0; row < N - 7; ++row) {
    for (let col = 0; col < M - 7; ++col) {
        count = check(row, col, board);
        if (minCount > count) {
            minCount = count;
        }
    }
}

console.log(minCount);

/*
const fs = require('fs'); 
const inputData = fs.readFileSync(process.platform === "linux" ? "/dev/stdin" : './solved_ac/test.txt').toString().trim().split('\n');

const [N, M] = inputData[0].trim().split(' ').map(Number);
const board = [];

for (let i = 0; i < N; ++i) {
    board.push(inputData[1 + i].trim().split(''));
}

const check = (row, col) => {
    let repaintB = 0;
    let repaintW = 0;

    for (let i = 0; i < 8; ++i) {
        for (let j = 0; j < 8; ++j) {
            const current = board[row + i][col + j];
            const expectedB = ((i + j) % 2 === 0) ? 'B' : 'W';
            const expectedW = ((i + j) % 2 === 0) ? 'W' : 'B';

            if (current !== expectedB) repaintB++;
            if (current !== expectedW) repaintW++;
        }
    }

    return Math.min(repaintB, repaintW);
};

let minCount = Infinity;
for (let row = 0; row <= N - 8; ++row) {
    for (let col = 0; col <= M - 8; ++col) {
        minCount = Math.min(minCount, check(row, col));
    }
}

console.log(minCount);
*/