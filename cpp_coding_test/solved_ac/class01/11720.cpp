// 숫자의 합
// 큰 숫자는 문자열로 처리
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::string str;
    std::cin >> N;
    std::cin >> str;

    int total_num = 0;
    for (int i = 0; i < N; ++i) {
        total_num += str[i] - '0';
    }

    std::cout << total_num;

    return 0;
}