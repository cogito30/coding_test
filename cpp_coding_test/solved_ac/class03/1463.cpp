// 1로 만들기
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::vector<int> dp = {0, 0, 1, 1};
    int min_val = 0;
    for (int i = 4; i <= N; ++i) {
        min_val = dp[i-1] + 1;
        if (i % 3 == 0) {
            min_val = std::min(min_val, dp[i/3] + 1);
        }
        if (i % 2 == 0){
            min_val = std::min(min_val, dp[i/2] + 1);
        }
        dp.push_back(min_val);
    }
    std::cout << dp[N];

    return 0;
}