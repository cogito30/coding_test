// 요세푸스 문제 0
#include <iostream>
#include <queue>
#include <vector>

int main(int argc, char** argv) {
    int N, K;
    std::cin >> N >> K;

    std::queue<int> q;
    for (int i = 1; i <= N; ++i) {
        q.push(i);
    }

    std::vector<int> result;
    while (!q.empty()) {
        for (int i = 0; i < K - 1; ++i) {
            q.push(q.front());
            q.pop();
        }
        result.push_back(q.front());
        q.pop();
    }

    std::cout << "<";
    for (int i = 0; i < result.size(); ++i) {
        if (i == result.size() - 1) {
            std::cout << result[i];
        } else {
            std::cout << result[i] << ", ";
        }
    }
    std::cout << ">";

    return 0;
}