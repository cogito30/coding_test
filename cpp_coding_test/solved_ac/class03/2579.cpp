// 계단 오르기
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> stairs = {0};
    int num;
    for (int i = 1; i < N + 1; ++i) {
        std::cin >> num;
        stairs.push_back(num);
    }

    if (N == 0) {
        std::cout << 0;
        return 0;
    } else if (N == 1) {
        std::cout << stairs[1];
        return 0;
    } else if (N == 2) {
        std::cout << stairs[1] + stairs[2];
        return 0;
    }
    
    std::vector<int> dp = {0, stairs[1], stairs[1] + stairs[2]};
    int max_val = 0;
    for (int i = 3; i < N + 1; ++i) {
        max_val = std::max(dp[i-2] + stairs[i], dp[i-3] + stairs[i] + stairs[i-1]);
        dp.push_back(max_val);
    }

    std::cout << dp[N];

    return 0;
}