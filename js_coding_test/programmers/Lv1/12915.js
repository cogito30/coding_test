// 문자열 내 마음대로 정렬하기
function solution(strings, n) {
    var answer = [];
    strings.sort((str1, str2) => {
        if (str1[n] < str2[n]) {
            return -1;
        } else if (str1[n] > str2[n]) {
            return 1;
        } else {
            if (str1 <= str2) {
                return -1;
            } else {
                return 1;
            }
        }
    });
    answer = strings;
    return answer;
}