// 그대로 출력하기
// 한줄 입력 getline 사용
#include <iostream>

int main(int argc, char** argv) {
    std::string str;

    while (true) {
        getline(std::cin, str);
        if (std::cin.eof())
            break;
        std::cout << str << "\n";

    }
    return 0;
}