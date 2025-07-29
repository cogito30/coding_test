// 사분면 고르기
#include <iostream>

int main(int argc, char** argv) {
    int x, y;
    std::cin >> x;
    std::cin >> y;

    if ((x > 0) && (y > 0)) {
        std::cout << 1;
    } else if ((x < 0) && (y > 0)) {
        std::cout << 2;
    } else if ((x < 0) && (y < 0)) {
        std::cout << 3;
    } else if ((x > 0) && (y < 0)) {
        std::cout << 4;
    }
    
    return 0;
}