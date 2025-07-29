# 좌표 압축
## 중복된 숫자가 존재할 경우 주의!!
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(list(set(X)))
result = {}
for idx, val in enumerate(sort_X):
    result[val] = idx

for i in X:
    print(result[i], end =" ")


""" 시간초과
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sort_X = sorted(X)
result = []
for val in X:
    result.append(sort_X.index(val))

for i in result:
    print(i)
"""