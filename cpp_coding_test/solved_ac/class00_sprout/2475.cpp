// 검증수
#include <iostream>

int func(const int arr[], int size) {
    int result;
    result = 0;
    for (int i = 0; i < size; ++i) {
        result += (arr[i] * arr[i]) % 10;
    }
    result %= 10;
    return result;
}

int main(int argc, char** argv) {
    int num;
    int arr[5] = {0};
    for (int i = 0; i < 5; ++i) {
        std::cin >> num;
        arr[i] = num;
    }

    std::cout << func(arr, 5);
    return 0;
}