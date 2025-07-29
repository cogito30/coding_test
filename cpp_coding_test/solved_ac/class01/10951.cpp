// A+B - 4
#include <iostream>

int main(int argc, char** argv) {
    while (true) {
        int A, B;
        std::cin >> A >> B;

        if (std::cin.eof()) {
            break;
        }

        std::cout << A + B << "\n";
    }

    return 0;
}