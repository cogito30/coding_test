// 영어가 싫어요
#include <string>
#include <vector>

using namespace std;

long long solution(string numbers) {
    long long answer = 0;
    vector<string> num_str = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int start = 0;
    for (int i = 0; i < numbers.length(); ++i) {
        for (int j = 0; j < num_str.size(); ++j) {
            if (numbers.substr(start, i - start + 1) == num_str[j]) {
                answer *= 10;
                answer += j;
                start = i + 1;
            }    
        }
        
    }
    return answer;
}

/* 확인해볼 풀이
#include <string>
#include <vector>

using namespace std;

long long solution(string numbers) {
    long long answer = 0;
    vector<string> num = {
        "zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    };
    int tmp;

    for (int i=0; i<num.size(); i++)
    {
        while ((tmp = numbers.find(num[i])) != string::npos)
        {
            numbers.replace(tmp, num[i].size(), to_string(i));
        }
    }
    answer = stoll(numbers);
    return answer;
}
*/