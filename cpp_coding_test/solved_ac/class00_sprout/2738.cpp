// 행렬 덧셈
#include <iostream>

int main(int argc, char** argv) {
    int N, M;
    std::cin >> N >> M;

    int** mat1 = new int*[N];
    for (int i = 0; i < N; ++i) {
        mat1[i] = new int[M];
        for (int j = 0; j < M; ++j) {
            std::cin >> mat1[i][j];
        }
    }
    int** mat2 = new int*[N];
    for (int i = 0; i < N; ++i) {
        mat2[i] = new int[M];
        for (int j = 0; j < M; ++j) {
            std::cin >> mat2[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            mat1[i][j] += mat2[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            std::cout << mat1[i][j] << " ";
        }
        std::cout << "\n";
    }

    for (int i = 0; i < N; ++i) {
        delete[] mat1[i];
        delete[] mat2[i];
    }
    delete[] mat1;
    delete[] mat2;

    return 0;
}