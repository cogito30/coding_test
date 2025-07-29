// 2016년
function solution(a, b) {
    var answer = '';
    const day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    const month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let totalDay = 5 // FRI
    for (let i = 1; i < a; ++i) {
        totalDay += month[i];
    }
    totalDay += b - 1;
    answer = day[totalDay % 7];
    return answer;
}