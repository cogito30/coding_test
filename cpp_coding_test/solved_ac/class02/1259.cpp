// 팰린드롬수
#include <iostream>

int main(int argc, char** argv) {
    std::string str;
    std::string result;
    
    while (true) {
        std::cin >> str;
        int size = str.length();
        result = "yes";

        if (str[0] == '0') {
            break;
        }

        for (int i = 0; i < size; ++i) {
            if (str[i] != str[size-i-1]) {
                result = "no";
            }
        }
        std::cout << result << "\n";
    }

    return 0;
}