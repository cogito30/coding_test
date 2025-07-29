// 음계
#include <iostream>

int main(int argc, char** argv) {
    int* arr = new int[8];
    for (int i = 0; i < 8; ++i) {
        std::cin >> arr[i];
    }

    bool asc = true;
    bool desc = true;
    for (int i = 0; i < 7; ++i) {
        if (arr[i] < arr[i+1]) {
            desc = false;
        } else {
            asc = false;
        }
    }

    if (asc && !desc) {
        std::cout << "ascending";
    } else if (!asc && desc) {
        std::cout << "descending";
    } else {
        std::cout << "mixed";
    }

    return 0;
}