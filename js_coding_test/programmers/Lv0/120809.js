// 배열 두 배 만들기
function solution(numbers) {
    var answer = [];
    answer = numbers.map(num => num * 2);
    return answer;
}

/* Test Case */ 
// [1, 2, 3, 4, 5] [2, 4, 5, 8, 10]
// [1, 2, 100, -99, 1, 2, 3] [2, 4, 200, -198, 2, 4, 6]
