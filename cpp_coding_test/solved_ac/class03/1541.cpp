// 잃어버린 괄호
#include <iostream>

int main(int argc, char** argv) {
    std::string str;
    getline(std::cin, str);

    int num = 0;
    int result = 0;
    int sign = 1;
    for (int i = 0; i < str.length(); ++i) {
        if (str[i] == '-') {
            result += num * sign;
            sign = -1;
            num = 0;
        } else if (str[i] == '+') {
            result += num * sign;
            num = 0;
        } else {
            num *= 10;
            num += str[i] - '0';
        }
    }

    result += num * sign;
    std::cout << result;

    return 0;
}