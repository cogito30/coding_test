// 두 정수 사이의 합
function solution(a, b) {
    var answer = 0;
    let tmpNum = 0;
    if (a > b) {
        tmpNum = a;
        a = b;
        b = tmpNum;
    }
    for (let i = a; i <= b; ++i) {
        answer += i;
    }
    return answer;
}