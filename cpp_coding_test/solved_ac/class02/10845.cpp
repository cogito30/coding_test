// 큐
#include <iostream>
#include <queue>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::queue<int> q;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        if (str == "push") {
            std::cin >> num;
            q.push(num);
        } else if (str == "pop") {
            if (q.empty()) {
                std::cout << -1 << "\n";
            } else {
                std::cout << q.front() << "\n";
                q.pop();
            }
        } else if (str == "size") {
            std::cout << q.size() << "\n";
        } else if (str == "empty") {
            if (q.empty()) {
                std::cout << 1 << "\n";
            } else {
                std::cout << 0 << "\n";
            }
        } else if (str == "front") {
            if (q.empty()) {
                std::cout << -1 << "\n";
            } else {
                std::cout << q.front() << "\n";
            }
        } else if (str == "back") {
            if (q.empty()) {
                std::cout << -1 << "\n";
            } else {
                std::cout << q.back() << "\n";
            }
        }
    }
    return 0;
}