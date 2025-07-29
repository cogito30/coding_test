// 영화감독 숌
#include <iostream>

bool check_666(int num) {
    int count_six = 0;
    int r = 0;
    while (num > 0) {
        r = num % 10;
        num /= 10;

        if (r == 6) {
            count_six++;
        } else {
            count_six = 0;
        }

        if (count_six == 3) {
            return true;    
        }
    }
    return false;
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int count = 0;
    int num = 0;
    while (true) {
        num++;
        if (check_666(num)){
            count++;
        }

        if (count == N) {
            break;
        }
    }
    std::cout << num;

    return 0;
}