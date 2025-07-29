// 진료 순서 정하기
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> emergency2(emergency);
    sort(emergency2.begin(), emergency2.end(), greater<int>());

    unordered_map<int, int> map;
    for (int i = 0; i < emergency2.size(); ++i) {
        map[emergency2[i]] = i + 1;
    }

    for (int i = 0; i < emergency.size(); ++i) {
        answer.push_back(map[emergency[i]]);
    }

    return answer;
}