// 파도반 수열
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    std::vector<long long> dp = {0, 1, 1, 1, 2, 2};
    for (int i = 6; i < 101; ++i) {
        dp.push_back(dp[i-1] + dp[i-5]);
    }
    
    int N;
    for (int t = 0; t < T; ++t) {
        std::cin >> N;
        std::cout << dp[N] << "\n";
    }

    return 0;
}