// 랜선 자르기
// int 사용시 범위 문제. long long 사용
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    int K, N;
    std::cin >> K >> N;

    long long num;
    std::vector<long long> wires;
    for (int i = 0; i < K; ++i) {
        std::cin >> num;
        wires.push_back(num);
    }

    sort(wires.begin(), wires.end());
    long long start = 1;
    long long end = wires[K-1];
    long long mid = 0;
    long long count = 0;
    while (start <= end) {
        mid = (start + end) / 2;
        count = 0;
        for (int i =0; i <  K; ++i) {
            count += wires[i] / mid;
        }

        if (count < N) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    std::cout << end;

    return 0;
}