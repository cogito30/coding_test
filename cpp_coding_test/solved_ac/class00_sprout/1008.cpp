// A/B
// 소수점 개수 지정시 cout.precision(num) 사용
#include <iostream>

int main(int argc, char** argv) {
    double A, B;
    std::cin >> A;
    std::cin >> B;

    std::cout.precision(10);
    std::cout << A / B << "\n";
    return 0;
}