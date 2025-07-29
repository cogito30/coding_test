// 나이순 정렬
#include <iostream>
#include <vector>
#include <algorithm>

bool compare(std::pair<int, std::string> arg1, std::pair<int, std::string> arg2) {
    if (arg1.first < arg2.first) {
        return true;
    }
    return false;
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;

    std::vector<std::pair<int, std::string>> vec;
    int age;
    std::string name;
    for (int i = 0; i < N; ++i) {
        std::cin >> age >> name;
        vec.push_back({age, name});
    }

    std::stable_sort(vec.begin(), vec.end(), compare);

    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << it->first << " " << it->second << " ";
    }

    return 0;
}