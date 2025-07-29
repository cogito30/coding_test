// 수박수박수박수박수박수?
function solution(n) {
    var answer = '';
    let count = parseInt(n / 2);
    for (let i = 0; i < count; ++i) {
        answer += "수박";
    }
    if (n % 2 == 1) {
        answer += "수";
    }
    return answer;
}