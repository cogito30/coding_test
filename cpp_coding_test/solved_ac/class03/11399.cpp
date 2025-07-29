//ATM
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::vector<int> people;
    int num;
    for (int i = 0; i < N; ++i) {
        std::cin >> num;
        people.push_back(num);
    }
    
    std::sort(people.begin(), people.end());
    
    int total_time = 0;
    for (int i = 0; i < N; ++i) {
        total_time += people[i] * (N - i);
    }
    
    std::cout << total_time;
    
    return 0;
}