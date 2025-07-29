// 좌표 압축
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    int num;
    std::vector<int> cor1, cor2;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        cor1.push_back(num);
        cor2.push_back(num);
    }

    std::sort(cor1.begin(), cor1.end());
    cor1.erase(std::unique(cor1.begin(), cor1.end()), cor1.end());

    for (int i = 0; i < N; ++i){
        std::cout << std::lower_bound(cor1.begin(), cor1.end(), cor2[i]) - cor1.begin() << " ";
    }

    return 0;
}