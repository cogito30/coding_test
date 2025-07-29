// 공 던지기
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> numbers, int k) {
    int answer = 0;
    queue<int> q;
    for (int i = 0; i < numbers.size(); ++i) {
        q.push(numbers[i]);
    }
    
    for (int i = 0; i < k; ++i) {
        answer = q.front();
        for (int j = 0; j < 2; ++j){
            q.push(q.front());
            q.pop();
        }
    }
    
    
    return answer;
}