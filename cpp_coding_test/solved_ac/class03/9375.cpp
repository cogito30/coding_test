// 패션왕 신해빈
#include <iostream>
#include <unordered_map>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    int N;
    for (int t = 0; t < T; ++t) {
        std::cin >> N;
        std::string name, category;
        std::unordered_map<std::string, int> category_count;
        for (int i = 0; i < N; ++i) {
            std::cin >> name >> category;
            category_count[category]++;
        }

        // 안 입는 경우 고려
        int result = 1;
        for (auto& p: category_count) {
            result *= p.second + 1;
        }

        std::cout << result - 1 << "\n";
    }
    return 0;
}