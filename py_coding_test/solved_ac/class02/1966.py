# 프린터 큐
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    document = []
    for index, priority in enumerate(input().split()):
        document.append((int(priority), index))
    sort_document = sorted(document, reverse=True)
    i = 0
    while document:
        if sort_document[i][0] == document[0][0]:
            if document[0][1] == M:
                break
            document.pop(0)
            i += 1
        else:
            num = document.pop(0)
            document.append(num)
    print(i+1)