// 대소문자 바꾸기
#include <iostream>

int main(int argc, char** argv) {
    std::string str;
    std::cin >> str;

    for (int i = 0; i < str.length(); ++i) {
        if (isupper(str[i])) {
            str[i] += 32;
        } else {
            str[i] -= 32;
        }
    }

    std::cout << str;

    return 0;
}