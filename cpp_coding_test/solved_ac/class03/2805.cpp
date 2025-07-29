// 나무 자르기
// 자료형 주의
// total_sum == M {break;} 사용시 틀림
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    long long N;
    long long M;
    std::cin >> N >> M;

    std::vector<int> trees;
    long long tree;
    for (int i = 0; i < N; ++i) {
        std::cin >> tree;
        trees.push_back(tree);
    }

    long long start = 1;
    long long end = 1000000000;
    long long mid = 0;
    long long total_sum = 0;
    while (start <= end) {
        mid = (start + end) / 2;
        total_sum = 0;
        for (int i = 0; i < N; ++i) {
            if (trees[i] > mid) {
                total_sum += trees[i] - mid;
            }
        }
        
        if (total_sum >= M) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    std::cout << end;

    return 0;
}