// 문자열
#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    std::string str;
    for (int i = 0; i < T; ++i) {
        std::cin >> str;
        std::cout << str[0] << str[str.length() - 1] << "\n";
    }

    return 0;
}