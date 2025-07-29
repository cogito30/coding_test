// 2xn  타일링
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int n;
    std::cin >> n;

    std::vector<int> dp = {1, 2};

    for (int i = 2; i < n; ++i) {
        dp.push_back((dp[i-1] + dp[i-2]) % 10007);
    }

    std::cout << dp[n-1];

    return 0;
}