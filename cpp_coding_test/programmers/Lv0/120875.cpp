// 평행
// 자료형 주의!! int일 경우 테스트 2번 오류. double 사용

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> dots) {
    int answer = 0;
    sort(dots.begin(), dots.end());
    double line1 = ((double)dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]);
    double line2 = ((double)dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]);
    if (line1 == line2) {
        answer = 1;
    } else {
        answer = 0;
    }
    return answer;
}