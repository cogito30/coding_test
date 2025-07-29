// 좌표 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>

bool compare(std::pair<int, int> a, std::pair<int, int> b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<std::pair<int, int>> vec;
    int x, y;
    for (int i = 0; i < N; ++i) {
        std::cin >> x >> y;
        vec.push_back({x, y});
    }

    sort(vec.begin(), vec.end(), compare);

    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << it->first << " " << it->second << "\n";
    }

    return 0;
}