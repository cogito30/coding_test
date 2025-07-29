# 옹알이 (2)
def solution(babbling):
    answer = 0
    available_words = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        prev_word = []
        word = ""
        for i in babble:
            word += i
            if word in available_words:
                prev_word.append(word)
                word = ""
        for i in range(1, len(prev_word)):
            if prev_word[i-1] == prev_word[i]:
                word = "a" # 카운트 방지    
        if word == "" :
            answer += 1
        
    return answer