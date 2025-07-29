# Programmers(JavaScript)

## 입출력 템플릿
```javascript
const fs = require('fs');
const input = fs.readFileSync('./programmers/input.txt').toString().split('\n'); // 파일 읽기

function solution(input) {
    // 문제풀이 로직
    return null;
}

for (let i = 0; i < input.length; ++i) {
    let data = input[0].split(' ');
    console.log(`answer: ${data[data.length - 1]}`);
    let inputData = [];
    for (let j = 0; j < data.length - 1; ++j) {
        inputData.push(parseInt(data[j]));
    }
    console.log(`input: ${inputData} typeof: ${typeof inputData}`);
    console.log(`solution: ${solution(input)}`);
    console.log('----------');
}
```

## 기본문법
- 변수선언
```javascript
let 변수명 = value;
const 변수명 = value;
```
- 형변환
```javascript
parseInt();

```
- 연산자
```javascript
// 사칙연산
const result = a + b;
const result = a - b;
const result = a * b;
const result = a / b;
const result = a % b;

// 삼항연산자
const result = (조건문) ? true일때 반환값 : false일떄 반환값;
```
- 제어문
```javascript
```
- 함수
```javascript
const funcName = (param1, ...) => {
    ...
    return val;
}
```
- 
```javascript
```
- 
```javascript
```
- 
```javascript
```

## 내장함수
- 
```javascript
```
