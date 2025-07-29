# Hashing
L = int(input())
word = input()

answer = 0
for i in range(L):
    answer += ((ord(word[i]) - ord('a') + 1) * (31 ** i)) 
print(answer % 1234567891)