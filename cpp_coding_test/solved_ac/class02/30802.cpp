// 웰컴 키트
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    int* arr = new int[6];
    for (int i = 0; i < 6; ++i) {
        std::cin >> arr[i];
    }
    int T, P;
    std::cin >> T >> P;

    int count = 0;
    for (int i = 0; i < 6; ++i) {
        count += arr[i] / T;
        if (arr[i] % T != 0) {
            count += 1;
        }
    }
    
    std::cout << count << "\n";
    std::cout << N / P << " " << N % P;

    delete[] arr;

    return 0;
}