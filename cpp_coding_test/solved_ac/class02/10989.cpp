// 수 정렬하기 3
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int arr[10001] = {0};
    int num = 0;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        arr[num]++;
    }

    for (int i = 0; i < 10001; ++i) {
        for (int j = 0; j < arr[i]; ++j)
            std::cout << i << "\n";
    }

    return 0;
}


/* 메모리 초과
#include <iostream>
#include <algorithm>
#include <vector>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<int> vec;
    int num = 0;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        vec.push_back(num);
    }

    std::sort(vec.begin(), vec.end());

    for (int i = 0; i < vec.size(); ++i) {
        std::cout << vec[i] << "\n";
    }

    return 0;
}
*/ 

/*
#include <iostream>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int* arr = new int[N];
    for (int i = 0; i < N; ++i) {
        std::cin >> arr[i];
    }

    std::sort(arr, arr + N);

    for (int i = 0; i < N; ++i) {
        std::cout << arr[i] << "\n";
    }

    return 0;
}
*/