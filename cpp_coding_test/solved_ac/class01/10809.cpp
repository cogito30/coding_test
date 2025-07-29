// 알파벳 찾기
#include <iostream>

int main(int argc, char** argv) {
    std::string S;
    std::cin >> S;

    int arr[26] = {0};
    int idx = 0;
    for (int i = 0; i < 26; ++i) {
        arr[i] = -1;
    }
    
    for (int i = 0; i < S.length(); ++i) {
        idx = S[i] - 'a';
        if (arr[idx] == -1) {
            arr[idx] = i;
        }
    }

    for (int i = 0; i < 26; ++i) {
        std::cout << arr[i] << " ";
    }

    return 0;
}