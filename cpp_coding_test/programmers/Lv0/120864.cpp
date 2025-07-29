// 숨어있는 숫자의 덧셈 (2)
#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    string num_str = "";
    for (int i = 0; i < my_string.length(); ++i) {
        if ((my_string[i] >= '0') && (my_string[i] <= '9')) {
            num_str += my_string[i];
        } else {
            if (num_str != "") {
                answer += stoi(num_str);
                num_str = "";
            }
        }
    }
    if (num_str != "") {
        answer += stoi(num_str);
    }
    return answer;
}