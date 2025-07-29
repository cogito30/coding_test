# [PCCE 기출문제] 10번 / 데이터 분석
def solution(data, ext, val_ext, sort_by):
    answer = []
    rows = ["code", "date", "maximum", "remain"]
    for i in data:
        idx = rows.index(ext)
        if i[idx] < val_ext:
            answer.append(i)
    sort_by = rows.index(sort_by)
    answer.sort(key = lambda x: x[sort_by])
    return answer