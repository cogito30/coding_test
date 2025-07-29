// 설탕 배달
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int dp[50001] = {0};
    for (int i = 0; i < 8; ++i) {
        dp[i] = 10001;
    }
    dp[3] = 1;
    dp[5] = 1;
    dp[6] = 2;
    for (int i = 8; i < N + 1; ++i) {
        if (dp[i-3] < dp[i-5]) {
            dp[i] = dp[i-3] + 1;
        } else {
            dp[i] = dp[i-5] + 1;
        }
    }

    if (dp[N] >= 10001) {
        std::cout << - 1;
    } else {
        std::cout << dp[N];
    }

    return 0;
}

/* 그리디
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int result = 0;
    while (N > 0) {
        if (N % 5 == 0) {
            result += N / 5;
            break;
        } else {
            N -= 3;
            result += 1;
        }
    }
    if (N < 0) {
        std::cout << -1;
    } else {
        std::cout << result;
    }
    return 0;
}
*/

/* 시간초과
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int five_count = N / 5;
    N %= 5;
    int three_count = N / 3;
    N %= 3;
    while (true) {
        if (N == 0) {
            break;
        } else if (five_count < 0) {
            five_count--;
            N += 5;
        }
        three_count = N / 3;
        N %= 3;
    }

    if (five_count < 0) {
        std::cout << -1;
    } else {
        std::cout << five_count + three_count;
    }

    return 0;
}
*/