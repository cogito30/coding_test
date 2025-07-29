// 스택 수열
#include <iostream>
#include <vector>
#include <stack>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::stack<int> stack;
    std::vector<char> result;    
    int i = 1;
    int num;
    while (N) {
        N--;
        std::cin >> num;
        while (i <= num) {
            stack.push(i);
            i++;
            result.push_back('+');
        }
        if (stack.top() == num) {
            stack.pop();
            result.push_back('-');
        }
    }

    if (stack.size() >= 1) {
        std::cout << "NO" << "\n";
    } else {
        for (int i = 0; i < result.size(); ++i) {
            std::cout << result[i] << "\n";
        }
    }

    return 0;
}