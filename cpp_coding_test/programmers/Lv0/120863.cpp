// 다항식 더하기
#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string polynomial) {
    string answer = "";
    stringstream ss;
    ss.str(polynomial);
    string str;
    int x_count = 0;
    int count = 0;
    while (ss >> str) {
        string tmp = "";
        if (str[str.length()-1] == 'x') {
            if (str.length() == 1) {
                x_count++;
            } else {
                x_count += stoi(str.substr(0, str.length() - 1));
            }
        }
        if ((str[str.length()-1] >= '0') && (str[str.length()-1] <= '9')) {
            count += stoi(str.substr(0, str.length()));
        }
    }
    if (x_count > 0) {
        if (x_count == 1) {
            answer += "x";    
        } else {
            answer += to_string(x_count) + "x";    
        }
    }
    if (count > 0) {
        if (answer.length() > 0) {
            answer += " + ";
        }
        answer += to_string(count);
    }
    

    return answer;
}