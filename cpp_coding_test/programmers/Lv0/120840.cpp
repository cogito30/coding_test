// 구슬을 나누는 경우의 수
// 자료형의 범위 주의!!
#include <string>
#include <vector>

using namespace std;

int solution(int balls, int share) {
    int answer = 0;
    double a = 1, b = 1;
    for (double i = share + 1; i < balls + 1; ++i) {
        a *= i;
    }
    for (double i = 1; i < balls - share + 1; ++i) {
        b *= i;
    }
    answer = a / b;
    return answer;
}