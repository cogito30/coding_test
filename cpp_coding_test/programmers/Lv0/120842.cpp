// 2차원으로 만들기
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    vector<vector<int>> answer;
    for (int i = 0; i < num_list.size()/n; ++i) {
        vector<int> row;
        answer.push_back(row);
        for (int j = 0; j < n; ++j) {
            answer[i].push_back(num_list[i*n + j]);
        }
    }
    return answer;
}