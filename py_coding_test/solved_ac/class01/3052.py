# 나머지
data = set()
for _ in range(10):
    num = int(input())
    data.add(num%42)
print(len(data))