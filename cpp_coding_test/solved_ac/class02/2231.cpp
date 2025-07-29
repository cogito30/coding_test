// 분해합
// 생성자가 없는 경우 주의!
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int answer = 0;
    for (int i = 1; i <= N; ++i) {
        int total_sum = i;
        int num = i;
        while (num > 0) {
            total_sum += num % 10;
            num /= 10;
        }

        if (total_sum == N) {
            answer = i;
            break;
        }
    }
    std::cout << answer;

    return 0;
}