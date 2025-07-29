# 카드2
from collections import deque

N = int(input())
card = deque()
for i in range(1, N+1):
    card.append(i)
# 1개가 주어질 경우를 고려하여 길이 체크
while True:
    if len(card) == 1:
        answer = card[0]
        break
    card.popleft()
    num = card.popleft()
    card.append(num)

print(answer)

"""시간초과
N = int(input())

card = [i for i in range(1, N+1)]
answer = 0
while True:
    card.pop(0)
    if len(card) == 1:
        answer = card[0]
        break
    num = card.pop(0)
    card.append(num)
print(answer)
"""