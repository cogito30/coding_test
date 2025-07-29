// A+B - 5
#include <iostream>

int main(int argc, char** argv) {
    while (true) {
        int A, B;
        std::cin >> A >> B;
        
        if ((A == 0) && (B == 0)) {
            break;
        }

        std::cout << A + B << "\n";
    }

    return 0;
}