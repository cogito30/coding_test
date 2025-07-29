// 체스판 다시 칠하기
#include <iostream>
#include <vector>

int check_board_color(int start_row, int start_col, std::vector<std::string>& board) {
    int white_count = 0;
    int black_count = 0;
    for (int i = start_row; i < start_row + 8; ++i) {
        for (int j = start_col; j < start_col + 8; ++j) {
            if ((i + j) % 2 == 0) {
                if (board[i][j] == 'B') {
                    white_count++;
                } else {
                    black_count++;
                }
            } else {
                if (board[i][j] == 'W') {
                    white_count++;
                } else {
                    black_count++;
                }
            }
        }
    }
    if (white_count > black_count) {
        return black_count;
    } else {
        return white_count;
    }
}

int main(int argc, char** argv) {
    int N, M;
    std::cin >> N >> M;

    std::vector<std::string> board;
    std::string line;
    for (int i = 0; i < N; ++i) {
        std::cin >> line;        
        board.push_back(line);
    }

    int min_val = 64;
    int result = 0;
    for (int i = 0; i < N - 7; ++i) {
        for (int j = 0; j < M - 7; ++j) {
            result = check_board_color(i, j, board);
            if (result < min_val) {
                min_val = result;
            }
        }
    }
    std::cout << min_val;
    return 0;
}