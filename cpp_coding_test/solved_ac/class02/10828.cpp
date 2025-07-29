// 스택
#include <iostream>
#include <stack>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::stack<int> stack;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        if (str == "push") {
            std::cin >> num;
            stack.push(num);
        } else if (str == "pop") {
            if (stack.size() > 0) {
                std::cout << stack.top() << "\n";
                stack.pop();
            } else {
                std::cout << -1 << "\n";
            }
        } else if (str == "size") {
            std::cout << stack.size() << "\n";
        } else if (str == "empty") {
            if (stack.size() == 0) {
                std::cout << 1 << "\n";
            } else {
                std::cout << 0 << "\n";
            }
        } else if (str == "top") {
            if (stack.size() > 0) {
                std::cout << stack.top() << "\n";
            } else {
                std::cout << -1 << "\n";
            }
        }
    }
    return 0;
}