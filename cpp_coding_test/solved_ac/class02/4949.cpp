// 균형잡힌 세상
// 스택에 남아있는 경우 확인
#include <iostream>
#include <stack>

int main(int argc, char** argv) {
    std::string str;
    std::string result;
    while (true) {
        result = "yes";
        getline(std::cin, str);

        if ((str.length() == 1) && (str == ".")) {
            break;
        }

        std::stack<char> stk;
        for (int i = 0; i < str.length(); ++i) {
            if ((str[i] == '(') || (str[i] == '[')) {
                stk.push(str[i]);
            } else if (str[i] == ')') {
                if ((stk.size() > 0) && (stk.top() == '(')) {
                    stk.pop();
                } else {
                    result = "no";
                    break;
                }
            } else if (str[i] == ']') {
                if ((stk.size() > 0) && (stk.top() == '[')) {
                    stk.pop();
                } else {
                    result = "no";
                    break;
                }
            }
        }
        
        if (stk.size() > 0) {
            result = "no";
        }
        std::cout << result << "\n";
    }
    return 0;
}