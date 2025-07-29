// 문자열 다루기 기본
function solution(s) {
    var answer = true;
    const sLength = s.length;
    if (sLength != 4 && sLength != 6) {
        answer = false;
    }
    for (let i = 0; i < sLength; ++i) {
        if (s[i] < '0' || s[i] > '9') {
            answer = false;
            break;
        }
    }
    return answer;
}

// 반례: "0x16" false
// function solution(s) {
//     var answer = true;
//     const sLength = s.length;
//     if (sLength != 4 && sLength != 6) {
//         answer = false;
//     }
//     if (isNaN(s)) {
//         answer = false;
//     }
//     return answer;
// }