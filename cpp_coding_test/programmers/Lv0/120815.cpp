// 피자 나눠 먹기 (2)
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int x = 0;
    while (true) {
        x += 1;
        if ((6 * x) % n == 0) {
            answer = x;
            break;
        }
    }
    return answer;
}