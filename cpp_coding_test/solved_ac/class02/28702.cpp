// FizzBuzz
#include <iostream>

bool is_number(std::string& str) {
    int length = str.length();
    for (int i = 0; i < length; ++i) {
        if (('0' > str[i]) || (str[i] > '9')) {
            return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    std::string str1, str2, str3;
    std::cin >> str1 >> str2 >> str3;

    int result = 0;
    if (is_number(str3)) {
        result = std::stoi(str3) + 1;
    } else if (is_number(str2)) {
        result = std::stoi(str2) + 2;
    } else if (is_number(str1)) {
        result = std::stoi(str1) + 3;
    }

    if ((result % 3 == 0) && (result % 5 == 0)) {
        std::cout << "FizzBuzz";
    } else if (result % 3 == 0) {
        std::cout << "Fizz";
    } else if (result % 5 == 0) {
        std::cout << "Buzz";
    } else {
        std::cout << result;
    }

    return 0;
}