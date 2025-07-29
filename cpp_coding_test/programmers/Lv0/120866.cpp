// 안전지대
#include <string>
#include <vector>
#include <iostream>

using namespace std;

void check(int row, int col, vector<vector<int>>& board) {
    int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
    int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            if (row + dx[i] < 0 || row + dx[i] >= board.size() || col + dy[i] < 0 || col + dy[i] >= board.size()) {
                continue;
            }
            board[row + dx[i]][col + dy[i]] = 1;
        }
    }
    return;
}

int solution(vector<vector<int>> board) {
    int answer = 0;
    vector<vector<int>> board2(board);
    for (int row = 0; row < board.size(); ++row) {
        for (int col = 0; col < board[0].size(); ++col) {
            if (board[row][col] == 1) {
                check(row, col, board2);
            }
        }
    }
    for (int row = 0; row < board2.size(); ++row) {
        for (int col = 0; col < board2[0].size(); ++col) {
            if (board2[row][col] == 0) {
                answer++;
            }
        }
    }
    
    return answer;
}