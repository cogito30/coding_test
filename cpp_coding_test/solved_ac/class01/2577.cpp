// 숫자의 개수
#include <iostream>

int main(int argc, char** argv) {
    int A, B, C;
    std::cin >> A;
    std::cin >> B;
    std::cin >> C;

    int count_num[10] = {0};
    int total_mul = A * B * C;
    while (total_mul > 0) {
        count_num[total_mul % 10]++;
        total_mul /= 10;
    }

    for (int i = 0; i < 10; ++i) {
        std::cout << count_num[i] << "\n";
    }

    return 0;
}