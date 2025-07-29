#  [1차] 비밀지도
def num_to_bin(num):
    bin_num = ""
    while num > 0:
        bin_num += str(num % 2)
        num = num // 2
    return bin_num[::-1]

def change_len(s, n):
    if len(s) < n:
        return "0"*(n-len(s)) + s 
    else:
        return s

def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in range(n):
        map1.append([])
        for j in change_len(num_to_bin(arr1[i]), n):
            map1[i].append(j)
    
    for i in range(n):
        map2.append([])
        for j in change_len(num_to_bin(arr2[i]), n):
            map2[i].append(j)
    
    for i in range(n):
        str_map = ""
        for j in range(n):
            if map1[i][j] == "0" and map2[i][j] == "0":
                str_map += " "
            else:
                str_map += "#"
        answer.append(str_map)
        
    return answer