// IOIOI
#include <iostream>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    int N;
    std::cin >> N;
    int M;
    std::cin >> M;
    std::string str;
    std::cin >> str;
    
    int i = 1;
    int io_count = 0;
    int count = 0;
    while (i < M) {
        if ((str[i-1] == 'I') && (str[i] == 'O') && (str[i+1] == 'I')) {
            io_count++;
            i += 2;
        } else {
            io_count = 0;
            i += 1;
        }

        if (io_count >= N) {
            count++;
        }
    }

    std::cout << count;

    return 0;
}


/* 50점
#include <iostream>

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    int N;
    std::cin >> N;
    int M;
    std::cin >> M;
    std::string str;
    std::cin >> str;

    std::string P = "I";
    for (int i = 0; i < N; ++i) {
        P += "OI";
    }
    
    int i = 0;
    int count = 0;
    while (i < M) {
        if (P == str.substr(i, N*2 + 1)) {
            count++;
            i += 2;
        } else {
        i += 1;
        }
    }

    std::cout << count;

    return 0;
}
*/