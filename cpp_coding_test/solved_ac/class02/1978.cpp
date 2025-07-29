// 소수 찾기
#include <iostream>

int is_prime(int num) {
    if (num <= 1) {
        return false;
    }
    // 등호(범위) 주의
    for (int i = 2; i*i <= num; ++i) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int count = 0;
    for (int i = 0; i < N; ++i) {
        if (is_prime(arr[i])) {
            count++;
        }
    }

    std::cout << count;

    return 0;
}