# 달리기 경주
def solution(players, callings):
    answer = []
    # 시간 초과
    # for call in callings:
    #     idx = players.index(call)
    #     players[idx-1], players[idx] = players[idx], players[idx-1]
    # answer = players
    rankPlayer = {i: player for i, player in enumerate(players)}
    playerRank = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        idx = playerRank[call]
        otherPlayer = rankPlayer[idx - 1]
        rankPlayer[idx], rankPlayer[idx - 1] = rankPlayer[idx - 1], rankPlayer[idx]
        playerRank[call] -= 1
        playerRank[otherPlayer] += 1
    answer = list(rankPlayer.values())
    return answer