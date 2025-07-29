// 카드2
#include <iostream>
#include <queue>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::queue<int> q;
    for (int i = 1; i < N + 1; ++i) {
        q.push(i);
    }

    int num;
    while (true) {
        if (q.size() == 1) {
            std::cout << q.front();
            break;
        }
        q.pop();
        num = q.front();
        q.pop();
        q.push(num);
    }

    return 0;
}