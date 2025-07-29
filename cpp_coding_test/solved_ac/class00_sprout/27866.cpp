// 문자와 문자열
#include <iostream>

int main(int argc, char** argv) {
    std::string str;
    int i;
    std::cin >> str;
    std::cin >> i;
    std::cout << str[i-1];

    return 0;
}