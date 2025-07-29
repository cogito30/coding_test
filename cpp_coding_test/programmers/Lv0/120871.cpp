// 저주의 숫자 3
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (int i = 1; i < n+1; ++i) {
        answer += 1;
        while ((answer % 3 == 0) || to_string(answer).find('3') != string::npos) {
            answer++;
        }
    }
    return answer;
}