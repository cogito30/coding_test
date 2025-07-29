// 단어의 개수
// 문자열이 공백으로 시작하거나 끝나는 경우 주의
#include <iostream>

int main(int argc, char** argv) {
    std::string line;
    getline(std::cin, line);

    int count = 1;
    for (int i = 0; i < line.length(); ++i) {
        if (line[i] == ' ') {
            count++;
        }
    }

    if (line[0] == ' ') {
        count--;
    }
    
    if (line[line.length() - 1] == ' ') {
        count--;
    }

    std::cout << count;

    return 0;
}