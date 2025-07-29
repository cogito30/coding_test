// 겹치는 선분의 길이
// 인덱스 위치 주의! 시작점 기준
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    vector<int> lines2(200, 0);
    for (int i = 0; i < lines.size(); ++i) {
        for (int j = lines[i][0]; j < lines[i][1]; ++j) {
            lines2[100 + j]++;
        }
    }
    for (int i = 0; i < 200; ++i) {
        if (lines2[i] > 1) {
            answer++;
        }
    }
    return answer;
}