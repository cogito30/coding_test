// 특이한 정렬
// 전역변수 사용
// 전체에서 n을 뺀후 정렬하여 n을 더하는 방법도 있음
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int num;

bool compare(int num1, int num2) {
    if (abs(num - num1) == abs(num - num2)) {
        return num1 > num2;
    } else {
        return (abs(num - num1) < abs(num - num2));
    }
}

vector<int> solution(vector<int> numlist, int n) {
    vector<int> answer;
    num = n;
    sort(numlist.begin(), numlist.end(), compare);
    answer = numlist;
    return answer;
}