// 사파리월드
// abs의 namespaces는 std
#include <iostream>

int main(int argc, char** argv) {
    long long N, M;
    std::cin >> N;
    std::cin >> M;
    std::cout << std::abs(N - M);

    return 0;
}