// 문자열 내림차순으로 배치하기
function solution(s) {
    var answer = '';
    let sArray = s.split('');
    sArray.sort((a, b) => {
        return a < b ? 1: -1;
    });
    answer = sArray.join('');
    
    return answer;
}