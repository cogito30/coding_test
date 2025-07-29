// 윤년
#include <iostream>

int main(int argc, char** argv) {
    int year;
    std::cin >> year;

    if((year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0))) {
        std::cout << 1;
    } else {
        std::cout << 0;
    }

    return 0;
}