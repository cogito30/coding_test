// 최댓값
#include <iostream>

int main(int argc, char** argv) {
    int num = 0;
    int max_val = 0;
    int max_val_idx = 0;

    for (int i = 0; i < 9; ++i) {
        std::cin >> num;
        if (num > max_val) {
            max_val = num;
            max_val_idx = i + 1;
        }
    }

    std::cout << max_val << "\n";
    std::cout << max_val_idx << "\n";

    return 0;
}