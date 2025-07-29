// 평균
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    double* scores = new double[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> scores[i];
    }

    double max_score = scores[0];
    for (int i = 0; i < N; ++i) {
        if (max_score < scores[i]) {
            max_score = scores[i];
        }
    }

    for (int i = 0; i < N; ++i) {
        scores[i] = (scores[i] * 100) / max_score;
    }

    double total_score = 0;
    for (int i = 0; i < N; ++i) {
        total_score += scores[i];
    }

    std::cout << total_score / N;

    delete[] scores;

    return 0;
}