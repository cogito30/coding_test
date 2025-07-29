// A로 B로 만들기
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string before, string after) {
    int answer = 1;
    vector<char> q1;
    vector<char> q2;
    for (int i = 0; i < after.length(); ++i) {
        q1.push_back(before[i]);
        q2.push_back(after[i]);
    }
    sort(q1.begin(), q1.end());
    sort(q2.begin(), q2.end());
    for (int i = 0; i < after.length(); ++i) {
        if (q1[i] != q2[i]) {
            answer = 0;
            break;
        }
    }
    return answer;
}