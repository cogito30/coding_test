// 벌집
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    int result = 1;
    int total_num = 1;
    while (total_num < N) {
        if ((N > result) && (N <= result)) {
            break;
        }
        total_num += 6 * (result);
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
    int N;
    cin >> N;

    int num=1, cnt=1;
    while (true)
    {
        if (N <= num)
                break;
        num += 6*cnt;
        cnt += 1;
    }
    cout << cnt << endl;
    return 0;
}
*/