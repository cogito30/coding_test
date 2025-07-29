// 단어 정렬
// set은 자동으로 사전순 정렬 진행!!!
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

bool compare(std::string s1, std::string s2) {
    if (s1.length() == s2.length()) {
        return s1 < s2;
    } else {
        return s1.length() < s2.length();
    }
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::vector<std::string> vec;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        vec.push_back(str);
    }

    // 중복 제거 후 정렬 순서 중요
    std::sort(vec.begin(), vec.end());
    vec.erase(std::unique(vec.begin(), vec.end()), vec.end());

    std::sort(vec.begin(), vec.end(), compare);

    for (const auto& word : vec) {
        std::cout << word << "\n";
    }

    return 0;
}

/*
#include <iostream>
#include <algorithm>

bool compare(std::string s1, std::string s2) {
    if (s1.length() == s2.length()) {
        return s1 < s2;
    } else {
        return s1.length() < s2.length();
    }
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::vector<std::string> vec;
    for (int i = 0; i < N; ++i) {
        std::cin >> str;
        vec.push_back(str);
    }

    sort(vec.begin(), vec.end(), compare);

    // 중복제거
    std::string tmp = "";
    for (int i = 0; i < N; i++)
    {
        if (tmp != vec[i])
        {
            std::cout << vec[i] << "\n"; 
            tmp = vec[i];
        }
    }

    return 0;
}
*/