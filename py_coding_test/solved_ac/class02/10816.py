# 숫자 카드 2
N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

card_dec = {}
for card in card1:
    if card_dec.get(card, None):
        card_dec[card] += 1
    else:
        card_dec[card] = 1
    
for card in card2:
    if card_dec.get(card, None):
        print(card_dec[card])
    else:
        print(0)
