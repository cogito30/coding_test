// ACM 호텔
#include <iostream>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        int H, W, N;
        std::cin >> H >> W >> N;

        int q = N % H;
        int r = N / H + 1;

        if (q == 0) {
            q = H;
            r = N / H;
        }

        std::cout << q * 100 + r << "\n";
    }

    return 0;
}