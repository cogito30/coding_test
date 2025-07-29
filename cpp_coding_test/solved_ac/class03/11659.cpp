// 누적합
// 입출력 미처리시 시간초과
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);
    std::cout.tie(0);
    
    int N, M;
    std::cin >> N >> M;
    std::vector<int> vec = {0};
    int num;
    for (int i = 1; i <= N; ++i) {
        std::cin >> num;
        vec.push_back(num);
    }

    for (int i = 1; i <= N; ++i) {
        vec[i] = vec[i] + vec[i-1];
    }

    int start, end;
    for (int i = 0; i < M; ++i) {
        std::cin >> start >> end;
        std::cout << vec[end] - vec[start-1] << "\n";
    }

    return 0;
}