// 머쓱이보다 키 큰 사람
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array, int height) {
    int answer = 0;
    for (int i = 0; i < array.size(); ++i) {
        if (array[i] > height) {
            answer ++;
        }
    }
    return answer;
}