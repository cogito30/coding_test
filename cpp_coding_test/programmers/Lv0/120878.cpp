// 유한소수 판별하기
#include <string>
#include <vector>

using namespace std;

int gcd(int num1, int num2) {
    int tmp = 0;
    if (num1 > num2) {
        tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
    
    while (num2 != 0) {
        tmp = num1;
        num1 = num2;
        num2 = tmp % num2;
    }
    return num1;
}

int solution(int a, int b) {
    int answer = 1;
    int gcd_num = gcd(a, b);
    b = b / gcd_num;
    while (true) {
        while (b % 2 == 0) {
            b /= 2;
        }
        while (b % 5 == 0) {
            b /= 5;
        }
        break;
    }
    if (b > 1) {
        answer = 2;
    }
    return answer;
}