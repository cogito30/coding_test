// 최소 힙
// 입출력 처리하지 않을 경우 시간 초과
#include <iostream>
#include <vector>
#include <queue>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    int N;
    std::cin >> N;
    int num;
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_pq;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        if (num == 0) {
            if (min_pq.empty()) {
                std::cout << 0 << "\n";
            } else {
                std::cout << min_pq.top() << "\n";
                min_pq.pop();
            }
        } else {
            min_pq.push(num);
        }
    }
    return 0;
}