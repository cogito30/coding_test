// 빠른 A+B
#include <iostream>

int main(int argc, char** argv) {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int T;
    std::cin >> T;
    
    for (int i = 0; i < T; ++i) {
        int A, B;
        std::cin >> A >> B;
        std::cout << A + B << "\n";
    }

    return 0;
}