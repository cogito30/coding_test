// 알람 시계
#include <iostream>

int main(int argc, char** argv) {
    int H, M;
    std::cin >> H;
    std::cin >> M;
    
    M -= 45;
    
    if (M < 0) {
        M += 60;
        H -= 1;
    }
    
    if (H < 0) {
        H += 24;
    }

    std::cout << H << " " << M;

    return 0;
}