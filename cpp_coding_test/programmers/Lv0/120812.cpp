// 최빈값 구하기
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    unordered_map<int, int> num_count;
    for (int i = 0; i < array.size(); ++i) {
        num_count[array[i]]++;        
    }

    int max_val = 0;
    for (auto& p: num_count) {
        if (p.second > max_val) {
            max_val = p.second;
            answer = p.first;
        } else if (p.second == max_val) {
            answer = -1;
        }
    }

    return answer;
}