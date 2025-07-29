// 팩토리얼 0의 개수
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int count_two = 0;
    int count_five = 0;
    for (int i = 1; i <= N; ++i) {
        int num = i;
        while (num % 2 == 0) {
            count_two++;
            num /= 2;
        }
        while (num % 5 == 0) {
            count_five++;
            num /=5;
        }
    }

    if (count_two < count_five) {
        std::cout << count_two;
    } else if (count_two >= count_five) {
        std::cout << count_five;
    }

    return 0;
}

/* 시간초과
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    long long factorial_num = 1;
    for (int i = 1; i <= N; ++i) {
        factorial_num *= i;
    }

    int count = 0;
    while(factorial_num % 10 == 0) {
        factorial_num /= 10;
        count++;
    }

    std::cout << count;

    return 0;
}
*/