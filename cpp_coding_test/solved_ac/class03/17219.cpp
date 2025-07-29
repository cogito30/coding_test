// 비밀번호 찾기
#include <iostream>
#include <unordered_map>

int main(int argc, char** argv) {
    int N, M;
    std::cin >> N >> M;
    std::unordered_map<std::string, std::string> id_pw;
    std::string id, pw;
    for (int i = 0; i < N; ++i) {
        std::cin >> id >> pw;
        id_pw[id] = pw;
    }
    
    for (int i = 0; i < M; ++i) {
        std::cin >> id;
        std::cout << id_pw[id] << "\n";
    }
    return 0;
}