# 요세푸스 문제 0
from collections import deque
N, K = map(int, input().split())
dq = deque()

for i in range(1, N+1):
    dq.append(str(i))

answer = []
while dq:
    for _ in range(K-1):
        num = dq.popleft()
        dq.append(num)
    answer.append(dq.popleft())

answer = ", ".join(answer)
print(f"<{answer}>")

"""
from collections import deque

N, K = map(int,input().split())
data = deque([i for i in range(1,N+1)])
result = []

while len(data)>0:
    data.rotate(-K+1)
    num = data.popleft()
    result.append(str(num))
print('<'+', '.join(result)+'>')
"""