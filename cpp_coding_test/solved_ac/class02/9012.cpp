// 괄호
#include <iostream>
#include <stack>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    std::string str;
    std::string result;
    for (int t = 0; t < T; ++t) {
        result = "YES";
        std::cin >> str;
        std::stack<char> stack;
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] == '(') {
                stack.push(str[i]);
            } else {
                if (stack.size() > 0 && stack.top() == '(') {
                    stack.pop();
                } else {
                    result = "NO";
                    break;
                }
            }
        }

        if (stack.size() > 0) {
            result = "NO";
        }

        std::cout << result << "\n";
    }
    return 0;
}