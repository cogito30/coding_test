// 듣보잡
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

int main(int argc, char** argv) {
    int N, M;
    std::cin >> N >> M;
    std::unordered_map<std::string, int> name_list;
    std::string str;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        name_list[str]++;
    }
    
    std::vector<std::string> result;
    for (int i = 0; i < M; ++i) {
        std::cin >> str;
        if (name_list[str] > 0) {
            result.push_back(str);
        }
    }
    
    std::sort(result.begin(), result.end());
    std::cout << result.size() << "\n";
    for (int i = 0; i < result.size(); ++i) {
        std::cout << result[i] << "\n";
    }

    return 0;
}