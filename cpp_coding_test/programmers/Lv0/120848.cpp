// 팩토리얼
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    // n이 1,2일 경우 주의
    if (n == 1) {
        answer = 1;
    } else {
        for (int i = 1; i < n + 1; ++i) {
            answer *= i;
            if (answer == n) {
                answer = i;
                break;
            } else if (answer > n) {
                answer = i - 1;
                break;
            }
        }
    }
    return answer;
}