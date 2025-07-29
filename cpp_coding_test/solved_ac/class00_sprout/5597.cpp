// 과제 안 내신 분..?
#include <iostream>

int main(int argc, char** argv) {
    int student[31] = {0};

    int num;
    for (int i = 0; i < 28; ++i){
        std::cin >> num;
        student[num]++;
    }
    
    // 1번부터 시작
    for (int i = 1; i < 31; ++i){
        if (student[i] == 0) {
            std::cout << i << "\n";
        }
    }

    return 0;
}