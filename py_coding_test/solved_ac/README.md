# Beakjoon Online Judge

## Code Template
- Test Code
```cpp
with open('./solved_ac/class03/test.txt', 'r') as f:
    N, M = map(int, f.readline().split())
    board = []
    for _ in range(N):
        cols = list(map(int, f.readline().split()))
        board.append(cols)
```

- Submit Code
```cpp
N = int(input())
board = []
for _ in range(8):
    cols = list(map(int, input().split()))
    board.append(cols)
```

## Rule
- *(못 푼 문제) / **(여러번 풀어볼 분제)