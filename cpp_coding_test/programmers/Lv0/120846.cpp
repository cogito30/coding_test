// 합성수 찾기
#include <string>
#include <vector>

using namespace std;

int divisor_count(int n) {
    int count = 0;
    for (int i = 1; i < n + 1; ++i) {
        if (n % i == 0) {
            count++;
        }
    }
    return count;
}

int solution(int n) {
    int answer = 0;
    for (int i = 3; i < n + 1; ++i) {
        if (divisor_count(i) >= 3) {
            answer++;
        }
    }
    return answer;
}