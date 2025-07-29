# [한양대 HCPC 2023] Tren del Fin del Mundo
import sys

n = int(input())
x, y = 0, 0
min_y = 1001;
min_x = 0;
for i in range(n):
    x, y = map(int, input().split())
    if (y < min_y):
        min_x = x
        min_y = y
print(f"{min_x} {min_y}");
