//동전 0
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    int N, K;
    std::cin >> N >> K;
    std::vector<int> A;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        A.push_back(num);
    }
    
    int result = 0;
    for (int i = A.size() - 1; i >= 0; --i) {
        result += K / A[i];
        K %= A[i];
    }

    std::cout << result;

    return 0;
}