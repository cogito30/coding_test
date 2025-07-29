// 두 수 비교하기
#include <iostream>

int main(int argc, char** argv) {
    int A, B;
    std::cin >> A >> B;

    if (A > B) {
        std::cout << ">";
    } else if (A < B) {
        std::cout << "<";
    } else {
        std::cout << "==";
    }
    
    return 0;
}