// X보다 작은 수
// 동적 할당을 하지 않고 arr[N]을 사용할 경우 컴피일 에러
#include <iostream>

int main(int argc, char** argv) {
    int N, X;
    std::cin >> N >> X;

    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    for (int i = 0; i < N; ++i){
        if (arr[i] < X) {
            std::cout << arr[i] << " ";
        }
    }

    delete[] arr;

    return 0;
}

/* 배열 없는 풀이
int main(int argc, char** argv) {
    int N, X;
    std::cin >> N >> X;

    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        if (num < X) {
            std::cout << num << " ";
        }
    }
    return 0;
}
*/ 