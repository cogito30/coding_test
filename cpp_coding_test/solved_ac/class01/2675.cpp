// 문자열 반복
#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        int R;
        std::string S;
        std::cin >> R >> S;

        for (int i = 0; i < S.length(); ++i) {
            for (int j = 0; j < R; ++j) {
                std::cout << S[i];
            }
        }
        std::cout << "\n";
    }

    return 0;
}