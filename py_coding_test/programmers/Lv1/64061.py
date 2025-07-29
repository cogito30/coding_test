# 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                stack.append(board[row][move-1])
                board[row][move-1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2] :
            answer += 2
            stack.pop()
            stack.pop()

    return answer