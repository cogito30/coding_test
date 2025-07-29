// 짝수 홀수 개수
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    int odd_count = 0;
    int even_count = 0;
    for (int i = 0; i < num_list.size(); ++i)  {
        if (num_list[i] % 2 == 0) {
            even_count++;
        } else {
            odd_count++;
        }
    }
    answer.push_back(even_count);
    answer.push_back(odd_count);
    return answer;
}