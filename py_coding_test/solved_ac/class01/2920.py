# 음계
data = list(map(int,input().split()))
asc = False
des = False

for i in range(len(data)-1):
    if data[i] < data[i+1]:
        asc = True
    elif data[i] > data[i+1]:
        des = True
        
if asc and des:
    print('mixed')
elif asc:
    print('ascending')
elif des:
    print('descending')