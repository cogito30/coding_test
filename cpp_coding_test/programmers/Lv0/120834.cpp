// 외계행성의 나이
// 문자열의 요소는 char 주의
#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    vector<char> word;
    while (age > 0) {
        word.push_back(char(age % 10 + 97));
        age /= 10;
    }
    for (int i = word.size() - 1; i >= 0; --i) {
        answer += word[i];
    }
    return answer;
}