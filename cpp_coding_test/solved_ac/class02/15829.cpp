// Hashing
// 자료형 범위 고려!!
// 긴문자열을 고려해서 연산시 모듈러 연산 반복
#include <iostream>

int main(int argc, char** argv) {
    int L;
    std::string str;
    std::cin >> L;
    std::cin >> str;

    long long result = 0;
    long long square_31 = 1; 
    for (int i = 0; i < L; ++i) {
        result += ((str[i] - 'a' + 1) * (square_31));
        square_31 *= 31;
        result %= 1234567891;
        square_31 %= 1234567891;
    }

    std::cout << result;
    return 0;
}