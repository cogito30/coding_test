// 이항 계수 1
#include <iostream>

int main(int argc, char** argv) {
    int N, K;
    std::cin >> N >> K;

    int result = 1;
    for (int i = N - K + 1; i < N + 1; ++i) {
        result *= i;
    }
    for (int i = 1; i < K + 1; ++i) {
        result /= i;
    }

    std::cout << result;

    return 0;
}