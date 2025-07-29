// 정수 내림차순으로 배치하기
function solution(n) {
    var answer = 0;
    let numberArray = [];
    while (n > 0) {
        numberArray.push(n % 10);
        n = parseInt(n / 10);
    }
    numberArray.sort((a, b) => { return b - a; });
    answer = parseInt(numberArray.join(''));
    return answer;
}