// 피보나치 함수
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    int num;
    for (int t = 0; t < T; ++t) {
        std::cin >> num;

        std::vector<int> count_zero = {1, 0};
        std::vector<int> count_one = {0, 1};
        for (int i = 2; i <= num; ++i) {
            count_zero.push_back(count_zero[i-2] + count_zero[i-1]);
            count_one.push_back(count_one[i-2] + count_one[i-1]);
        }

        std::cout << count_zero[num] << " " << count_one[num] << "\n";
    }
    return 0;
}