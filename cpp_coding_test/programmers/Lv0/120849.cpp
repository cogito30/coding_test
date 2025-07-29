// 모음 제거
#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    vector<char> data = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < my_string.length(); ++i) {
        for (int j = 0; j < 5; ++j) {
            if (my_string[i] == data[j]) {
                break;
            } else if (j == 4) {
                answer += my_string[i];
            }
        }
    }
    return answer;
}