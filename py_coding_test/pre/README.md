# Coding Test

## 기본문법
1. 변수/자료형/형변환
```
str(a)
int(a)
float(a)
bool(a)
bin(10)
```

2. 연산자
```
a + b
a // b
```

3. 제어문(조건문)
```
if a == 10:
    pass
elif a > 10:
    pass
else:
    pass

for not i in [1, 2, 3]:
    pass
```

4. 제어문(반복문)
```
for i in range(N):
    pass
i = 0
while i < 100>:
    i += 1
```

5. 함수
```
def func(arg1, arg2):
    return art1 + arg2
```

6. 문자열
```
str.split(" ")
str.strip()
str[i].isdecimal()
str[i].isalpah()
str[i].upper()
str[i].lower()
str[i].isupper()
str[i].islower()
ord(str[i])
chr(97)
```

## 자료구조
1. 배열/리스트
```
arr = [0 for _ in range(N)]
arr.append(val)
arr.pop()
arr[i]
len(arr)
arr.sort(reverse=False)
arr.reverse()  # arr[::-1]
```

2. 딕셔너리
```
d = dict()
d[key] = val
d.get(key, None)
del d[key]
d.items()
d.keys()
d.valuse()
```

3. 셋(집합)
```
s = set()
s.add(val)
s.remove(val)
len(s)
```

4. 튜플
```
a, b = b, a
```

5. 덱
```
from collections import deque

dq = deque()
dq.append(val)
dq.appendleft(val)
dq.pop()
dq.popleft()
```

6. 힙
```
import headq

heap = []
heapq.heapify(heap)
heapq.push(heap, val)
heapq.pop(heap)
```

## 내장 함수
1. 수학
```
max()
min()
math.gcd(a, b)

```

2. 정렬
```
sorted(arr, key=lambda x: -x, reverse=True)
```