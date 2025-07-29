# 대충 만든 자판
def solution(keymap, targets):
    answer = []
    # ["AA"], ["AB"] / [-1]
    for target in targets:
        total_count = 0
        for i in target:
            count = 101   # keymap의 원소길이 100보다 큰 값
            for key in keymap:
                if i in key:
                    count = min(count, key.index(i) + 1)
            if count == 101:
                total_count = 0
                break
            total_count += count
        if total_count == 0:
            answer.append(-1)
        else:
            answer.append(total_count)
    return answer