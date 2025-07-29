// 달팽이는 올라가고 싶다
// V <= A + (A-B) * (i-1)
#include <iostream>

using ll = long long;

int main(int argc, char** argv) {
    ll A, B, V;
    std::cin >> A >> B >> V;

    int result = (V - A) / (A - B) + 1;

    if (((V - A) % (A - B)) != 0) {
        result += 1;
    }

    std::cout << result;

    return 0;
}

/*
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    int A, B, V;
    cin >> A >> B >> V;

    int day;
    day = (V-B) / (A-B);
    if ((V-B) % (A-B) == 0)
        cout << day;
    else
        cout << day + 1;
    return 0;
}
*/ 

/* 시간초과
#include <iostream>

using ll = long long;

int main(int argc, char** argv) {
    ll A, B, V;
    std::cin >> A >> B >> V;

    ll total_distance = 0;
    int count = 0;
    while (true) {
        count++;
        total_distance += A;
        if (total_distance >= V) {
            break;
        }
        total_distance -= B;
    }

    std::cout << count;

    return 0;
}
*/ 