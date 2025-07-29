// 개수 세기
#include <iostream>>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    int v;
    std::cin >> v;

    int answer = 0;
    for (int i = 0; i < N; ++i) {
        if (arr[i] == v) {
            answer++;
        }
    }

    std::cout << answer; 
    
    delete[] arr;

    return 0;
}