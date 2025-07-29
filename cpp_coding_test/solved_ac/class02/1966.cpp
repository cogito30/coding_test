// 프린터 큐
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        int N, M;
        std::cin >> N >> M;
        std::queue<std::pair<int,int>> q;
        std::vector<int> vec;
        int num;
        for (int i = 0; i < N; ++i) {
            std::cin >> num;
            q.push({num, i});
            vec.push_back(num);
        }

        std::sort(vec.begin(), vec.end(), std::greater<int>());

        int max_val = 0;
        int count = 0;
        int idx = 0;
        while (true) {
            if (q.front().first == vec[idx]) {
                count++;
                idx++;
                if (q.front().second == M){
                    break;
                }
                q.pop();
            } else {
                q.push(q.front());
                q.pop();
            }
        }
        std::cout << count << "\n";
    }
    return 0; 
}