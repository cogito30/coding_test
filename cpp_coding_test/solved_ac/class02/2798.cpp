// 블랙잭
#include <iostream>

int main(int argc, char** argv) {
    int N, M;
    std::cin >> N >> M;
    
    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int sum_of_card = 0;
    int max_sum_of_card = 0;
    for (int i = 0; i < N - 2; ++i) {
        for (int j = i + 1; j < N - 1; ++j) {
            for (int k = j + 1; k < N; ++k) {
                sum_of_card = arr[i] + arr[j] + arr[k];
                if ((sum_of_card <= M) && (sum_of_card >= max_sum_of_card)) {
                    max_sum_of_card = sum_of_card;
                }
            }
        }
    }

    std::cout << max_sum_of_card;

    return 0;
}