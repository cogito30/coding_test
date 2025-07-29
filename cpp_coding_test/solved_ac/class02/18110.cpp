// solved.ac
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

int main(int argc, char** argv) {
    int n;
    std::cin >> n;

    if (n == 0) {
        std::cout << 0;
    } else {
        std::vector<int> vec;
        int num;
        for (int i = 0; i < n; ++i) {
            std::cin >> num;
            vec.push_back(num);
        }

        sort(vec.begin(), vec.end());

        int round_num = std::round(n * 0.15);

        double total_num = 0;
        for (int i = round_num; i < n - round_num; ++i) {
            total_num += vec[i];
        }

        std::cout << (int)std::round(total_num / (n - 2 * round_num));
    }
    return 0;
}