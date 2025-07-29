// 사칙연산
#include <iostream>>

int main(int argc, char** argv) {
    int A, B;
    std::cin >> A;
    std::cin >> B;

    std::cout << A + B << "\n";
    std::cout << A - B << "\n";
    std::cout << A * B << "\n";
    std::cout << A / B << "\n";
    std::cout << A % B << "\n";
    return 0;
}