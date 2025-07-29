// 나는야 포켓몬 마스터 이다솜
// std.cin.tie(nullptr) 미사용시 시간초과
#include <iostream>
#include <unordered_map>

int main(int argc, char** argv) {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::string str;
    std::unordered_map<std::string, std::string> name_to_id;
    std::unordered_map<std::string, std::string> id_to_name;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        name_to_id[str] = std::to_string(i + 1);
        name_to_id[std::to_string(i+1)] = str;
    }

    for (int i = 0; i < M; ++i) {
        std::cin >> str;
        std::cout << name_to_id[str] << "\n";
    }

    return 0;
}