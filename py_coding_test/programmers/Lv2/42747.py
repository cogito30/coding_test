# H-Index
def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    for idx, cite in enumerate(citations):
        if idx >= cite:
            answer = idx
            break
    # # [5, 6, 7, 8], 4
    # citations.sort(reverse=True)
    # for idx, cite in enumerate(citations):
    #     if idx + 1 >= cite:
    #         answer = max(cite, idx)
    #         break
    # if answer == 0 and (citations[-1] >= len(citations)):
    #     answer = len(citations)
    return answer