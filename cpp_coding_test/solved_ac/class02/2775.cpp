// 부녀회장이 될테야
// int people[n]는 C++에서 표준이 아니므로 vector 사용
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        int k, n;
        std::cin >> k;
        std::cin >> n;

        std::vector<int> people(n);
        for (int i = 0; i < n; ++i) {
            people[i] = i + 1;
        }

        for (int i = 0; i < k; ++i) {
            for (int j = 1; j < n; ++j) {
                people[j] += people[j-1];
            }
        }

        std::cout << people[n-1] << "\n";
    }

    return 0;
}