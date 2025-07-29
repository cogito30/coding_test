// 홀짝 구분하기 
// replace 함수 가능
#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    if (n % 2 == 0) {
        cout << n << " is even";
    } else {
        cout << n << " is odd";
    }
    return 0;
}

/*
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
    string answer = "";
    answer = my_string.replace(s,overwrite_string.size(),overwrite_string);
    return answer;
}
*/