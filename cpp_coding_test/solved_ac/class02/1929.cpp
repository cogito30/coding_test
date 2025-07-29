// 소수 구하기
// 에로토스테네스의 체
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int M, N;
    std::cin >> M >> N;

    std::vector<bool> prime(N+1, true);
    prime[0] = false;
    prime[1] = false;
    for (int i = 2; i < N + 1; ++i) {
        if (prime[i]) {
            for (int j = i * 2; j <= N + 1; j += i) {
                prime[j] = false;
            }
        }
    }

    for (int i = M; i < N + 1; ++i) {
        if (prime[i]) {
            std::cout << i << "\n";
        }
    }
    return 0;
}