// 팩토리얼
#include <iostream>>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    long long answer = 1;
    for (int i = 1; i <= N; ++i) {
        answer *= i;
    }

    std::cout << answer << "\n";
    
    return 0;
}