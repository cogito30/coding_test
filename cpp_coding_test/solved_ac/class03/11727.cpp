// 2xn 타일링 2
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    std::vector<int> dp = {0, 1, 3};
    for (int i = 3; i < 1001; ++i) {
        dp.push_back((dp[i-1] + dp[i-2] * 2) % 10007);
    }

    int N;
    std::cin >> N;
    std::cout << dp[N];
    return 0;
}