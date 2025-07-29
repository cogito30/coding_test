// 외계어 사전
// 조건 확인!! 중복된 원소 없음
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> spell, vector<string> dic) {
    int answer = 2;
    for (auto& word: dic) {
        bool check = true;
        for (auto& alpha: spell) {
            if (word.find(alpha) == string::npos) {
                check = false;
                break;
            }
        }
        if (check) {
            answer = 1;
        }
    }
    return answer;
}