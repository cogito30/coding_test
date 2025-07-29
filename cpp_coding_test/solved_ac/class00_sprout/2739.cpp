// 구구단
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    for (int i = 1; i < 10; ++i) {
        std::cout << N << " * " << i << " = " << N * i << "\n";
    }

    return 0;
}