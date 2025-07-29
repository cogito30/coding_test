// A + B - C
// <string>의 stoi와 to_string으로 문자열 숫자간 변환
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::string A, B, C;
    std::cin >> A;
    std::cin >> B;
    std::cin >> C;

    std::cout << std::stoi(A) + std::stoi(B) - std::stoi(C) << "\n";
    std::cout << std::stoi(A + B) - std::stoi(C);

    return 0;
}