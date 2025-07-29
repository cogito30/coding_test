// 별 찍기 - 2
#include <iostream>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < (N - i - 1); ++j) {
            std::cout << " ";
        }
        for (int k = 0; k < (i + 1); ++k) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
    return 0;
}

/* 
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    int N;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (j < N-i-1)
                cout << " ";
            else
                cout << "*";
        }
        cout << endl;
    }
    return 0;
}
*/