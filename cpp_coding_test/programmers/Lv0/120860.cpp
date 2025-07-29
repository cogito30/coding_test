// 직사각형 넓이 구하기
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> dots) {
    int answer = 0;
    sort(dots.begin(), dots.end());
    answer = (dots[0][1] - dots[1][1]) * (dots[1][0] - dots[2][0]);
    return answer;
}