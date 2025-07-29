// 평균 구하기
function solution(arr) {
    var answer = 0;
    let sumNumber = 0;
    for (let i = 0; i < arr.length; ++i) {
        sumNumber += arr[i];
    }
    answer = sumNumber / arr.length;
    return answer;
}