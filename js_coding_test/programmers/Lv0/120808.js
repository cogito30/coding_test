// 분수의 덧셈
function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    
    const gcd = (a, b) => (b === 0) ? a: gcd(b, a % b);
    let gcdNumber = (denom >= numer) ? gcd(denom, numer): gcd(numer, denom);
    answer.push(numer / gcdNumber);
    answer.push(denom / gcdNumber);
    return answer;
}

/* Test Case */
// 1 2 3 4 [5,4]
// 9 2 1 3 [29,6]
