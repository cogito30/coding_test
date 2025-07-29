// 나머지
#include <iostream>

int main(int argc, char** argv) {
    int num = 0;
    int arr[42] = {0};
    for (int i = 0; i < 10; ++i) {
        std::cin >> num;
        arr[num % 42]++;
    }

    int count = 0;
    for (int i = 0; i < 42; ++i) {
        if (arr[i] != 0) {
            count++;
        }
    }

    std::cout << count;

    return 0;
}