// 모스부호 (1)
#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

string solution(string letter) {
    string answer = "";
    map<string,string> morse =
    {
        {".-","a"},{"-...","b"},{"-.-.","c"},{"-..","d"},
        {".","e"},{"..-.","f"},{"--.","g"},{"....","h"},
        {"..","i"},{".---","j"},{"-.-","k"},{".-..","l"},
        {"--","m"},{"-.","n"},{"---","o"},{".--.","p"},
        {"--.-","q"},{".-.","r"},{"...","s"},{"-","t"},
        {"..-","u"},{"...-","v"},{".--","w"},{"-..-","x"},
        {"-.--","y"},{"--..","z"}
    };
    
    stringstream ss;
    ss.str(letter);
    string tmp;
    while (true) {
        if (ss.eof()) {
            break;
        } else {
            ss >> tmp;
            answer += morse[tmp];
        }
    }
    return answer;
}