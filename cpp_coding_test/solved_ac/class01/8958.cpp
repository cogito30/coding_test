// OX퀴즈
#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int t = 0; t < T; ++t) {
        std::string str;
        std::cin >> str;

        int total_score = 0;
        int current_score = 1;
        for (int i = 0; i < str.length(); ++i) {
            if (str[i] == 'O') {
                total_score += current_score;
                current_score++;
            } else {
                current_score = 1;
            }
        }
        std::cout << total_score << "\n";
    }
    return 0;
}