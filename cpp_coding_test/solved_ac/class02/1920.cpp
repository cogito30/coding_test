// 수 찾기
// 이진 탐색 사용하지 않고 전체 순회시 시간초과
#include <iostream>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> A;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        A.push_back(num);
    }
    
    int M;
    std::cin >> M;

    std::vector<int> B;
    for (int i = 0; i < M; ++i) {
        std::cin >> num;
        B.push_back(num);
    }
    
    std::sort(A.begin(), A.end());
    A.erase(std::unique(A.begin(), A.end()), A.end());
    
    for (int i = 0; i < M; ++i) {
        if (std::binary_search(A.begin(), A.end(), B[i])) {
            std::cout << 1 << "\n";
        } else {
            std::cout << 0 << "\n";
        }
    }

    return 0;
}

/* 시간초과
#include <iostream>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> A;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        A.push_back(num);
    }
    
    int M;
    std::cin >> M;

    std::vector<int> B;
    for (int i = 0; i < M; ++i) {
        std::cin >> num;
        B.push_back(num);
    }
    
    std::sort(A.begin(), A.end());
    A.erase(std::unique(A.begin(), A.end()), A.end());
    
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < A.size(); ++j) {
            if (B[i] == A[j]) {
                std::cout << 1 << "\n";
                break;
            }
            
            if (j == A.size() - 1) {
                std::cout << 0 << "\n";
            }
        }
    }

    return 0;
}
*/