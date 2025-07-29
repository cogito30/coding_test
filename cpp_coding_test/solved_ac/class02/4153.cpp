// 직각삼각형
#include <iostream>

int main(int argc, char** argv) {
    int a, b, c;
    int tmp;
    while (true) {
        std::cin >> a >> b >> c;
        if ((a == 0) && (b == 0) && (c == 0)) {
            break;
        }
        
        if (a > b) {
            tmp = a;
            a = b;
            b = tmp;
        }

        if (b > c) {
            tmp = b;
            b = c;
            c = tmp;
        }

        if ((a * a + b * b) == (c * c)) {
            std::cout << "right" << "\n";
        } else {
            std::cout << "wrong" << "\n";
        }

    }
    return 0;
}