// 이진수 더하기
#include <string>
#include <vector>

using namespace std;

string solution(string bin1, string bin2) {
    string answer = "";
    int idx1 = bin1.length() - 1;
    int idx2 = bin2.length() - 1;
    int carry = 0;
    vector<char> num_list;
    while (idx1 >= 0 && idx2 >= 0) {
        if (bin1[idx1] == '1' && bin2[idx2] == '1') {
            if (carry == 1) {
                num_list.push_back('1');    
            } else {
                num_list.push_back('0');
            }
            carry = 1;
        } else if (bin1[idx1] == '1' || bin2[idx2] == '1') {
            if (carry == 1) {
                num_list.push_back('0');
                carry = 1;
            } else {
                num_list.push_back('1');
            }
        } else if (bin1[idx1] == '0' && bin2[idx2] == '0') {
            if (carry == 1) {
                num_list.push_back('1');
            } else {
                num_list.push_back('0');
            }
            carry = 0;
        }
        idx1--;
        idx2--;
    }
    while (idx1 >= 0) {
        if (bin1[idx1] == '1' && carry == 1) {
            num_list.push_back('0');
            carry = 1;
        } else if (bin1[idx1] == '1' || carry == 1) {
            num_list.push_back('1');
            carry = 0;
        } else {
            num_list.push_back('0');
            carry = 0;
        }
        idx1--;
    }
    while (idx2 >= 0) {
        if (bin2[idx2] == '1' && carry == 1) {
            num_list.push_back('0');
            carry = 1;
        } else if (bin2[idx2] == '1' || carry == 1) {
            num_list.push_back('1');
            carry = 0;
        } else {
            num_list.push_back('0');
            carry = 0;
        }
        idx2--;
    }
    if (carry == 1) {
        num_list.push_back('1');
    }
    
    for (int i = num_list.size() - 1; i >= 0; --i) {
        answer += num_list[i];
    }
    return answer;
}

/* bitset 사용
// 0, 0 입력시 0 출력 주의!!
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

string solution(string bin1, string bin2) {
    string answer = "";
    bitset<10> bit1(bin1);
    bitset<10> bit2(bin2);
    
    int sum = bit1.to_ulong() + bit2.to_ulong();
    
    while (sum > 0) {
        answer += to_string(sum % 2);
        sum /= 2;
    }
    reverse(answer.begin(), answer.end());
    
    if (answer == "") {
        answer = "0";
    }
    return answer;
}
*/