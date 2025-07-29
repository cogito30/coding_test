// 통계학
// 합, 나누기 연산시 자료형 주의!!1
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> vec;
    std::map<int, int> freq;
    int num;
    for (int i = 0; i < N; ++i){
        std::cin >> num;
        vec.push_back(num);
        freq[num]++;
    }

    double total_sum = 0;
    for (int i = 0; i < vec.size(); ++i) {
        total_sum += vec[i];
    }
    std::cout << (int)std::round(total_sum / N) << "\n";

    sort(vec.begin(), vec.end());
    std::cout << vec[N/2] << "\n";

    int max_freq = 0;
    for (auto& p: freq) {
        if (p.second > max_freq) {
            max_freq = p.second;
        }
    }

    std::vector<int> result;
    for (auto& p: freq) {
        if (p.second == max_freq) {
            result.push_back(p.first);
        }
    }

    sort(result.begin(), result.end());
    if (result.size() > 1) {
        std::cout << result[1] << "\n";
    } else {
        std::cout << result[0] << "\n";
    }

    std::cout << vec[N-1] - vec[0];


    return 0;
}