// 별찍기 - 1
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    for (int i = 0 ; i < N; ++i) {
        for (int j = 0; j < (i + 1); ++j) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
    return 0;
}