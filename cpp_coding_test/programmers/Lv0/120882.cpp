// 등수 매기기
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<vector<int>> score) {
    vector<int> answer(score.size(), 0);
    vector<int> sorted_score;
    for (int i = 0; i < score.size(); ++i) {
        sorted_score.push_back(score[i][0] + score[i][1]);
    }
    
    sort(sorted_score.begin(), sorted_score.end(), greater<int>());
    sorted_score.erase(unique(sorted_score.begin(), sorted_score.end()), sorted_score.end());
    int count = 0;
    int rank = 1;
    for (int i = 0; i < sorted_score.size(); ++i) {
        count = 0;
        for (int j = 0; j < score.size(); ++j) {
            if (sorted_score[i] == (score[j][0] + score[j][1])) {
                answer[j] = rank;
                count++;
            }
        }
        rank += count;
    }
    return answer;
}