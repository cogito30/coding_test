// 삼각형의 완성조건 (2)
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    if (sides[0] > sides[1]) {
        swap(sides[0], sides[1]);
    }
    
    for (int i = 1; i < sides[1]; ++i) {
        if ((sides[0] + i) > sides[1]) {
            answer++;
        }
    }
    for (int i = sides[1]; i < sides[0] + sides[1]; ++i) {
        if ((sides[0] + sides[1]) > i) {
            answer++;
        }
    }
    
    return answer;
}