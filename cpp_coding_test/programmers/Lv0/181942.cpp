// 문자열 섞기
// 문자열(str1[i] + str2[i]) 한 번에 계산시 숫자로 처리됨 
#include <string>
#include <vector>

using namespace std;

string solution(string str1, string str2) {
    string answer = "";
    for (int i = 0; i < str1.length(); ++i) {
        answer += str1[i];
        answer += str2[i];
    }
    return answer;
}