// 분수의 덧셈
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

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int numer = numer1 * denom2 + numer2 * denom1;
    int denom = denom1 * denom2;
    
    int gcd_num = gcd(numer, denom);
    answer.push_back(numer/gcd_num);
    answer.push_back(denom/gcd_num);
    return answer;
}