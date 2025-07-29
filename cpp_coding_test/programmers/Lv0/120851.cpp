// 숨어있는 숫자의 덧셈 (1)
#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for (int i = 0; i < my_string.size(); ++i) {
        if ((my_string[i] >= '0') && (my_string[i] <= '9')) {
            answer += my_string[i] - '0';
        }
    }
    return answer;
}