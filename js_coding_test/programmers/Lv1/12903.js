// 가운데 글자 가져오기
function solution(s) {
    var answer = '';
    let sLengthDivTwo = parseInt(s.length / 2);
    if (s.length % 2 == 0) {
        answer = s.substring(sLengthDivTwo - 1, sLengthDivTwo + 1);
    } else {
        answer = s[sLengthDivTwo];
    }
    return answer;
}