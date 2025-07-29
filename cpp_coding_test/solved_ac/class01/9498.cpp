// 시험 성적
#include <iostream>

int main(int argc, char** argv) {
    int score;
    std::cin >> score;

    if ((90 <= score) && (score <= 100)) {
        std::cout << "A";
    } else if ((80 <= score) && (score <= 89)) {
        std::cout << "B";
    } else if ((70 <= score) && (score <= 79)) {
        std::cout << "C";
    } else if ((60 <= score) && (score <= 69)) {
        std::cout << "D";
    } else {
        std::cout << "F";
    }

    return 0;
}