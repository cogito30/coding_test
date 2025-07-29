// 학점계산
#include <iostream>

int main(int argc, char** argv) {
    std::string str;
    std::cin >> str;
    // 소수점 고정을 하지 않으면 틀림
    std::cout << std::fixed;
    std::cout.precision(1);

    if (str == "A+") {
        std::cout << 4.3 ;
    } else if (str == "A0") {
        std::cout << 4.0 ;
    } else if (str == "A-") {
        std::cout << 3.7 ;
    } else if (str == "B+") {
        std::cout << 3.3 ;
    } else if (str == "B0") {
        std::cout << 3.0 ;
    } else if (str == "B-") {
        std::cout << 2.7 ;
    } else if (str == "C+") {
        std::cout << 2.3 ;
    } else if (str == "C0") {
        std::cout << 2.0 ;
    } else if (str == "C-") {
        std::cout << 1.7 ;
    } else if (str == "D+") {
        std::cout << 1.3 ;
    } else if (str == "D0") {
        std::cout << 1.0 ;
    } else if (str == "D-") {
        std::cout << 0.7 ;
    } else if (str == "F") {
        std::cout << 0.0 ;
    }

    return 0;
}


/*
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    string grade;
    cin >> grade;

    double score = 0;
    cout << fixed;
    cout.precision(1);

    switch(grade[0])
    {
        case 'A':
            score = 4.0;
            break;
        case 'B':
            score = 3.0;
            break;
        case 'C':
            score = 2.0;
            break;
        case 'D':
            score = 1.0;
            break;
        case 'F':
            score = 0.0;
            break;
    }

    switch(grade[1])
    {
        case '+':
            score += 0.3;
            break;
        case '-':
            score -= 0.3;
            break;
    }

    cout << score;

    return 0;
}
*/