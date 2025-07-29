// A+B - 3
#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        int A, B;
        std::cin >> A >> B;
        std::cout << A + B << "\n";
    }

    return 0;
}