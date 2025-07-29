// 제로
#include <iostream>
#include <stack>

int main(int argc, char** argv) {
    int K;
    std::cin >> K;
    int num;
    std::stack<int> stack;
    for (int i = 0; i < K; ++i) {
        std::cin >> num;
        if (num > 0) {
            stack.push(num);
        } else {
            stack.pop();
        }
    }

    int result = 0;
    while (stack.size() > 0) {
        result += stack.top();
        stack.pop();
    }

    std::cout << result;

    return 0;
}