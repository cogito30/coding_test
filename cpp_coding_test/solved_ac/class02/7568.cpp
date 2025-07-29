// 덩치
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int weight, height;
    std::vector<std::pair<int, int>> vec;
    for (int i = 0; i < N; ++i) {
        std::cin >> weight >> height;
        vec.push_back({weight, height});
    }

    std::vector<int> result;
    int rank = 0;
    for (int i = 0; i < N; ++i) {
        rank = 1;
        for (int j = 0; j < N; ++j) {
            if ((vec[i].first < vec[j].first) && (vec[i].second < vec[j].second)) {
                rank++;
            }
        }
        result.push_back(rank);
    }

    for (int i = 0; i < result.size(); ++i) {
        std::cout << result[i] << " ";
    }

    return 0;
}