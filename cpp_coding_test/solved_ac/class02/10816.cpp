// 숫자 카드 2
// std::map에서 []사용시 key가 없을 떄 기본 값으로 생성
// 입출력(std::cin.tie(0)) 처리하지 않으면 시간 초과
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    std::ios::sync_with_stdio(false);
	std::cin.tie(0);

    int N;
    std::cin >> N;

    std::vector<int> cards;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        cards.push_back(num); 
    }

    std::sort(cards.begin(), cards.end());

    int M;
    std::cin >> M;

    for (int i = 0; i < M; ++i) {
        std::cin >> num;

        auto lower = std::lower_bound(cards.begin(), cards.end(), num);
        auto upper = std::upper_bound(cards.begin(), cards.end(), num);

        std::cout << (upper - lower) << " ";
    }

    return 0;
}

/* 시간초과(std::cin.tie(0) 사용시 통과)
#include <iostream>
#include <unordered_map>

int main(int argc, char** argv) {
    std::ios::sync_with_stdio(false);
	std::cin.tie(0);

    int N;
    std::cin >> N;

    std::unordered_map<int, int> card_count;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        card_count[num]++;  
    }

    int M;
    std::cin >> M;

    for (int i = 0; i < M; ++i) {
        std::cin >> num;
        std::cout << card_count[num] << " ";
    }

    return 0;
}
*/