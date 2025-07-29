// 수 정렬하기 2
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> vec;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end());

    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << "\n";
    }

    return 0;
}