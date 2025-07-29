// 무작위로 K개의 수 뽑기
// c++의 unique는 정렬하지 않는 경우 중복되는 숫자 존재
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer(k, -1);
    map<int, int> map;
    int j = 0;
    for (int i = 0; i < arr.size(); ++i) {
        if (map[arr[i]]++ == 0) {
            answer[j] = arr[i];
            j++;
        }
        if (j >= k) {
            break;
        }
    }
    return answer;
}