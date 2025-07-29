// 1, 2, 3 더하기
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    std::vector<int> vec = {0, 1, 2, 4};
    for (int i = 4; i < 11; ++i) {
        vec.push_back(vec[i-1] + vec[i-2] + vec[i-3]);
    }

    int N;
    for (int t = 0; t < T; ++t) {
        std::cin >> N;
        std::cout << vec[N] << "\n";
    }
    return 0;
}