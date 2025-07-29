// 최대공약수와 최소공배수
#include <iostream>

int gcd(int a, int b) {
    int tmp;
    if (a > b) {
        tmp = a;
        a = b;
        b = tmp;
    }

    while (b != 0) {
        tmp = a;
        a = b;
        b = tmp % b;
    }

    return a;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main(int argc, char** argv) {
    int a, b;
    std::cin >> a >> b;

    std::cout << gcd(a, b) << "\n";
    std::cout << lcm(a, b);

    return 0;
}