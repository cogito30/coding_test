// 컨트롤 제트
// 'Z'이후 공백시 주의
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;
    string num = "";
    int prevNum = 0;
    for (int i = 0; i < s.length(); ++i) {
        cout << num << " ";
        if (s[i] == ' ') {
            if (num != ""){
                answer += stoi(num);
                prevNum = stoi(num);
                num = "";    
            } 
        } else if (s[i] == 'Z') {
            answer -= prevNum;
        } else {
            num += s[i];
        }
    }
    if (num != ""){
        answer += stoi(num);    
    }
    return answer;
}