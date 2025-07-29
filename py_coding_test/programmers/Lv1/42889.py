# 실패율
def solution(N, stages):
    answer = []
    player_per_stage = [0 for i in range(N+2)]
    fail_per_stage = [0 for i in range(N+2)]
    total_member = len(stages)
    for i in stages:
        player_per_stage[i] += 1
    
    for i in range(1, N+1):
        # 반례: 2, [1, 1, 1, 1] // [1, 2]
        if total_member == 0:
            fail_per_stage[i] = (0, i)
        else:
            fail_per_stage[i] = (player_per_stage[i]/total_member, i)
            total_member -= player_per_stage[i]
            
    fail_per_stage = fail_per_stage[1:-1]
    fail_per_stage.sort(key=lambda x: (-x[0], x))
    for fail, stage in fail_per_stage:
        answer.append(stage)
    return answer