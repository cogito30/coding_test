// 자연수 뒤집어 배열로 만들기
function solution(n) {
    var answer = [];
    while (n > 0) {
        answer.push(n % 10);
        n = parseInt(n / 10);
    }
    return answer;
}