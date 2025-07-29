// 이상한 기호
// 자료형 범위 주의
#include <iostream>

using ll = long long;

ll func(ll a, ll b) {
    return (a + b) * (a - b);
}

int main(int argc, char** argv) {
    long long A, B;
    std::cin >> A >> B;
    std::cout << func(A, B);

    return 0;
}