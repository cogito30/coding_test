// 최소, 최대
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int max_val = -1000000;
    int min_val = 1000000; 
    for (int i = 0; i < N; ++i) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }

        if (arr[i] < min_val) {
            min_val = arr[i];
        }
    }

    std::cout << min_val << " " << max_val;

    delete[] arr;
    
    return 0;
}