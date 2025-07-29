# Coding Test를 위한 JavaScript 주요 메서드

- 기본 입출력
```javascript
const fs = require('fs'); 
const inputData = fs.readFileSync('/dev/stdin').toString().split('\n');

const varName = inputData[0].split(' ').map(Number);

console.log(inputData[0]);
```

- 형변환
```javascript
parseInt(varName);
Number(varName);
varName.toString();
```

- 문자열 메서드
```javascript
stringName[0].charCodeAt()
```

- 수학 메서드
```javascript
Math.abs(varName);
Math.max(...varList);
Math.min(...varList);
```