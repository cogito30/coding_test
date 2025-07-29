# 가장 많이 받은 선물
def solution(friends, gifts):
    answer = 0
    N = len(friends)
    gift_count = [[0 for _ in range(N)] for _ in range(N)]
    gift_score = [0 for _ in range(N)]
    score = [0 for _ in range(N)]
    for gift in gifts:
        give, rec = gift.split()
        give_idx = friends.index(give)
        rec_idx = friends.index(rec)
        gift_count[give_idx][rec_idx] += 1
    
    for i in range(N):
        give_score = 0
        rec_score = 0
        for j in range(N):
            give_score += gift_count[i][j]
        for k in range(N):
            rec_score += gift_count[k][i]
        gift_score[i] = give_score - rec_score
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            elif gift_count[i][j] > gift_count[j][i]:
                score[i] += 1
            elif gift_count[i][j] == gift_count[j][i]:
                if gift_score[i] > gift_score[j]:
                    score[i] += 1                    
    answer = max(score)
    return answer 