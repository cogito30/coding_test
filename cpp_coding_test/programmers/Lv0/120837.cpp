// 개미 군단
#include <string>
#include <vector>

using namespace std;

int solution(int hp) {
    int answer = 0;
    int ant[3] = {5, 3, 1};
    for (int i = 0; i < 3; ++i) {
        answer += hp / ant[i];
        hp %= ant[i];
    }
    return answer;
}